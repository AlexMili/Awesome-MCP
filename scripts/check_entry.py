#!/usr/bin/env python3
"""Deterministic form check for AlexMili/Awesome-MCP pull requests.

Reads the unified diff of a PR and the base-branch README.md, and decides
whether the PR adds exactly one well-formed table row at the end of an
existing section. No network, no LLM, standard library only.

Exit codes: 0 form is right, 1 at least one issue, 2 usage or input error.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field

README = "README.md"
DEFAULT_COLUMNS = 5

# Order in which issues are reported; also the full set of stable codes.
CODES = (
    "DELETED_LINE",
    "FILES_TOUCHED",
    "MULTIPLE_ENTRIES",
    "NO_ENTRY",
    "COLUMN_COUNT",
    "LINK_NOT_REPO",
    "LINK_IN_DESCRIPTION",
    "UNKNOWN_SECTION",
    "NEW_SECTION",
    "NOT_APPENDED",
    "FEATURED",
    "DUPLICATE",
    "CONTENTS_COUNT",
)

HUNK_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.*?)(?:[ \t]+#+)?[ \t]*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
SEPARATOR_RE = re.compile(r"^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")
CONTENTS_RE = re.compile(r"^(\s*[-*+]\s+\[(.+?)\]\(#[^)]*\)\s*\()(\d+)(\)\s*)$")
FIRST_CELL_RE = re.compile(r"^\[(?P<name>.+)\]\((?P<url>[^()\s]+)\)(?:\s*✅)?$")
REPO_URL_RE = re.compile(
    r"^https://github\.com/(?P<owner>[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)"
    r"/(?P<repo>[A-Za-z0-9._-]+?)(?:\.git)?"
    r"(?:/(?:tree|blob)/[^\s?#]+)?/?$"
)
ANY_GITHUB_RE = re.compile(r"https?://(?:www\.)?github\.com/([A-Za-z0-9-]+)/([A-Za-z0-9._-]+)")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\([^)]*\)")
BARE_URL_RE = re.compile(r"(?i)\b(?:https?://|www\.)\S+")


class InputError(Exception):
    """Unreadable or inconsistent input: exit code 2."""


# --------------------------------------------------------------------------
# Diff parsing


@dataclass
class Hunk:
    old_start: int
    old_count: int
    new_start: int
    new_count: int
    # (tag, text) with tag in " ", "-", "+"; tag "\\" marks "no newline at EOF".
    lines: list[tuple[str, str]] = field(default_factory=list)


@dataclass
class FileDiff:
    path: str
    hunks: list[Hunk] = field(default_factory=list)


def _strip_prefix(path: str) -> str | None:
    path = path.strip()
    if path.startswith('"') and path.endswith('"'):
        path = path[1:-1].encode("latin-1", "backslashreplace").decode("unicode_escape")
    if path == "/dev/null":
        return None
    if path[:2] in ("a/", "b/"):
        path = path[2:]
    return path


def parse_diff(text: str) -> list[FileDiff]:
    files: list[FileDiff] = []
    current: FileDiff | None = None
    old_path: str | None = None
    hunk: Hunk | None = None
    old_left = new_left = 0

    for raw in text.split("\n"):
        line = raw.rstrip("\r")
        if hunk is not None and (old_left > 0 or new_left > 0):
            tag = line[:1]
            if tag in (" ", "-", "+") or line == "":
                body = line[1:]
                tag = tag or " "
                hunk.lines.append((tag, body))
                if tag != "+":
                    old_left -= 1
                if tag != "-":
                    new_left -= 1
                continue
            if tag == "\\":
                hunk.lines.append(("\\", line))
                continue
            raise InputError(f"malformed hunk in diff near: {line[:80]!r}")
        if hunk is not None and line.startswith("\\"):
            hunk.lines.append(("\\", line))
            continue
        if hunk is not None and line[:1] in (" ", "+") and not line.startswith("+++ "):
            raise InputError(f"line outside hunk bounds in diff: {line[:80]!r}")
        hunk = None

        if line.startswith("diff --git "):
            m = re.match(r'^diff --git ("?a/.*?"?) ("?b/.*"?)$', line)
            path = _strip_prefix(m.group(2)) if m else line.split()[-1]
            current = FileDiff(path=path or "")
            files.append(current)
            old_path = _strip_prefix(m.group(1)) if m else None
        elif line.startswith("--- "):
            old_path = _strip_prefix(line[4:].split("\t")[0])
        elif line.startswith("+++ "):
            new_path = _strip_prefix(line[4:].split("\t")[0])
            path = new_path or old_path or ""
            if current is None or current.hunks:
                current = FileDiff(path=path)
                files.append(current)
            else:
                current.path = path
        elif line.startswith("@@"):
            m = HUNK_RE.match(line)
            if not m or current is None:
                raise InputError(f"malformed hunk header in diff: {line[:80]!r}")
            old_count = int(m.group(2)) if m.group(2) is not None else 1
            new_count = int(m.group(4)) if m.group(4) is not None else 1
            hunk = Hunk(int(m.group(1)), old_count, int(m.group(3)), new_count)
            current.hunks.append(hunk)
            old_left, new_left = old_count, new_count
        elif line.startswith(("rename from ", "rename to ", "copy from ", "copy to ")):
            if current is not None and line.startswith(("rename to ", "copy to ")):
                current.path = line.split(" ", 2)[2]
            elif current is not None:
                old_path = line.split(" ", 2)[2]

    if hunk is not None and (old_left > 0 or new_left > 0):
        # Tolerate a missing final context line (trailing newline trimmed).
        if old_left != new_left or old_left > 1:
            raise InputError("diff ends in the middle of a hunk")
    return files


# --------------------------------------------------------------------------
# Rebuilding the README after the PR


@dataclass
class NewLine:
    text: str
    old_index: int | None  # index in the base README, None for added lines
    added: bool


def _split_lines(text: str) -> list[str]:
    lines = [ln.rstrip("\r") for ln in text.split("\n")]
    if lines and lines[-1] == "":
        lines.pop()
    return lines


def apply_hunks(base: list[str], hunks: list[Hunk]) -> list[NewLine]:
    """Apply hunks to base, locating each by its context like `patch` does.

    The base README may have moved since the PR branched, so a hunk is placed
    at the nearest position where its old side matches, dropping leading or
    trailing context lines when needed.
    """
    out: list[NewLine] = []
    pos = 0
    drift = 0
    for hunk in hunks:
        body = [(t, s) for t, s in hunk.lines if t != "\\"]
        old_side = [s for t, s in body if t != "+"]
        lead = 0
        while lead < len(body) and body[lead][0] == " ":
            lead += 1
        trail = 0
        while trail < len(body) - lead and body[len(body) - 1 - trail][0] == " ":
            trail += 1
        expected = (hunk.old_start if hunk.old_count == 0 else hunk.old_start - 1) + drift

        # Rows land at the end of a table: the context after a hunk (blank
        # line, next heading) is stabler than the rows before it, so drop
        # leading context first.
        placed = None
        for fuzz in range(lead + trail + 1):
            for cut_lead in range(min(fuzz, lead), -1, -1):
                cut_trail = fuzz - cut_lead
                if cut_trail > trail:
                    continue
                block = old_side[cut_lead : len(old_side) - cut_trail]
                if not block and old_side:
                    continue
                best = None
                for p in range(pos, len(base) - len(block) + 1):
                    if base[p : p + len(block)] == block:
                        dist = abs(p - cut_lead - expected)
                        if best is None or dist < best[0]:
                            best = (dist, p)
                if not block:
                    best = (0, max(pos, min(expected, len(base))))
                if best is not None:
                    placed = (best[1], cut_lead, cut_trail)
                    break
            if placed:
                break
        if placed is None:
            raise InputError(
                f"hunk @@ -{hunk.old_start},{hunk.old_count} does not apply to the base README"
            )

        p, cut_lead, cut_trail = placed
        drift = p - cut_lead - (hunk.old_start - 1 if hunk.old_count else hunk.old_start)
        out.extend(NewLine(base[i], i, False) for i in range(pos, p))
        cursor = p
        for t, s in body[cut_lead : len(body) - cut_trail]:
            if t == "+":
                out.append(NewLine(s, None, True))
            elif t == "-":
                cursor += 1
            else:
                out.append(NewLine(base[cursor], cursor, False))
                cursor += 1
        pos = cursor
    out.extend(NewLine(base[i], i, False) for i in range(pos, len(base)))
    return out


# --------------------------------------------------------------------------
# README structure


def heading_key(text: str) -> str:
    """Comparison key for a heading: survives emoji variants, case, spacing."""
    text = unicodedata.normalize("NFKC", text).replace("️", "")
    return " ".join(text.split()).casefold()


def is_featured(key: str) -> bool:
    return re.sub(r"[^\w]", "", key) == "featured"


def headings(lines: list[str]) -> list[tuple[int, int, str]]:
    """(index, level, text) for every heading outside code fences."""
    found = []
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if m:
            found.append((i, len(m.group(1)), m.group(2).strip()))
    return found


def breadcrumbs(lines: list[str]) -> list[tuple[tuple[str, ...], ...] | None]:
    """For each line, the stack of (level, text) headings above it (level >= 2)."""
    marks = {i: (lvl, txt) for i, lvl, txt in headings(lines)}
    stack: list[tuple[int, str]] = []
    result = []
    for i in range(len(lines)):
        if i in marks:
            lvl, txt = marks[i]
            stack = [h for h in stack if h[0] < lvl]
            if lvl >= 2:
                stack.append((lvl, txt))
        result.append(tuple(stack))
    return result


def path_key(crumbs) -> tuple[str, ...]:
    return tuple(heading_key(t) for _, t in crumbs)


def split_row(line: str) -> list[str]:
    """Split a Markdown table row on unescaped pipes."""
    s = line.strip()
    cells, buf, i = [], [], 0
    while i < len(s):
        ch = s[i]
        if ch == "\\" and i + 1 < len(s):
            buf.append(s[i : i + 2])
            i += 2
            continue
        if ch == "|":
            cells.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
        i += 1
    cells.append("".join(buf))
    if s.startswith("|"):
        cells = cells[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        cells = cells[:-1]
    return [c.strip() for c in cells]


def is_table_line(line: str) -> bool:
    return line.lstrip().startswith("|")


def repo_key(owner: str, repo: str) -> str:
    repo = repo[:-4] if repo.lower().endswith(".git") else repo
    return f"{owner}/{repo}".lower()


def contents_counts(lines: list[str]) -> dict[str, tuple[int, str]]:
    """heading key -> (count, raw line) for the counters under ## Contents."""
    counts: dict[str, tuple[int, str]] = {}
    inside = False
    marks = {i: (lvl, txt) for i, lvl, txt in headings(lines)}
    for i, line in enumerate(lines):
        if i in marks:
            lvl, txt = marks[i]
            if lvl <= 2:
                inside = heading_key(txt) == "contents"
            continue
        if inside:
            m = CONTENTS_RE.match(line)
            if m:
                counts[heading_key(m.group(2))] = (int(m.group(3)), line)
    return counts


