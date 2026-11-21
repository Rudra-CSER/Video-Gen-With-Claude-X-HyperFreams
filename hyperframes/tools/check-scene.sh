#!/usr/bin/env bash
# `hyperframes check` for ONE scene: refreshes .preview/<id>/ and checks a real copy of it in
# .checks/<id>/ (tools/hf-lock.sh does the copy, because the check bundler skips symlinked
# scene files and would otherwise check nothing).
#   tools/check-scene.sh s05      (or the full scene id)
set -euo pipefail
HF="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$HF"
line="$(node tools/preview-scene.mjs "$1")"
id="$(basename "${line%% *}")"
exec tools/hf-lock.sh hyperframes check ".preview/$id" "${@:2}"
