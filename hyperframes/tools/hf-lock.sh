#!/usr/bin/env bash
# Run a Chrome-heavy HyperFrames command (snapshot, check, validate, inspect, render)
# while holding one of a few shared slots, so parallel scene builders never start more
# headless Chromes than this machine (a shared QA box) can hold.
#   tools/hf-lock.sh hyperframes snapshot .preview/s03-sign-in --at 1,2.5
# Env: HF_LOCK_SLOTS (default 1), HF_MIN_FREE_MB (default 900). With ~1.2 GB usually free on this
# box, a 1800 MB floor made every launch sit out its full 10-minute memory wait; one Chrome at a
# time with a 900 MB floor runs a snapshot in seconds and stays clear of the OOM killer.
set -uo pipefail
HF="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$HF" || exit 1
# shellcheck disable=SC1091
. "$HF/hf-env.sh"
export PATH="$HF/node_modules/.bin:$PATH"
SLOTS="${HF_LOCK_SLOTS:-1}"
MIN_FREE_MB="${HF_MIN_FREE_MB:-900}"
LOCKS="$HF/.locks"; mkdir -p "$LOCKS"

# Lint is static (no Chrome, ~130 MB, under a second): never queue it behind the slots.
if [ "${1:-}" = "hyperframes" ] && [ "${2:-}" = "lint" ]; then exec "$@"; fi

# `hyperframes check .preview/<id>` would skip the symlinked scene file (the check bundler calls
# it "empty") and check nothing, so check a real copy of that preview in .checks/<id>/ instead.
if [ "${1:-}" = "hyperframes" ] && [ "${2:-}" = "check" ] && [[ "${3:-}" =~ ^(\./)?\.preview/([^/]+)/?$ ]]; then
  id="${BASH_REMATCH[2]}"; dst=".checks/$id"
  rm -rf "$dst"; mkdir -p "$dst/compositions"
  cp ".preview/$id/index.html" "$dst/index.html"
  cp -L ".preview/$id/compositions/"*.html "$dst/compositions/"
  ln -s "$HF/assets" "$dst/assets"
  set -- "$1" "$2" "$dst" "${@:4}"
fi

free_mb() { awk '/MemAvailable/ { printf "%d", $2 / 1024 }' /proc/meminfo; }

waited=0
while :; do
  for i in $(seq 1 "$SLOTS"); do
    exec {fd}>"$LOCKS/slot$i.lock"
    if flock -n "$fd"; then
      # Hold the slot, then wait (bounded) for enough free memory before launching Chrome.
      for _ in $(seq 1 200); do   # up to ~10 min
        [ "$(free_mb)" -ge "$MIN_FREE_MB" ] && break
        sleep 3
      done
      "$@" {fd}>&-; rc=$?   # the child does not inherit the lock fd, so stray processes cannot pin a slot
      flock -u "$fd"; exec {fd}>&-
      exit "$rc"
    fi
    exec {fd}>&-
  done
  if [ $((waited % 30)) -eq 0 ]; then echo "hf-lock: all $SLOTS slots busy, waiting..." >&2; fi
  sleep 2; waited=$((waited + 2))
done
