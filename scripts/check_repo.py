#!/usr/bin/env python3
"""Quality gate on the repository a pull request wants to add.

Reads the PR diff (same input as check_entry.py), finds the repository linked
by the added entry, asks the GitHub API about it, and rejects it when it is:
  - too young           (created less than MIN_AGE_DAYS days ago);
  - too little starred  (fewer than MIN_STARS stars);
  - not maintained      (last push more than MAX_INACTIVE_DAYS days ago);
  - archived, missing (404) or without a license.

Network errors other than 404 never reject a PR: the check fails open and
reports an error, so a GitHub outage cannot close legitimate contributions.

Requires GITHUB_TOKEN (environment or scripts/.env) for a usable rate limit.
Standard library only.

Exit codes: 0 repository accepted (or nothing to check), 1 rejected,
2 usage or input error, 3 GitHub API unavailable (inconclusive).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

import env_load  # noqa: F401  -- loads .env into os.environ on import
from check_entry import REPO_URL_RE, InputError, _read, check

API = "https://api.github.com"

# Thresholds. Edit here; the messages below follow automatically.
MIN_AGE_DAYS = 30
MIN_STARS = 10
MAX_INACTIVE_DAYS = 90

MESSAGES = {
    "REPO_NOT_FOUND": "The repository `{repo}` does not exist or is private.",
    "REPO_ARCHIVED": "The repository `{repo}` is archived, so it is no longer maintained.",
    "REPO_TOO_NEW": "The repository `{repo}` was created {age} day(s) ago; we require at least {min} days of existence.",
    "REPO_LOW_STARS": "The repository `{repo}` has {stars} star(s); we require at least {min}.",
    "REPO_INACTIVE": "The repository `{repo}` had no push for {days} days; we require activity within the last {max} days.",
    "REPO_NO_LICENSE": "The repository `{repo}` has no detectable license; please add one.",
}


class ApiUnavailable(Exception):
    pass


def gh_repo(full: str, token: str | None) -> dict | None:
    """Repository metadata, or None on 404. Raises ApiUnavailable otherwise."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-mcp-check-repo",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(f"{API}/repos/{full}", headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        if e.code in (404, 451):
            return None
        raise ApiUnavailable(f"HTTP {e.code}") from e
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        raise ApiUnavailable(type(e).__name__) from e


def _days_since(iso: str, now: datetime) -> int:
    then = datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    return max((now - then).days, 0)


def evaluate(meta: dict | None, full: str, now: datetime | None = None) -> list[dict]:
    """Issues for one repository's metadata (None = not found)."""
    now = now or datetime.now(timezone.utc)
    issues: list[dict] = []

    def add(code: str, **fmt) -> None:
        issues.append({"code": code, "message": MESSAGES[code].format(repo=full, **fmt)})

    if meta is None:
        add("REPO_NOT_FOUND")
        return issues
    if meta.get("archived"):
        add("REPO_ARCHIVED")
    if meta.get("created_at"):
        age = _days_since(meta["created_at"], now)
        if age < MIN_AGE_DAYS:
            add("REPO_TOO_NEW", age=age, min=MIN_AGE_DAYS)
    stars = meta.get("stargazers_count") or 0
    if stars < MIN_STARS:
        add("REPO_LOW_STARS", stars=stars, min=MIN_STARS)
    if meta.get("pushed_at"):
        days = _days_since(meta["pushed_at"], now)
        if days > MAX_INACTIVE_DAYS:
            add("REPO_INACTIVE", days=days, max=MAX_INACTIVE_DAYS)
    if not meta.get("license"):
        add("REPO_NO_LICENSE")
    return issues


def entry_repo(diff_text: str, readme_text: str) -> str | None:
    """owner/repo of the entry the PR adds, or None if there is none."""
    entry = check(diff_text, readme_text).get("entry")
    url = entry and entry.get("url")
    m = REPO_URL_RE.match(url) if url else None
    return f"{m.group('owner')}/{m.group('repo')}" if m else None


def render_text(result: dict) -> str:
    head = result["repo"] or "no repository to check"
    out = [f"{result['status'].upper()}  {head}"]
    for it in result["issues"]:
        out.append(f"  {it['code']}: {it['message']}")
    if result.get("error"):
        out.append(f"  ERROR: GitHub API unavailable ({result['error']}); check skipped.")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check the repository added by an Awesome-MCP pull request.")
    parser.add_argument("--diff", required=True, help="unified diff of the PR, '-' for stdin")
    parser.add_argument("--readme", required=True, help="README.md of the base branch")
    parser.add_argument("--json", action="store_true", help="print JSON instead of a summary")
    args = parser.parse_args(argv)
    if args.readme == "-" and args.diff == "-":
        parser.error("--diff and --readme cannot both read stdin")

    try:
        diff_text = _read(args.diff, "diff")
        readme_text = _read(args.readme, "README")
        repo = entry_repo(diff_text, readme_text)
    except InputError as exc:
        print(f"check_repo: {exc}", file=sys.stderr)
        return 2

    result = {"status": "ok", "repo": repo, "issues": [], "error": None}
    code = 0
    if repo:
        try:
            result["issues"] = evaluate(gh_repo(repo, os.environ.get("GITHUB_TOKEN")), repo)
        except ApiUnavailable as exc:
            result["status"], result["error"], code = "skipped", str(exc), 3
        else:
            if result["issues"]:
                result["status"], code = "fail", 1

    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else render_text(result))
    return code


if __name__ == "__main__":
    sys.exit(main())
