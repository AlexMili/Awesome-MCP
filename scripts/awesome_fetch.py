"""Parse the Awesome-MCP README and enrich each entry with GitHub signals
(stars, freshness = last push, archived flag, actual language).

Output: scripts/awesome_entries.json, the structured data awesome_gen.py uses
to regenerate the README organized by use case.

The source README is only read, never written.
Requires GITHUB_TOKEN (environment or scripts/.env).
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

import env_load  # noqa: F401  -- loads .env into os.environ on import

API = "https://api.github.com"
HERE = os.path.dirname(os.path.abspath(__file__))
README = os.path.join(os.path.dirname(HERE), "README.md")
OUT = os.path.join(HERE, "awesome_entries.json")

_GH_RE = re.compile(r"github\.com/([A-Za-z0-9][\w.-]*)/([A-Za-z0-9][\w.-]*)")
_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
_ALT_RE = re.compile(r'alt="([^"]+)"')


def parse_readme(path):
    """Parse the README in **table format** (the current source of truth).

    For each table row, extract name, url and description (first 2 columns).
    - under `## Servers`, the current `### <title>` is the **category** (picked
      by the contributor when editing the right table);
    - under `## SDKs`, the `### <title>` is the tier (Official/Community);
    - the `## ⭐ Featured` section is **skipped** (generated view, not a source);
    - the language is derived later from the repo; only a hint (the logo's alt
      text) is kept as a fallback when the API returns no application language.
    """
    top = category = tier = None
    out = []
    seen = set()  # dedupe on identical URL (e.g. Fast MCP listed under SDKs + Tools)
    with open(path, encoding="utf-8") as f:
        for raw in f:
            s = raw.rstrip("\n")
            if s.startswith("## "):
                top = s[3:].strip()
                category = tier = None
                continue
            if s.startswith("### "):
                head = s[4:].strip()
                if top == "Servers":
                    category = head
                else:
                    tier = head
                continue
            if not s.lstrip().startswith("|"):
                continue
            if top and "Featured" in top:        # generated view, skipped
                continue
            cells = [c.strip() for c in s.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            m = _LINK_RE.search(cells[0])
            if not m:                              # header / separator row
                continue
            url = m.group(2).strip()
            if url in seen:
                print(f"  (duplicate skipped: {m.group(1).strip()} — {url})", file=sys.stderr)
                continue
            seen.add(url)
            lang_hint = None
            if len(cells) >= 3:
                a = _ALT_RE.search(cells[2])
                if a:
                    lang_hint = a.group(1)
            out.append({
                "name": m.group(1).strip(),
                "url": m.group(2).strip(),
                "desc": cells[1].strip(),
                "top": top,
                "category": category,
                "language": lang_hint,
                "tier": tier,
            })
    return out


def repo_of(url):
    """owner/repo from any GitHub URL (tree/blob -> base repo)."""
    m = _GH_RE.search(url)
    if not m:
        return None
    repo = m.group(2)
    if repo.endswith(".git"):
        repo = repo[:-4]
    return f"{m.group(1)}/{repo}"


def gh_get(path, token):
    req = urllib.request.Request(f"{API}{path}", headers={
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "awesome-mcp-fetch",
    })
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)


def fetch_repo(full, token, cache):
    if full in cache:
        return cache[full]
    meta = {"stars": None, "pushed_at": None, "archived": None,
            "language": None, "full_name": full, "error": None}
    try:
        d = gh_get(f"/repos/{full}", token)
        meta["stars"] = d.get("stargazers_count")
        meta["pushed_at"] = d.get("pushed_at")
        meta["archived"] = d.get("archived")
        meta["language"] = d.get("language")
        meta["full_name"] = d.get("full_name") or full
    except urllib.error.HTTPError as e:
        meta["error"] = f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        meta["error"] = type(e).__name__
    cache[full] = meta
    return meta


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN missing (export it or put it in scripts/.env)")

    entries = parse_readme(sys.argv[1] if len(sys.argv) > 1 else README)
    cache = {}
    for i, e in enumerate(entries, 1):
        full = repo_of(e["url"])
        e["repo"] = full
        if full:
            e["gh"] = fetch_repo(full, token, cache)
            if e["gh"] not in (None,) and full not in list(cache)[:-1]:
                time.sleep(0.15)  # go easy on the API
        else:
            e["gh"] = None
        print(f"  [{i}/{len(entries)}] {e['name']:<28} {full or '(no repo)'} "
              f"-> {'' if not e.get('gh') else e['gh'].get('stars')}", file=sys.stderr)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    print(f"\n{len(entries)} entries -> {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
