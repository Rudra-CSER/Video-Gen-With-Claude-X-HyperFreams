// Generate the root orchestrator (index.html) and the burned-in caption track
// (compositions/captions.html) from the approved storyboard.
//   node tools/build-root.mjs [--no-captions]
import { writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { HF, loadStoryboard, sceneId, rootHtml, slotHtml, captionsHtml } from './lib-root.mjs';

export { sceneId };
const { sb, layout, boundary, total } = await loadStoryboard();
const withCaptions = !process.argv.includes('--no-captions');

const slotsHtml = sb.scenes.map((s) => slotHtml(sceneId(s), s.start, s.end - s.start)).join('\n');
await writeFile(path.join(HF, 'index.html'),
  rootHtml({ title: sb.title || 'SETU Food walkthrough', total, slotsHtml, captions: withCaptions, boundary }));

const centerScenes = new Set(layout.captionCenter || []);
const caps = sb.scenes.flatMap((s) => s.captions.map((c) => ({ ...c, center: centerScenes.has(s.id) })));
await mkdir(path.join(HF, 'compositions'), { recursive: true });
if (withCaptions) await writeFile(path.join(HF, 'compositions/captions.html'), captionsHtml(caps));
console.log(`index.html: ${sb.scenes.length} scene slots, ${total}s${withCaptions ? `; captions.html: ${caps.length} captions` : ''}`);
console.log(sb.scenes.map((s) => `  ${sceneId(s)}  ${s.start}-${s.end}`).join('\n'));
