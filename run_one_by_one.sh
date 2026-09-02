#!/usr/bin/env bash
#
# Run every collected test in its own pytest process, one at a time.
# Fresh browser per test, no shared-state bleed between tests.
# Written for the Bash 3.2 that ships with macOS (no mapfile / declare -A).
#
# Usage:
#   ./run_one_by_one.sh                 # run all, headless
#   ./run_one_by_one.sh --resume        # skip tests already recorded in the previous run
#   ./run_one_by_one.sh --no-headless   # watch the browser
#   ./run_one_by_one.sh -k thread       # only node ids whose name matches "thread"
#
# Output goes to: test_runs/<timestamp>/
#   results.tsv        STATUS<TAB>DURATION_S<TAB>NODEID   (one line per test)
#   <test>.log         full pytest output for that test
#   summary.txt        counts + list of failures, written at the end

set -uo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PY="$ROOT_DIR/.venv/bin/python"
ENV_FILE="$ROOT_DIR/.env.local"

[ -x "$VENV_PY" ] || { echo "No venv at $VENV_PY. Run ./setup.sh first."; exit 1; }

if [ -f "$ENV_FILE" ]; then
  set -a
  # shellcheck disable=SC1090
  . "$ENV_FILE"
  set +a
fi

# Speed: an unfound locator otherwise blocks for the full implicit wait.
export CANONIZER_IMPLICIT_WAIT="${CANONIZER_IMPLICIT_WAIT:-5}"

HEADLESS=1
RESUME=0
NAME_FILTER=""
while [ $# -gt 0 ]; do
  case "$1" in
    --no-headless) HEADLESS=0; shift ;;
    --headless)    HEADLESS=1; shift ;;
    --resume)      RESUME=1; shift ;;
    -k)            NAME_FILTER="${2:-}"; shift 2 ;;
    *) echo "Unknown arg: $1"; exit 2 ;;
  esac
done

RUN_DIR="$ROOT_DIR/test_runs/$(date +%Y%m%d-%H%M%S)"
mkdir -p "$RUN_DIR"
RESULTS="$RUN_DIR/results.tsv"
: > "$RESULTS"

# If resuming, seed results from the most recent previous run directory.
if [ "$RESUME" = "1" ]; then
  PREV=$(ls -dt "$ROOT_DIR"/test_runs/*/ 2>/dev/null | sed -n 2p)
  if [ -n "${PREV:-}" ] && [ -f "${PREV}results.tsv" ]; then
    echo "Resuming: carrying over results from ${PREV}results.tsv"
    cp "${PREV}results.tsv" "$RESULTS"
  fi
fi

echo "Collecting tests..."
NODES_FILE="$RUN_DIR/.nodes.txt"
"$VENV_PY" -m pytest --collect-only -q "$ROOT_DIR/main.py" 2>/dev/null | grep '::' > "$NODES_FILE"
if [ -n "$NAME_FILTER" ]; then
  grep -- "$NAME_FILTER" "$NODES_FILE" > "$NODES_FILE.tmp" && mv "$NODES_FILE.tmp" "$NODES_FILE"
fi

TOTAL=$(wc -l < "$NODES_FILE" | tr -d ' ')
echo "$TOTAL tests to run. Output dir: $RUN_DIR"
echo

i=0
pass=0; fail=0; other=0; skipped_resume=0
while IFS= read -r node; do
  [ -n "$node" ] || continue
  i=$((i+1))
  name="${node##*::}"

  # Already recorded (resume)? results.tsv lines end with a tab + the node id.
  if grep -qF "	$node" "$RESULTS" 2>/dev/null; then
    printf '[%3d/%d] %-70s SKIP (already done)\n' "$i" "$TOTAL" "$name"
    skipped_resume=$((skipped_resume+1))
    continue
  fi

  safe=$(printf '%s' "$name" | tr -c 'A-Za-z0-9_.-' '_')
  logf="$RUN_DIR/$safe.log"

  hl=""
  [ "$HEADLESS" = "1" ] && hl="--headless"

  start=$(date +%s)
  "$VENV_PY" -m pytest "$node" -v $hl -p no:cacheprovider > "$logf" 2>&1
  rc=$?
  end=$(date +%s)
  dur=$((end - start))

  case $rc in
    0) status="PASS"; pass=$((pass+1)) ;;
    1) status="FAIL"; fail=$((fail+1)) ;;
    5) status="NOTFOUND"; other=$((other+1)) ;;
    *) status="ERR($rc)"; other=$((other+1)) ;;
  esac

  printf '[%3d/%d] %-70s %s (%ds)\n' "$i" "$TOTAL" "$name" "$status" "$dur"
  printf '%s\t%s\t%s\n' "$status" "$dur" "$node" >> "$RESULTS"
done < "$NODES_FILE"

{
  echo "Run dir : $RUN_DIR"
  echo "Total   : $TOTAL"
  echo "Passed  : $pass"
  echo "Failed  : $fail"
  echo "Other   : $other   (NOTFOUND / errors)"
  [ "$skipped_resume" -gt 0 ] && echo "Skipped : $skipped_resume (resumed)"
  echo
  if [ "$fail" -gt 0 ] || [ "$other" -gt 0 ]; then
    echo "Non-passing:"
    grep -v '^PASS	' "$RESULTS" | sed 's/^/  /'
  fi
} | tee "$RUN_DIR/summary.txt"
