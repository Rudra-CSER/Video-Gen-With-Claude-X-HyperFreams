// Make a stand-alone preview project for ONE scene, so a builder can lint, check and
// snapshot it without the rest of the film. The preview looks exactly like the film at
// that moment: same background state, the scene at local time 0, and its own captions.
//   node tools/preview-scene.mjs s05            (or the full id, e.g. s05-where-orders-arrive)
//   -> .preview/<sceneId>/  (index.html, compositions/, assets -> ../../assets)
// Then, for example:
//   tools/hf-lock.sh hyperframes lint .preview/<sceneId>
//   tools/hf-lock.sh hyperframes snapshot .preview/<sceneId> --at 0.5,2,4.2 -o .preview/<sceneId>/snaps
import { mkdir, writeFile, symlink, rm, lstat } from 'node:fs/promises';
import path from 'node:path';
import { HF, loadStoryboard, sceneId, rootHtml, slotHtml, captionsHtml, r3 } from './lib-root.mjs';

const want = process.argv[2];
if (!want) { console.error('usage: node tools/preview-scene.mjs <sNN | full scene id>'); process.exit(2); }
const { sb, layout, boundary, total } = await loadStoryboard();
const scene = sb.scenes.find((s) => sceneId(s) === want || s.id === want || sceneId(s).startsWith(`${want}-`));
if (!scene) { console.error(`no scene ${want}; have ${sb.scenes.map(sceneId).join(', ')}`); process.exit(2); }

const id = sceneId(scene);
const dur = r3(scene.end - scene.start);
const dir = path.join(HF, '.preview', id);
// Replace only the generated project files; keep snapshots and notes already in the folder.
await rm(path.join(dir, 'compositions'), { recursive: true, force: true });
await rm(path.join(dir, 'index.html'), { force: true });
await mkdir(path.join(dir, 'compositions'), { recursive: true });
const link = async (target, at) => {
  try { await lstat(at); await rm(at, { force: true }); } catch { /* new */ }
  await symlink(target, at);
};
await link(path.join(HF, 'assets'), path.join(dir, 'assets'));
await link(path.join(HF, 'compositions', `${id}.html`), path.join(dir, 'compositions', `${id}.html`));

const center = (layout.captionCenter || []).includes(scene.id);
const caps = scene.captions.map((c) => ({ ...c, center }));
await writeFile(path.join(dir, 'compositions/captions.html'), captionsHtml(caps, scene.start));
await writeFile(path.join(dir, 'index.html'), rootHtml({
  title: `Preview ${id}`, total: dur, slotsHtml: slotHtml(id, 0, dur), captions: true, boundary,
  filmTotal: total, windowStart: scene.start,
}));
console.log(`${path.relative(HF, dir)}  (${dur} s, film ${scene.start}-${scene.end})`);
