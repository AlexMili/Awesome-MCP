"""Regenerate the Awesome-MCP README from awesome_entries.json.

Servers are organized by **use case** (no longer by language), in tables with
signals: actual language, freshness (last push), stars, official badge.
Clients / SDKs / Tools sections are kept.

Does NOT write the file itself: prints the README to stdout (redirect it).
Input: awesome_entries.json (produced by awesome_fetch.py).
Entries whose repo returns 404 are dropped; pass --keep-missing to keep them.
"""

import json
import os
import re
import sys
from datetime import datetime


def gh_anchor(s):
    """Mimic GitHub's anchor algorithm: lowercase, strip punctuation (except
    spaces/hyphens), spaces -> hyphens (without collapsing hyphens)."""
    s = s.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return s.replace(" ", "-")

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "awesome_entries.json")
FEATURED = os.path.join(HERE, "featured.txt")
# Reference date for freshness. Defaults to today. A hardcoded date would turn
# every repo pushed after it into "0d" (negative days, clamped by max(days,0) in
# freshness()), wrongly showing 🟢 0d everywhere.
# AWESOME_REF_DATE=YYYY-MM-DD pins the output (tests, stable diffs).
_REF_ENV = os.environ.get("AWESOME_REF_DATE")
REF = datetime.strptime(_REF_ENV, "%Y-%m-%d") if _REF_ENV else datetime.now()