# --------------------------------------------------------------------------
# The check


MESSAGES = {
    "DELETED_LINE": "Do not remove or edit existing lines; restore the {n} deleted line(s) and only add your entry.",
    "FILES_TOUCHED": "Only README.md may be changed; revert your changes to {files}.",
    "MULTIPLE_ENTRIES": "Add exactly one entry per pull request; split these {n} rows into separate pull requests.",
    "NO_ENTRY": "Add your project as one table row of the form `| [Name](https://github.com/owner/repo) | Description. | | | |` in README.md.",
    "COLUMN_COUNT": "Give the row exactly {expected} columns, like the other rows of the table (it has {got}).",
    "LINK_NOT_REPO": "Start the row with `[Name](https://github.com/owner/repo)`, linking the GitHub repository itself (a `/tree/...` path is fine for a monorepo).",
    "LINK_IN_DESCRIPTION": "Remove the link from the description; the only link in the row should be the repository link in the first column.",
    "UNKNOWN_SECTION": "Add the row inside one of the existing sections of the README ({section} does not exist).",
    "NEW_SECTION": "Do not create new headings; add your row to the existing section that fits best.",
    "NOT_APPENDED": "Add the row as the last line of an existing section table, just before the blank line that closes it, without moving other rows.",
    "FEATURED": "Do not add entries to Featured, which the maintainer curates; add the row to the matching category under Servers instead.",
    "DUPLICATE": "This repository ({repo}) is already listed in the README; drop the pull request or update the existing entry instead.",
    "CONTENTS_COUNT": "Increment the counter of `{section}` in the Contents list from {old} to {expected}.",
}


