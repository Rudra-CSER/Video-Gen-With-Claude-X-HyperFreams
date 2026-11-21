// Representative frames of every scene from the assembled film, for cross-scene review.
//   node tools/montage.mjs [outDir] [fractions]   (default .qc/montage, "0.15,0.4,0.65,0.9")
// Writes <outDir>/raw/frame-*.png (full 1920x1080) and <outDir>/strip-<sceneId>.png
// (the scene's frames side by side at 480 px wide, labelled by film time in the file list).
import { mkdir, readdir, rm, writeFile } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import { HF, loadStoryboard, sceneId, r3 } from './lib-root.mjs';

const out = path.resolve(HF, process.argv[2] || '.qc/montage');
const fr = (process.argv[3] || '0.15,0.4,0.65,0.9').split(',').map(Number);
const { sb } = await loadStoryboard();
const plan = sb.scenes.map((s) => ({ id: sceneId(s), times: fr.map((f) => r3(s.start + f * (s.end - s.start))) }));
const times = plan.flatMap((p) => p.times);
const raw = path.join(out, 'raw');
await rm(out, { recursive: true, force: true });
await mkdir(raw, { recursive: true });
execFileSync(path.join(HF, 'tools/hf-lock.sh'), ['hyperframes', 'snapshot', '.', '--at', times.join(','), '--no-end', '-o', raw],
  { cwd: HF, stdio: ['ignore', 'inherit', 'inherit'] });
const files = (await readdir(raw)).filter((f) => /^frame-\d+-at-.*\.png$/.test(f)).sort();
const ff = process.env.HYPERFRAMES_FFMPEG_PATH || path.join(process.env.HOME, '.local/bin/ffmpeg');
const index = [];
let k = 0;
for (const p of plan) {
  const mine = files.slice(k, k + p.times.length); k += p.times.length;
  if (mine.length !== p.times.length) { console.log(`${p.id}: missing frames`); continue; }
  const dst = path.join(out, `strip-${p.id}.png`);
  const inputs = mine.flatMap((f) => ['-i', path.join(raw, f)]);
  const scale = mine.map((_, i) => `[${i}:v]scale=480:-1[v${i}]`).join(';');
  const stack = `${mine.map((_, i) => `[v${i}]`).join('')}hstack=inputs=${mine.length}`;
  execFileSync(ff, ['-hide_banner', '-loglevel', 'error', '-y', ...inputs, '-filter_complex', `${scale};${stack}`, dst]);
  index.push(`${path.basename(dst)}: film times ${p.times.join(', ')} s -> raw/${mine.join(', raw/')}`);
  console.log(`${path.relative(HF, dst)}  @ ${p.times.join(', ')}`);
}
await writeFile(path.join(out, 'INDEX.txt'), index.join('\n') + '\n');