def load_pinned():
    """Repos pinned at the top of `## ⭐ Featured`, one `owner/repo` per line.

    Optional file: missing or empty = original behavior (top 8 by stars).
    `#` comments and blank lines are ignored; file order is display order."""
    try:
        with open(FEATURED, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return []
    out = []
    for raw in lines:
        s = raw.split("#", 1)[0].strip()
        if s and s not in out:
            out.append(s)
    return out

# --- Use-case categories (display order) ---
CATS = [
    "Dev, Code & Git",
    "Databases & Data",
    "Cloud, DevOps & Monitoring",
    "Web, Search & Browser",
    "Productivity, Docs & Knowledge",
    "Communication & Social",
    "Commerce, Ads & Business",
    "AI, Agents & Memory",
    "Media & 3D",
    "Finance & Crypto",
    "Other",
]

# Categorization key -> category. Key = repo "owner/name", except for the
# official monorepos (modelcontextprotocol/servers|python-sdk) where the last
# URL segment (src/<x>) is used to tell each server apart.
CAT = {
    # monorepo servers (src/<x>)
    "filesystem": "Dev, Code & Git", "github": "Dev, Code & Git",
    "gitlab": "Dev, Code & Git", "git": "Dev, Code & Git",
    "gdrive": "Productivity, Docs & Knowledge", "postgres": "Databases & Data",
    "sqlite": "Databases & Data", "slack": "Communication & Social",
    "memory": "AI, Agents & Memory", "puppeteer": "Web, Search & Browser",
    "brave-search": "Web, Search & Browser", "google-maps": "Other",
    "aws-kb-retrieval-server": "Cloud, DevOps & Monitoring",
    "sentry": "Cloud, DevOps & Monitoring", "fetch": "Web, Search & Browser",
    "stdio.py": "Other", "websocket.py": "Other",
    # community / other repos
    "cloudflare/mcp-server-cloudflare": "Cloud, DevOps & Monitoring",
    "MindscapeHQ/mcp-server-raygun": "Cloud, DevOps & Monitoring",
    "ac3xx/mcp-servers-kagi": "Web, Search & Browser",
    "theishangoswami/exa-mcp-server": "Web, Search & Browser",
    "anaisbetts/mcp-youtube": "Web, Search & Browser",
    "joshrutkowski/applescript-mcp": "Other",
    "integromat/make-mcp-server": "Other",
    "biegehydra/BifrostMCP": "Dev, Code & Git",
    "microsoft/playwright-mcp": "Web, Search & Browser",
    "hyperdrive-eng/mcp-nodejs-debugger": "Dev, Code & Git",
    "cameroncooke/XcodeBuildMCP": "Dev, Code & Git",
    "joachimBrindeau/domain-mcp": "Other",
    "connerlambden/bgpt-mcp": "Web, Search & Browser",
    "taskade/mcp": "Productivity, Docs & Knowledge",
    "nicofains1/agentic-ads": "Commerce, Ads & Business",
    "pranciskus/newsmcp": "Web, Search & Browser",
    "preflight-dev/preflight": "Dev, Code & Git",
    "teamsincetoday/podcast-commerce-mcp": "Commerce, Ads & Business",
    "teamsincetoday/newsletter-commerce-mcp": "Commerce, Ads & Business",
    "teamsincetoday/recipe-commerce-mcp": "Commerce, Ads & Business",
    "octoco-ltd/sheetsdata-mcp": "Other",
    "Nadeus/toolradar-mcp": "Commerce, Ads & Business",
    "Writbase/writbase": "AI, Agents & Memory",
    "Frihet-io/frihet-mcp": "Commerce, Ads & Business",
    "Cleo-Labs-IA/skills_library": "Commerce, Ads & Business",
    "jabbawocky/proposalcraft": "Commerce, Ads & Business",
    "pierrebrunelle/mcp-server-openai": "AI, Agents & Memory",
    "baba786/phabricator-mcp-server": "Dev, Code & Git",
    "MarkusPfundstein/mcp-obsidian": "Productivity, Docs & Knowledge",
    "philgei/mcp_server_filesystem": "Dev, Code & Git",
    "zenml-io/mcp-zenml": "Cloud, DevOps & Monitoring",
    "ahujasid/blender-mcp": "Media & 3D",
    "lharries/whatsapp-mcp": "Communication & Social",
    "awslabs/mcp": "Cloud, DevOps & Monitoring",
    "microsoft/markitdown": "Productivity, Docs & Knowledge",
    "MervinPraison/praisonai-mcp": "AI, Agents & Memory",
    "elestirelbilinc-sketch/vap-showcase": "Media & 3D",
    "uju777/coupang-mcp": "Commerce, Ads & Business",
    "uju777/mcp-server-naver-search": "Web, Search & Browser",
    "Scottcjn/rustchain-mcp": "Finance & Crypto",
    "eidetic-works/nucleus-mcp": "AI, Agents & Memory",
    "FunplayAI/funplay-unity-mcp": "Media & 3D",
    "mark3labs/mcp-filesystem-server": "Dev, Code & Git",
    "github/github-mcp-server": "Dev, Code & Git",
    "HendryAvila/Hoofy": "Dev, Code & Git",
    "Muvon/octocode": "Dev, Code & Git",
}

MONOREPO = {"modelcontextprotocol/servers", "modelcontextprotocol/python-sdk"}
FIRSTPARTY = {
    "github/github-mcp-server", "cloudflare/mcp-server-cloudflare",
    "microsoft/playwright-mcp", "microsoft/markitdown", "awslabs/mcp", "taskade/mcp",
}
# "Generic" languages reported by the API (not the real application language)
# -> fall back to the language hint from the README.
GENERIC = {None, "", "HTML", "CSS", "Shell", "Dockerfile", "PLpgSQL", "Astro",
           "Go Template", "MDX", "SCSS", "Makefile", "Jupyter Notebook", "Batchfile"}

# Normalization -> single canonical name (no more TS vs Typescript).
NORMALIZE = {
    "typescript": "TypeScript", "javascript": "JavaScript", "python": "Python",
    "go": "Go", "golang": "Go", "rust": "Rust", "c#": "C#", "csharp": "C#",
    "java": "Java", "kotlin": "Kotlin",
}

# Canonical language -> official logo (devicon, brand-colored SVGs).
_DEVICON = "https://cdn.jsdelivr.net/gh/devicons/devicon/icons"
DEVICON = {
    "TypeScript": "typescript/typescript-original",
    "JavaScript": "javascript/javascript-original",
    "Python": "python/python-original",
    "Go": "go/go-original",
    "C#": "csharp/csharp-original",
    "Java": "java/java-original",
    "Kotlin": "kotlin/kotlin-original",
}
ICON_W = 18


def canon_lang(e):
    """Canonical language: GitHub's language when meaningful, else the README
    hint; normalized (TS == TypeScript)."""
    raw = (e.get("gh") or {}).get("language")
    if raw in GENERIC:
        raw = e.get("language")
    return NORMALIZE.get((raw or "").strip().lower(), (raw or "").strip())


def lang_badge(e):
    """Official language logo. Rust's is black -> <picture> that switches to
    white on dark theme to stay visible."""
    lang = canon_lang(e)
    if lang == "Rust":
        return ('<picture><source media="(prefers-color-scheme: dark)" '
                'srcset="https://cdn.simpleicons.org/rust/white">'
                f'<img src="{_DEVICON}/rust/rust-original.svg" width="{ICON_W}" '
                'alt="Rust" title="Rust"></picture>')
    path = DEVICON.get(lang)
    if not path:
        return lang or "—"
    return (f'<img src="{_DEVICON}/{path}.svg" width="{ICON_W}" '
            f'alt="{lang}" title="{lang}">')


def cat_key(e):
    repo = e.get("repo")
    if repo in MONOREPO:
        return e["url"].rstrip("/").rsplit("/", 1)[-1]
    return repo or e["name"]


def category(e):
    # Source of truth = the entry's own category (table heading edited by the
    # contributor). CAT is only a fallback for old data.
    return e.get("category") or CAT.get(cat_key(e)) or "Other"


def freshness(gh):
    """Freshness badge from pushed_at (+ archived)."""
    if gh and gh.get("error") == "HTTP 404":
        return "❌ gone"
    if not gh or gh.get("error") or not gh.get("pushed_at"):
        return "❔ unknown"
    if gh.get("archived"):
        return "🗄️ archived"
    try:
        d = datetime.strptime(gh["pushed_at"][:10], "%Y-%m-%d")
    except Exception:  # noqa: BLE001
        return "❔ unknown"
    days = (REF - d).days
    if days < 14:
        rel = f"{max(days,0)}d"
    elif days < 60:
        rel = f"{days // 7}w"
    elif days < 365:
        rel = f"{days // 30}mo"
    else:
        rel = f"{days // 365}y"
    if days <= 90:
        return f"🟢 {rel}"
    if days <= 365:
        return f"🟡 {rel}"
    return f"🔴 {rel}"


def stars(gh):
    if not gh or gh.get("stars") is None:
        return "—"
    n = gh["stars"]
    return f"{n/1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)

def stars_num(gh):
    return (gh or {}).get("stars") or -1


def is_official(e):
    return (e.get("tier") == "Official"
            or (e.get("repo") or "").startswith("modelcontextprotocol/")
            or e.get("repo") in FIRSTPARTY)


def name_cell(e):
    star = " ✅" if is_official(e) else ""
    return f"[{e['name']}]({e['url']}){star}"


def server_row(e):
    return (f"| {name_cell(e)} | {e['desc']} | {lang_badge(e)} | "
            f"{freshness(e.get('gh'))} | {stars(e.get('gh'))} |")


def main():
    entries = json.load(open(DATA, encoding="utf-8"))
    # Repo not found (404: deleted, renamed without redirect, or made private)
    # -> entry dropped from the README. `--keep-missing` keeps them.
    if "--keep-missing" not in sys.argv:
        kept = []
        for e in entries:
            if (e.get("gh") or {}).get("error") == "HTTP 404":
                print(f"  (repo 404, entry dropped: {e['name']} — {e['url']})", file=sys.stderr)
            else:
                kept.append(e)
        entries = kept
    servers = [e for e in entries if e["top"] == "Servers"]
    clients = [e for e in entries if e["top"] == "Clients"]
    sdks = [e for e in entries if e["top"] == "SDKs"]
    tools = [e for e in entries if e["top"] == "Tools"]

    out = []
    A = out.append

    # --- Header ---
    A("# Awesome MCP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    A("")
    A("> A curated list of [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) servers, clients, SDKs and tools.")
    A("")
    A("The Model Context Protocol (MCP) is an open protocol published by [Anthropic](https://www.anthropic.com/) "
      "in November 2024. It lets LLM apps connect to external data and tools. This list covers the whole ecosystem "
      "around the protocol, organized **by use case** so you can find what you need fast.")
    A("")
    A(f"_Servers are grouped by what they do. Each row shows the real language, repository activity "
      f"(last push) and stars. **✅ = official / first-party.** Activity legend: 🟢 ≤3 mo · 🟡 ≤1 yr · "
      f"🔴 >1 yr · 🗄️ archived · ❔ unknown. Signals auto-refreshed; last update {REF:%Y-%m-%d}._")
    A("")

    # --- Table of contents ---
    A("## Contents")
    A("")
    A("- [Servers](#servers)")
    for c in CATS:
        present = [e for e in servers if category(e) == c]
        if present:
            A(f"  - [{c}](#{gh_anchor(c)}) ({len(present)})")
    A("- [Clients](#clients)")
    A("- [SDKs](#sdks)")
    A("- [Tools](#tools)")
    A("")

    # --- Featured: pinned repos from featured.txt first, then filled with the
    # top-starred distinct servers (monorepos excluded), up to 8. A pinned repo
    # bypasses the monorepo exclusion: it is an explicit maintainer choice.
    by_repo = {e["repo"]: e for e in servers if e.get("repo")}
    seen, feat = set(), []
    for r in load_pinned():
        e = by_repo.get(r)
        if e is None:
            # stdout is the README: all diagnostics must go to stderr.
            print(f"  (pinned repo not found under Servers, skipped: {r})", file=sys.stderr)
            continue
        seen.add(r)
        feat.append(e)
    for e in sorted(servers, key=lambda x: stars_num(x.get("gh")), reverse=True):
        if len(feat) >= 8:
            break
        r = e.get("repo")
        if not r or r in MONOREPO or r in seen:
            continue
        seen.add(r)
        feat.append(e)
    A("## ⭐ Featured")
    A("")
    A("Standout community servers by traction and activity.")
    A("")
    A("| Server | Description | Lang | Activity | ⭐ |")
    A("|---|---|---|:--:|--:|")
    for e in feat:
        A(server_row(e))
    A("")
    A("> The canonical reference servers live in "
      "[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — listed by category below.")
    A("")

    # --- Servers by use case ---
    A("## Servers")
    A("")
    for c in CATS:
        group = [e for e in servers if category(e) == c]
        if not group:
            continue
        group.sort(key=lambda x: stars_num(x.get("gh")), reverse=True)
        A(f"### {c}")
        A("")
        A("| Server | Description | Lang | Activity | ⭐ |")
        A("|---|---|---|:--:|--:|")
        for e in group:
            A(server_row(e))
        A("")

    # --- Clients ---
    A("## Clients")
    A("")
    A("| Client | Description | Lang | Activity | ⭐ |")
    A("|---|---|---|:--:|--:|")
    for e in clients:
        A(server_row(e))
    A("")

    # --- SDKs ---
    A("## SDKs")
    A("")
    off = [e for e in sdks if e.get("tier") == "Official"]
    if off:
        A("### Official")
        A("")
        A("Core SDKs maintained by the MCP organization.")
        A("")
        A("| SDK | Notes | Activity | ⭐ |")
        A("|---|---|:--:|--:|")
        for e in off:
            A(f"| [{e['name']}]({e['url']}) | {e['desc']} | {freshness(e.get('gh'))} | {stars(e.get('gh'))} |")
        A("")
    comm = [e for e in sdks if e.get("tier") != "Official"]
    if comm:
        A("### Community")
        A("")
        # grouped by language (tier field under SDKs Community = #### <lang>)
        langs = []
        for e in comm:
            if e.get("language") not in langs:
                langs.append(e.get("language"))
        # the parser puts #### <lang> into 'tier'; simple fallback
        A("| SDK | Notes | Lang | Activity | ⭐ |")
        A("|---|---|---|:--:|--:|")
        for e in comm:
            A(server_row(e))
        A("")

    # --- Tools ---
    A("## Tools")
    A("")
    A("Tooling that helps you **build, test, secure, deploy or manage** MCP servers.")
    A("")
    A("| Tool | Description | Lang | Activity | ⭐ |")
    A("|---|---|---|:--:|--:|")
    for e in sorted(tools, key=lambda x: stars_num(x.get("gh")), reverse=True):
        A(server_row(e))
    A("")

    print("\n".join(out))


if __name__ == "__main__":
    main()
