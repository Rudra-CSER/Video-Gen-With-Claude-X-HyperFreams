// Copy the real UI captures into the HyperFrames project, encode frame sequences
// (typing / scrolling) into 60 fps clips, and collect every element mark.
//   node tools/sync-assets.mjs [screensDir]
import { readdir, mkdir, copyFile, readFile, writeFile, stat } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import os from 'node:os';
import { rm } from 'node:fs/promises';

const HF = path.resolve(new URL('..', import.meta.url).pathname);
const SRC = path.resolve(process.argv[2] || path.join(HF, '../assets/screens'));
const UI = path.join(HF, 'assets/ui');
const CLIPS = path.join(HF, 'assets/clips');
const FFMPEG = process.env.HYPERFRAMES_FFMPEG_PATH || 'ffmpeg';

// How many 60 fps video frames each captured frame is held for.
//   typing: 4 (=15 chars/s) · OTP digits: 9 · scrolls: 2 (=30 fps of real scroll)
const HOLD = { type: 4, 'type-code': 9, scroll: 2 };
const holdFor = (name) => (name.includes('type-code') ? HOLD['type-code'] : name.includes('scroll') ? HOLD.scroll : HOLD.type);

const marks = {};
await mkdir(UI, { recursive: true }); await mkdir(CLIPS, { recursive: true });
for (const scene of (await readdir(SRC)).sort()) {
  const sdir = path.join(SRC, scene);
  if (!(await stat(sdir)).isDirectory()) continue;
  await mkdir(path.join(UI, scene), { recursive: true });
  for (const f of (await readdir(sdir)).sort()) {
    const p = path.join(sdir, f);
    const st = await stat(p);
    if (st.isDirectory()) {
      const frames = (await readdir(p)).filter((x) => x.endsWith('.png')).sort();
      if (!frames.length) continue;
      const hold = holdFor(f);
      const list = frames.map((fr) => `file '${path.join(p, fr)}'\nduration ${(hold / 60).toFixed(6)}`).join('\n')
        + `\nfile '${path.join(p, frames.at(-1))}'\n`;
      const listFile = path.join(os.tmpdir(), `setu-clip-${scene}-${f}.txt`);
      await writeFile(listFile, list);
      const out = path.join(CLIPS, `${scene}-${f}.mp4`);
      execFileSync(FFMPEG, ['-hide_banner', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', listFile,
        '-vf', 'fps=60,format=yuv420p', '-c:v', 'libx264', '-preset', 'slow', '-crf', '12', '-movflags', '+faststart', out]);
      await rm(listFile, { force: true });
      const secs = (frames.length * hold) / 60;
      marks[`clip:${scene}/${f}`] = { frames: frames.length, hold, seconds: +secs.toFixed(3) };
      console.log(`clip  ${scene}/${f}  ${frames.length} frames x${hold} -> ${secs.toFixed(2)} s`);
    } else if (f.endsWith('.png')) {
      await copyFile(p, path.join(UI, scene, f));
    } else if (f.endsWith('.json')) {
      const j = JSON.parse(await readFile(p, 'utf8'));
      marks[`${scene}/${f.replace(/\.json$/, '')}`] = j.boxes || {};
    }
  }
}
await mkdir(path.join(HF, 'assets/data'), { recursive: true });
await writeFile(path.join(HF, 'assets/data/marks.json'), JSON.stringify(marks, null, 1));
console.log(`marks for ${Object.keys(marks).length} shots/clips -> assets/data/marks.json`);
