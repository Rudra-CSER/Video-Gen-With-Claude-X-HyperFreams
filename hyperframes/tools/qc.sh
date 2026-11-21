#!/usr/bin/env bash
# Stage 7 quality control for a rendered MP4.
#   tools/qc.sh <video.mp4> <outdir>
# Writes: probe.json, blackdetect.txt, freezedetect.txt, contact sheets (every 0.5 s and every 2 s),
# and prints a short pass/fail summary for the spec (1920x1080, 60 fps, 105-120 s, H.264, no audio).
set -euo pipefail
V="$1"; OUT="$2"; mkdir -p "$OUT"
FF="${HYPERFRAMES_FFMPEG_PATH:-ffmpeg}"; FP="${HYPERFRAMES_FFPROBE_PATH:-ffprobe}"
"$FP" -v error -show_format -show_streams -of json "$V" > "$OUT/probe.json"
python3 - "$OUT/probe.json" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
v = [s for s in d['streams'] if s['codec_type'] == 'video'][0]
a = [s for s in d['streams'] if s['codec_type'] == 'audio']
num, den = map(int, v['r_frame_rate'].split('/'))
fps = num / den; dur = float(d['format']['duration'])
checks = [
  ('resolution 1920x1080', v['width'] == 1920 and v['height'] == 1080, f"{v['width']}x{v['height']}"),
  ('frame rate 60', abs(fps - 60) < 0.01, f'{fps:.3f}'),
  ('duration 105-120 s', 105 <= dur <= 120, f'{dur:.3f} s'),
  ('codec H.264', v['codec_name'] == 'h264', v['codec_name']),
  ('pixel format yuv420p', v.get('pix_fmt') == 'yuv420p', v.get('pix_fmt')),
  ('aspect 16:9', abs(v['width'] / v['height'] - 16 / 9) < 1e-3, v.get('display_aspect_ratio', '?')),
  ('no audio track (silent master)', not a, f'{len(a)} audio streams'),
]
for name, ok, val in checks: print(f"{'PASS' if ok else 'FAIL'}  {name:34s} {val}")
print(f"      frames: {v.get('nb_frames', '?')}  bitrate: {int(d['format'].get('bit_rate', 0)) // 1000} kb/s  size: {int(d['format']['size']) / 1e6:.1f} MB")
PY
"$FF" -hide_banner -nostats -i "$V" -vf "blackdetect=d=0.1:pix_th=0.04" -an -f null - 2> "$OUT/blackdetect.txt" || true
"$FF" -hide_banner -nostats -i "$V" -vf "freezedetect=n=0.0008:d=2.5" -an -f null - 2> "$OUT/freezedetect.txt" || true
B=$(command grep -c "black_start" "$OUT/blackdetect.txt" || true); F=$(command grep -c "freeze_start" "$OUT/freezedetect.txt" || true)
echo "black segments (>=0.1 s): $B   still segments (>=2.5 s): $F  (stills can be intended holds; see freezedetect.txt)"
# contact sheets: every 2 s (overview) and every 0.5 s (motion continuity), 960 px wide tiles
"$FF" -hide_banner -loglevel error -y -i "$V" -vf "fps=1/2,scale=480:-1,tile=6x10:padding=4:color=0x111111" -frames:v 1 "$OUT/sheet-every-2s.png"
"$FF" -hide_banner -loglevel error -y -i "$V" -vf "fps=2,scale=320:-1,tile=8x8:padding=3:color=0x111111" "$OUT/sheet-every-0.5s-%02d.png"
ls "$OUT" | sed 's/^/  /'
