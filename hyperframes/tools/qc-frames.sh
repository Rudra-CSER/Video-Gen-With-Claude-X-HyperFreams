#!/usr/bin/env bash
# Frames for human/agent QC of a rendered master: one JPEG every 0.25 s named by film time
# (frames/f_012.25.jpg) and one contact sheet per 10 s (sheets/sheet_010.jpg: 8 x 5 frames,
# 0.25 s apart, left to right, each labelled with its film time).
#   tools/qc-frames.sh <video.mp4> <outdir>
set -euo pipefail
V="$1"; OUT="$2"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FF="${HYPERFRAMES_FFMPEG_PATH:-$HOME/.local/bin/ffmpeg}"
rm -rf "$OUT"; mkdir -p "$OUT/frames" "$OUT/sheets"
# One frame per quarter second (the fps filter picks the frame nearest each tick), full resolution.
"$FF" -hide_banner -loglevel error -i "$V" -vf "fps=4" -q:v 3 "$OUT/frames/tmp_%05d.jpg"
python3 - "$OUT" "$HERE/../assets/fonts/SpaceMono-Bold.ttf" <<'PY'
import os, sys
from PIL import Image, ImageDraw, ImageFont
out, font_path = sys.argv[1], sys.argv[2]
fd = os.path.join(out, 'frames')
names = []
for f in sorted(os.listdir(fd)):
    if f.startswith('tmp_'):
        t = (int(f[4:9]) - 1) * 0.25
        n = f"f_{t:06.2f}.jpg"
        os.rename(os.path.join(fd, f), os.path.join(fd, n))
        names.append((t, n))
font = ImageFont.truetype(font_path, 16)
W, H, COLS, ROWS, PAD = 320, 180, 8, 5, 4
per = COLS * ROWS
for k in range(0, len(names), per):
    chunk = names[k:k + per]
    sheet = Image.new('RGB', (COLS * (W + PAD) + PAD, ROWS * (H + PAD) + PAD), (17, 17, 17))
    for i, (t, n) in enumerate(chunk):
        im = Image.open(os.path.join(fd, n)).convert('RGB').resize((W, H), Image.LANCZOS)
        d = ImageDraw.Draw(im)
        label = f"{t:6.2f}s"
        tw = d.textlength(label, font=font)
        d.rectangle([4, 4, 12 + tw, 26], fill=(0, 0, 0))
        d.text((8, 5), label, font=font, fill=(255, 255, 255))
        sheet.paste(im, (PAD + (i % COLS) * (W + PAD), PAD + (i // COLS) * (H + PAD)))
    sheet.save(os.path.join(out, 'sheets', f"sheet_{int(chunk[0][0]):03d}.jpg"), quality=88)
print(f"frames: {len(names)}  sheets: {len(os.listdir(os.path.join(out, 'sheets')))}  last frame t={names[-1][0]:.2f}s")
PY