def check(diff_text: str, readme_text: str) -> dict:
    files = parse_diff(diff_text)
    base = _split_lines(readme_text)
    issues: list[dict] = []

    def issue(code: str, line: str | None, **fmt) -> None:
        # One issue per code: the first offending line stands for the others.
        if any(it["code"] == code for it in issues):
            return
        issues.append({"code": code, "message": MESSAGES[code].format(**fmt), "line": line})

    readme_diffs = [f for f in files if f.path == README]
    other_paths = sorted({f.path for f in files if f.path != README})
    hunks = [h for f in readme_diffs for h in f.hunks]

    # Removed lines, all files, verbatim.
    deletions: list[str] = []
    for f in files:
        for h in f.hunks:
            deletions.extend(s for t, s in h.lines if t == "-")

    readme_added = [s for h in hunks for t, s in h.lines if t == "+"]
    readme_removed = []
    for h in hunks:
        body = h.lines
        for k, (t, s) in enumerate(body):
            if t != "-":
                continue
            noeol = k + 1 < len(body) and body[k + 1][0] == "\\"
            readme_removed.append((s, noeol))

    # Exempt: a Contents counter rewritten in place, and a last line
    # re-added only to fix a missing newline at end of file.
    added_counter_stems = {m.group(1) + "#" + m.group(4) for s in readme_added if (m := CONTENTS_RE.match(s))}
    real_deletions = [
        s
        for s, noeol in readme_removed
        if not (
            (m := CONTENTS_RE.match(s)) and m.group(1) + "#" + m.group(4) in added_counter_stems
        )
        and not (noeol and s in readme_added)
    ]
    for f in files:
        if f.path != README:
            real_deletions.extend(s for h in f.hunks for t, s in h.lines if t == "-")
    if real_deletions:
        issue("DELETED_LINE", real_deletions[0], n=len(real_deletions))

    if other_paths:
        issue("FILES_TOUCHED", None, files=", ".join(other_paths))

    new = apply_hunks(base, hunks) if hunks else [NewLine(s, i, False) for i, s in enumerate(base)]
    new_text = [n.text for n in new]
    new_crumbs = breadcrumbs(new_text)
    base_crumbs = breadcrumbs(base)
    base_paths = {path_key(c) for c in base_crumbs if c}
    for i, _, _ in headings(base):
        base_paths.add(path_key(base_crumbs[i]))

    # Added table rows that are entries, not header or separator.
    entries: list[int] = []
    for i, n in enumerate(new):
        if not n.added or not is_table_line(n.text):
            continue
        if SEPARATOR_RE.match(n.text.strip()):
            continue
        if i + 1 < len(new) and SEPARATOR_RE.match(new[i + 1].text.strip()):
            continue
        entries.append(i)

    if len(entries) > 1:
        issue("MULTIPLE_ENTRIES", new[entries[1]].text, n=len(entries))
    if not entries:
        issue("NO_ENTRY", None)

    new_headings = [
        n.text
        for i, n in enumerate(new)
        if n.added and (m := HEADING_RE.match(n.text)) and len(m.group(1)) in (2, 3)
    ]
    if new_headings:
        issue("NEW_SECTION", new_headings[0])

    known_repos = {repo_key(o, r) for o, r in ANY_GITHUB_RE.findall(readme_text)}
    base_counts = contents_counts(base)
    new_counts = contents_counts(new_text)
    per_section: dict[str, list[int]] = {}

    entry_obj = None
    section = None
    for rank, i in enumerate(entries):
        line = new[i].text
        cells = split_row(line)
        crumbs = new_crumbs[i]
        key = path_key(crumbs)
        label = " › ".join(t for _, t in crumbs) if crumbs else None

        # The table this row belongs to: contiguous "|" lines around it.
        top = i
        while top > 0 and is_table_line(new[top - 1].text):
            top -= 1
        bottom = i
        while bottom + 1 < len(new) and is_table_line(new[bottom + 1].text):
            bottom += 1
        has_header = bottom - top >= 2 and SEPARATOR_RE.match(new[top + 1].text.strip())
        expected_cols = len(split_row(new[top].text)) if has_header else DEFAULT_COLUMNS

        name = url = None
        if cells:
            m = FIRST_CELL_RE.match(cells[0])
            if m:
                name, url = m.group("name").strip(), m.group("url")
        description = cells[1] if len(cells) > 1 else None

        if rank == 0:
            entry_obj = {"name": name, "url": url, "description": description, "line": line}
            section = label

        if len(cells) != expected_cols:
            issue("COLUMN_COUNT", line, expected=expected_cols, got=len(cells))

        repo_match = REPO_URL_RE.match(url) if url else None
        if not repo_match:
            issue("LINK_NOT_REPO", line)

        if description is not None and (MD_LINK_RE.search(description) or BARE_URL_RE.search(description)):
            issue("LINK_IN_DESCRIPTION", line)

        if not crumbs or key not in base_paths:
            issue("UNKNOWN_SECTION", line, section=f"`{label}`" if label else "the top of the file")

        # Appended: last row of an existing table (header + separator on top),
        # followed by a blank line or EOF, and the other rows unchanged.
        appended = bool(has_header) and bottom == i and top + 2 <= i
        if appended and bottom + 1 < len(new) and new[bottom + 1].text.strip() != "":
            appended = False
        if appended:
            kept = [n.old_index for n in new[top : bottom + 1] if not n.added]
            if not kept or kept != list(range(kept[0], kept[0] + len(kept))):
                appended = False
            else:
                o_top, o_bottom = kept[0], kept[-1]
                if (o_top > 0 and is_table_line(base[o_top - 1])) or (
                    o_bottom + 1 < len(base) and is_table_line(base[o_bottom + 1])
                ):
                    appended = False
        if not appended:
            issue("NOT_APPENDED", line)

        if crumbs and is_featured(heading_key(crumbs[0][1])):
            issue("FEATURED", line)

        if repo_match:
            rk = repo_key(repo_match.group("owner"), repo_match.group("repo"))
            if rk in known_repos:
                issue("DUPLICATE", line, repo=rk)

        if len(crumbs) >= 2 and heading_key(crumbs[0][1]) == "servers":
            per_section.setdefault(crumbs[1][1], []).append(i)

    for sub, rows in per_section.items():
        k = heading_key(sub)
        if k not in base_counts:
            continue  # unknown sub-section, already reported
        old = base_counts[k][0]
        got = new_counts.get(k, (None, ""))[0]
        if got != old + len(rows):
            issue("CONTENTS_COUNT", new[rows[0]].text, section=sub, old=old, expected=old + len(rows))

    order = {c: n for n, c in enumerate(CODES)}
    issues.sort(key=lambda d: order[d["code"]])
    return {
        "ok": not issues,
        "issues": issues,
        "entry": entry_obj,
        "section": section,
        "deletions": deletions,
    }


