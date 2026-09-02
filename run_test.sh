#!/usr/bin/env bash
#
# Run a SINGLE test by method name, with a VISIBLE browser window.
#
#   ./run_test.sh test_click_on_join_now
#   ./run_test.sh test_create_topic_name_with_valid_data
#   ./run_test.sh test_login_to_canonizer -s        # extra pytest args pass through
#
# Add --headless as an extra arg if you ever want it hidden.

set -uo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PY="$ROOT_DIR/.venv/bin/python"

[ -x "$VENV_PY" ] || { echo "No venv at $VENV_PY. Run ./setup.sh first."; exit 1; }

if [ -f "$ROOT_DIR/.env.local" ]; then
  set -a
  # shellcheck disable=SC1090
  . "$ROOT_DIR/.env.local"
  set +a
fi

# Unfound locators otherwise block for the full implicit wait.
export CANONIZER_IMPLICIT_WAIT="${CANONIZER_IMPLICIT_WAIT:-5}"

[ $# -ge 1 ] || { echo "usage: ./run_test.sh <test_method_name> [extra pytest args]"; exit 2; }

NAME="$1"; shift
exec "$VENV_PY" -m pytest "$ROOT_DIR/main.py::TestPages::$NAME" -v "$@"
