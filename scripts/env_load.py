"""Load .env into os.environ, with no external dependency.

Import this module at the top of each entry point: `import env_load  # noqa`.
.env WINS: its values override an already exported shell variable
(otherwise a stale exported GITHUB_TOKEN would shadow the refreshed one -> 401)."""

import os

_ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")


def load(path=_ENV_PATH, override=True):
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if key and (override or key not in os.environ):
                os.environ[key] = val


load()
