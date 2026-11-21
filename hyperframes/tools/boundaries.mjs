// Snapshot the assembled film on both sides of every scene cut and pair the frames,
// so a reviewer can see whether each hard cut is invisible (or designed).
//   node tools/boundaries.mjs [outDir]      (default .qc/boundaries)
// Writes <outDir>/cut-NN-<from>-to-<to>.png: left = last frame of scene N, right = first frame of N+1.
import { mkdir, readdir, rm } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { HF, loadStoryboard, sceneId, r3 } from './lib-root.mjs';

const out = path.resolve(HF, process.argv[2] || '.qc/boundaries');
const { sb } = await loadStoryboard();
const FRAME = 1 / 60;
const cuts = sb.scenes.slice(0, -1).map((s, i) => ({ i, from: sceneId(s), to: sceneId(sb.scenes[i + 1]), t: r3(s.end) }));
const times = cuts.flatMap((c) => [r3(c.t - FRAME), c.t]);
const raw = path.join(out, 'raw');
await rm(out, { recursive: true, force: true });
await mkdir(raw, { recursive: true });
execFileSync(path.join(HF, 'tools/hf-lock.sh'), ['hyperframes', 'snapshot', '.', '--at', times.join(','), '--no-end', '-o', raw],
  { cwd: HF, stdio: ['ignore', 'inherit', 'inherit'] });
const files = (await readdir(raw)).filter((f) => /^frame-\d+-at-.*\.png$/.test(f)).sort();
const ff = process.env.HYPERFRAMES_FFMPEG_PATH || path.join(process.env.HOME, '.local/bin/ffmpeg');
for (const c of cuts) {
  const a = files[c.i * 2]; const b = files[c.i * 2 + 1];
  if (!a || !b) { console.log(`cut ${c.i + 1}: missing frames`); continue; }
  const dst = path.join(out, `cut-${String(c.i + 1).padStart(2, '0')}-${c.from}-to-${c.to}.png`);
  execFileSync(ff, ['-hide_banner', '-loglevel', 'error', '-y', '-i', path.join(raw, a), '-i', path.join(raw, b),
    '-filter_complex', '[0:v]scale=960:-1[l];[1:v]scale=960:-1[r];[l][r]hstack=inputs=2', dst]);
  console.log(`${path.relative(HF, dst)}   t=${c.t}s`);
}