# --------------------------------------------------------------------------
# CLI


def _read(path: str, what: str) -> str:
    try:
        if path == "-":
            return sys.stdin.buffer.read().decode("utf-8")
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except (OSError, UnicodeDecodeError) as exc:
        raise InputError(f"cannot read {what} {path!r}: {exc}") from exc


def render_text(result: dict) -> str:
    entry = result["entry"]
    where = result["section"] or "unknown section"
    head = f"{entry['name'] or entry['line']} → {where}" if entry else "no entry"
    if result["ok"]:
        return f"OK  {head}"
    out = [f"FAIL  {head}"]
    for it in result["issues"]:
        out.append(f"  {it['code']}: {it['message']}")
        if it["line"] is not None:
            out.append(f"      {it['line'][:120]}")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check the form of an Awesome-MCP pull request.")
    parser.add_argument("--diff", required=True, help="unified diff of the PR, '-' for stdin")
    parser.add_argument("--readme", required=True, help="README.md of the base branch")
    parser.add_argument("--json", action="store_true", help="print JSON instead of a summary")
    args = parser.parse_args(argv)
    if args.readme == "-" and args.diff == "-":
        parser.error("--diff and --readme cannot both read stdin")

    try:
        diff_text = _read(args.diff, "diff")
        readme_text = _read(args.readme, "README")
        result = check(diff_text, readme_text)
    except InputError as exc:
        print(f"check_entry: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
