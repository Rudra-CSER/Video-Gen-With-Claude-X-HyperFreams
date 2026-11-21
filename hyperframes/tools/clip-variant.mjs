// Re-time a typing / scrolling clip to an exact playback length (HyperFrames has no
// playback-rate attribute, so speed changes are baked into a variant file).
//   node tools/clip-variant.mjs <group>/<seq> <seconds>    -> assets/clips/<group>-<seq>.<ms>ms.mp4
//   node tools/clip-variant.mjs --from-storyboard          -> every shot with "clipSeconds"
// The source is the captured frame sequence in ../assets/screens/<group>/<seq>/*.png;
// every captured frame is shown for the same share of the new length (60 fps output).
import { readdir, readFile, writeFile, rm, access } from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
import os from 'node:os';

const HF = path.resolve(new URL('..', import.meta.url).pathname);
const VP = path.resolve(HF, '..');
const FFMPEG = process.env.HYPERFRAMES_FFMPEG_PATH || path.join(os.homedir(), '.local/bin/ffmpeg');

export const variantSrc = (seqPath, seconds) => {
  const [g, seq] = seqPath.replace(/^\/+|\/+$/g, '').split('/');
  return `assets/clips/${g}-${seq}.${Math.round(seconds * 1000)}ms.mp4`;
};

async function make(seqPath, seconds) {
  const [g, seq] = seqPath.replace(/^\/+|\/+$/g, '').split('/');
  const dir = path.join(VP, 'assets/screens', g, seq);
  const frames = (await readdir(dir)).filter((f) => f.endsWith('.png')).sort();
  if (!frames.length) throw new Error(`no frames in ${dir}`);
  const out = path.join(HF, variantSrc(seqPath, seconds));
  try { await access(out); return { out, cached: true }; } catch { /* build it */ }
  const per = seconds / frames.length;
  const list = frames.map((f) => `file '${path.join(dir, f)}'\nduration ${per.toFixed(6)}`).join('\n')
    + `\nfile '${path.join(dir, frames.at(-1))}'\n`;
  const listFile = path.join(os.tmpdir(), `setu-variant-${g}-${seq}-${Math.round(seconds * 1000)}.txt`);
  await writeFile(listFile, list);
  execFileSync(FFMPEG, ['-hide_banner', '-loglevel', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', listFile,
    '-vf', 'fps=60,format=yuv420p', '-t', seconds.toFixed(3), '-c:v', 'libx264', '-preset', 'slow', '-crf', '12',
    '-movflags', '+faststart', out]);
  await rm(listFile, { force: true });
  return { out, cached: false };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const a = process.argv.slice(2);
  const jobs = [];
  if (a[0] === '--from-storyboard') {
    const sb = JSON.parse(await readFile(path.join(VP, 'storyboard/scene-timing.json'), 'utf8'));
    for (const s of sb.scenes) for (const x of s.shots) {
      if (x.file.endsWith('/') && x.clipSeconds) jobs.push([x.file.replace(/^assets\/screens\//, ''), +x.clipSeconds]);
    }
  } else if (a.length === 2) jobs.push([a[0], +a[1]]);
  else { console.error('usage: node tools/clip-variant.mjs <group>/<seq> <seconds> | --from-storyboard'); process.exit(2); }
  for (const [p, secs] of jobs) {
    const r = await make(p, secs);
    console.log(`${r.cached ? 'kept ' : 'made '} ${path.relative(HF, r.out)}  (${secs.toFixed(3)} s)`);
  }
}
