# Source before any hyperframes command:  . ./hf-env.sh
# Keeps HyperFrames offline-friendly and private on this machine.
export HYPERFRAMES_SKIP_SKILLS=1          # never install agent skills into ~/.claude
export HYPERFRAMES_NO_TELEMETRY=1         # no anonymous usage telemetry
export HYPERFRAMES_NO_UPDATE_CHECK=1
export HYPERFRAMES_NO_AUTO_INSTALL=1
# Reuse the Chrome for Testing 151 builds Playwright already downloaded (no 150 MB browser download).
# Any other machine: the first existing candidate wins (set the variables yourself to override).
_hf_first() { for p in "$@"; do [ -x "$p" ] && { printf '%s' "$p"; return; }; done; }
: "${HYPERFRAMES_BROWSER_PATH:=$(_hf_first \
  "$HOME/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome" \
  /opt/google/chrome/chrome /usr/bin/google-chrome)}"
: "${PRODUCER_HEADLESS_SHELL_PATH:=$(_hf_first \
  "$HOME/.cache/ms-playwright/chromium_headless_shell-1234/chrome-headless-shell-linux64/chrome-headless-shell" \
  /opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux64/chrome-headless-shell)}"
: "${HYPERFRAMES_FFMPEG_PATH:=$(_hf_first "$HOME/.local/bin/ffmpeg" "$(command -v ffmpeg)")}"
: "${HYPERFRAMES_FFPROBE_PATH:=$(_hf_first "$HOME/.local/bin/ffprobe" "$(command -v ffprobe)")}"
export HYPERFRAMES_BROWSER_PATH PRODUCER_HEADLESS_SHELL_PATH HYPERFRAMES_FFMPEG_PATH HYPERFRAMES_FFPROBE_PATH
unset -f _hf_first
export PATH="$PWD/node_modules/.bin:$PATH"
