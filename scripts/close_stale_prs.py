#!/usr/bin/env python3
"""Close open pull requests left waiting on their author.

A PR is closed when both hold:
  - no activity for at least --days days (default 30);
  - the last comment or action on it was made by the maintainer (--maintainer),
    i.e. the ball is in the contributor's court and they never answered.

Activity is read from the PR timeline (comments, reviews, commits, labels,
force pushes...). Bot actions (github-actions, dependabot...) and pure
notification events (mentioned, subscribed) are ignored, so the closing
comment of a previous run or a CI bot never counts as activity. Commits are
attributed to the contributor, never to the maintainer.

Requires GITHUB_TOKEN (environment or scripts/.env), with pull-requests write
access unless --dry-run is given. Standard library only.

Exit codes: 0 success, 1 API error.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

import env_load  # noqa: F401  -- loads .env into os.environ on import

API = "https://api.github.com"
DEFAULT_REPO = "AlexMili/Awesome-MCP"
DEFAULT_MAINTAINER = "AlexMili"
DEFAULT_DAYS = 30

# Timeline events that are notifications, not something someone did on the PR.
IGNORED_EVENTS = {"mentioned", "subscribed", "unsubscribed"}

CLOSE_COMMENT = (
    "Closing this pull request as it has had no activity for {days} days "
    "since the last maintainer feedback. Feel free to reopen it, or open a "
    "new one, once the requested changes are in. Thanks for the contribution!"
)


class ApiError(Exception):
    pass


def _request(method: str, url: str, token: str, body: dict | None = None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = resp.read()
            return json.loads(payload) if payload else None, resp.headers.get("Link", "")
    except urllib.error.HTTPError as e:
        raise ApiError(f"{method} {url} -> {e.code} {e.read().decode(errors='replace')[:200]}")


def _next_link(link_header: str) -> str | None:
    for part in link_header.split(","):
        url, _, rel = part.partition(";")
        if 'rel="next"' in rel:
            return url.strip().strip("<>")
    return None


def get_all(url: str, token: str) -> list:
    out = []
    sep = "&" if "?" in url else "?"
    next_url: str | None = f"{url}{sep}per_page=100"
    while next_url:
        page, link = _request("GET", next_url, token)
        out.extend(page)
        next_url = _next_link(link)
    return out


def _parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _is_bot(user: dict | None) -> bool:
    if not user:
        return False
    return user.get("type") == "Bot" or user.get("login", "").endswith("[bot]")


def event_actor_and_time(event: dict) -> tuple[str | None, datetime | None]:
    """Who did this timeline event and when. (None, None) when it does not count.

    Commits carry a git author, not a GitHub account: their actor is reported
    as "" so they are never taken for the maintainer.
    """
    kind = event.get("event")
    if kind in IGNORED_EVENTS:
        return None, None
    if kind == "committed":
        date = (event.get("committer") or {}).get("date") or (event.get("author") or {}).get("date")
        return "", _parse_time(date) if date else None
    if kind == "reviewed":
        user, when = event.get("user"), event.get("submitted_at")
    else:
        user = event.get("actor") or event.get("user")
        when = event.get("created_at")
    if user is None or _is_bot(user) or not when:
        return None, None
    return user.get("login", ""), _parse_time(when)


def last_activity(pr: dict, timeline: list) -> tuple[str, datetime]:
    """Most recent human actor and time on the PR; the opening counts as the author's."""
    actor, when = pr["user"]["login"], _parse_time(pr["created_at"])
    for event in timeline:
        a, t = event_actor_and_time(event)
        if a is not None and t is not None and t >= when:
            actor, when = a, t
    return actor, when


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPO))
    parser.add_argument("--maintainer", default=DEFAULT_MAINTAINER,
                        help="login whose last action means the PR waits on its author")
    parser.add_argument("--days", type=int, default=DEFAULT_DAYS)
    parser.add_argument("--dry-run", action="store_true", help="report only, close nothing")
    args = parser.parse_args(argv)

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        print("GITHUB_TOKEN missing (environment or scripts/.env).", file=sys.stderr)
        return 1

    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=args.days)
    maintainer = args.maintainer.lower()
    matched = 0

    try:
        prs = get_all(f"{API}/repos/{args.repo}/pulls?state=open", token)
        print(f"{len(prs)} open pull request(s) in {args.repo}.")
        for pr in prs:
            number = pr["number"]
            timeline = get_all(f"{API}/repos/{args.repo}/issues/{number}/timeline", token)
            actor, when = last_activity(pr, timeline)
            idle = (now - when).days
            stale = when <= cutoff
            by_maintainer = actor.lower() == maintainer
            label = f"#{number} last activity {idle}d ago by {actor or 'a commit'}"

            if not (stale and by_maintainer):
                print(f"  keep   {label}")
                continue

            matched += 1
            if args.dry_run:
                print(f"  WOULD CLOSE {label}")
                continue

            _request("POST", f"{API}/repos/{args.repo}/issues/{number}/comments", token,
                     {"body": CLOSE_COMMENT.format(days=args.days)})
            _request("PATCH", f"{API}/repos/{args.repo}/pulls/{number}", token, {"state": "closed"})
            print(f"  CLOSED {label}")
    except ApiError as e:
        print(f"GitHub API error: {e}", file=sys.stderr)
        return 1

    verb = "would be closed" if args.dry_run else "closed"
    print(f"Done: {matched} pull request(s) {verb}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
