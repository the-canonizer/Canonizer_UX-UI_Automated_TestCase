#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PY="$ROOT_DIR/.venv/bin/python"
ENV_FILE="$ROOT_DIR/.env.local"

if [[ ! -x "$VENV_PY" ]]; then
  echo "Virtual environment not found. Run ./setup.sh first."
  exit 1
fi

if [[ -f "$ENV_FILE" ]]; then
  # shellcheck disable=SC1090
  set -a
  source "$ENV_FILE"
  set +a
fi

exec "$VENV_PY" "$ROOT_DIR/main.py" "$@"