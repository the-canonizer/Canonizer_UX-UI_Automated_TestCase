#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$ROOT_DIR/.venv"
PYTHON_BIN="${PYTHON_BIN:-python3}"
ENV_FILE="$ROOT_DIR/.env.local"
ENV_TEMPLATE="$ROOT_DIR/.env.local.example"

if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
  echo "python3 is required but was not found in PATH."
  exit 1
fi

CHROME_APP="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

if [[ ! -x "$CHROME_APP" ]] && ! command -v google-chrome >/dev/null 2>&1; then
  echo "Warning: Google Chrome was not found in PATH. Install Chrome before running the UI tests."
fi

if [[ ! -d "$VENV_DIR" ]]; then
  "$PYTHON_BIN" -m venv "$VENV_DIR"
fi

"$VENV_DIR/bin/python" -m pip install --upgrade pip
"$VENV_DIR/bin/python" -m pip install -r "$ROOT_DIR/requirements.txt"

if [[ ! -f "$ENV_FILE" ]]; then
  if [[ -f "$ENV_TEMPLATE" ]]; then
    cp "$ENV_TEMPLATE" "$ENV_FILE"
    chmod 600 "$ENV_FILE"
    echo "Created .env.local from .env.local.example"
  fi

  canonizer_user="${CANONIZER_DEFAULT_USER:-}"
  canonizer_pass="${CANONIZER_DEFAULT_PASS:-}"

  if [[ -z "$canonizer_user" || -z "$canonizer_pass" ]]; then
    if [[ -t 0 ]]; then
      echo "Set your Canonizer login credentials for local runs."
      if [[ -z "$canonizer_user" ]]; then
        read -r -p "CANONIZER_DEFAULT_USER (leave blank to skip): " canonizer_user
      fi
      if [[ -z "$canonizer_pass" ]]; then
        read -r -s -p "CANONIZER_DEFAULT_PASS (leave blank to skip): " canonizer_pass
        echo
      fi
    fi
  fi

  if [[ -n "$canonizer_user" || -n "$canonizer_pass" ]]; then
    {
      if [[ -n "$canonizer_user" ]]; then
        printf 'export CANONIZER_DEFAULT_USER=%q\n' "$canonizer_user"
      fi
      if [[ -n "$canonizer_pass" ]]; then
        printf 'export CANONIZER_DEFAULT_PASS=%q\n' "$canonizer_pass"
      fi
    } > "$ENV_FILE"
    chmod 600 "$ENV_FILE"
    echo "Saved local credentials to .env.local"
  else
    echo "Edit .env.local to set CANONIZER_DEFAULT_USER and CANONIZER_DEFAULT_PASS before running login-required tests."
  fi
fi

cat <<EOF
Setup complete.

Next steps:
1. Run all tests: ./run_tests.sh
2. Run a single test: ./run_tests.sh -k test_login_to_canonizer -q
3. Run main.py directly from the VS Code Run button; it now executes pytest.
EOF