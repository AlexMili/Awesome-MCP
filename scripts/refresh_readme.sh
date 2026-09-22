#!/usr/bin/env bash
#
# Refresh the Awesome-MCP data and regenerate the README.
# NO git operations (pull/commit/push are left to you).
#
#   1. GITHUB_TOKEN: environment, else scripts/.env, else `gh auth token`
#   2. awesome_fetch.py: README (tables) -> awesome_entries.json + fresh signals
#   3. awesome_gen.py:   awesome_entries.json -> regenerated README
#
# Entries whose repo returns 404 are dropped from the README.
#
# Usage:
#   scripts/refresh_readme.sh
#   scripts/refresh_readme.sh /path/to/README.md   # alternative target
#
set -euo pipefail

# Directory of this script (= scripts/), whatever the cwd.
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

README="${1:-$DIR/../README.md}"

# --- prerequisites ---
command -v python3 >/dev/null 2>&1 || { echo "❌ python3 not found."; exit 1; }

# --- load the token ---
if [ -f "$DIR/.env" ]; then
  set -a
  # shellcheck disable=SC1091
  . "$DIR/.env"
  set +a
fi
if [ -z "${GITHUB_TOKEN:-}" ] && command -v gh >/dev/null 2>&1; then
  GITHUB_TOKEN="$(gh auth token 2>/dev/null || true)"
  export GITHUB_TOKEN
fi
[ -n "${GITHUB_TOKEN:-}" ] || { echo "❌ GITHUB_TOKEN missing (env, scripts/.env or gh auth login)."; exit 1; }

if [ ! -f "$README" ]; then
  echo "❌ Source README not found: $README"
  echo "   (pass the right path as an argument)"
  exit 1
fi

echo "▸ 1/2  Fetching GitHub signals (stars, freshness, language)…"
python3 "$DIR/awesome_fetch.py" "$README"

echo "▸ 2/2  Regenerating README -> $README"
TMP="$(mktemp)"
python3 "$DIR/awesome_gen.py" > "$TMP"
mv "$TMP" "$README"

echo "✅ Done. README refreshed: $README"
echo "   (git pull/commit/push left to you)"
