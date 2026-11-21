// Asset manifest: every file the film uses, where it came from, how it is used and
// which scenes use it. Written from the storyboard plus what is on disk.
//   node tools/build-manifest.mjs   -> ../reports/asset-manifest.md and ../reports/asset-manifest.json
import { readFile, writeFile, readdir, stat, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { HF, VP, loadStoryboard, sceneId } from './lib-root.mjs';

const { sb } = await loadStoryboard();
const marks = JSON.parse(await readFile(path.join(HF, 'assets/data/marks.json'), 'utf8'));
const kb = async (p) => { try { return Math.round((await stat(p)).size / 1024); } catch { return null; } };
const exists = async (p) => { try { await stat(p); return true; } catch { return false; } };

const uses = new Map(); // key -> { kind, src, scenes:Set, treatments:[] }
const add = (key, o, scene, treatment) => {
  if (!uses.has(key)) uses.set(key, { ...o, scenes: new Set(), treatments: [] });
  const u = uses.get(key); u.scenes.add(scene); if (treatment) u.treatments.push(`${scene}: ${treatment}`);
};
for (const s of sb.scenes) {
  const id = sceneId(s);
  for (const x of s.shots) {
    const f = x.file.replace(/^(assets\/screens\/|assets\/ui\/)/, '');
    if (/^graphic:|^MOTION GRAPHIC/i.test(f)) { add(`graphic:${f.replace(/^graphic:\s*/i, '')}`, { kind: 'motion graphic (built in HTML/CSS/SVG, not an app screen)' }, id, null); continue; }
    if (f.endsWith('/')) {
      const [g, seq] = f.replace(/\/$/, '').split('/');
      const base = `assets/clips/${g}-${seq}.mp4`;
      const variant = x.clipSeconds ? `assets/clips/${g}-${seq}.${Math.round(x.clipSeconds * 1000)}ms.mp4` : null;
      add(`clip:${g}/${seq}`, { kind: 'real capture: typing/scroll frame sequence encoded as 60 fps clip', src: variant || base, base,
        source: `assets/screens/${g}/${seq}/ (${marks[`clip:${g}/${seq}`]?.frames ?? '?'} captured frames)` }, id, x.treatment);
      continue;
    }
    add(f, { kind: f.startsWith('desktop/') ? 'real capture: desktop web page (1440x900 CSS at 2x)' : 'real capture: phone screen (390x844 CSS at 3x)',
      src: `assets/ui/${f}`, source: `assets/screens/${f}` }, id, x.treatment);
  }
}
// Shared assets every scene relies on.
const shared = [
  ['assets/brand/setu-logo.png', 'official SETU lockup (shown on a white rounded tile, never recoloured)'],
  ['assets/brand/setu-mark.svg', "the app's vector mark"],
  ['assets/data/campus-boundary.json', 'IIT Kharagpur campus boundary polygon from server/src/config/campus-zone.js (78 points), drawn as SVG'],
  ['assets/data/marks.json', 'CSS-px boxes of UI elements per capture (for taps, rings, camera framing)'],
  ['assets/fonts/Sora-Variable.ttf', "the app's display font (OFL, licence alongside)"],
  ['assets/fonts/PlusJakartaSans-Variable.ttf', "the app's UI font (OFL)"],
  ['assets/fonts/SpaceMono-Regular.ttf', "the app's data font (OFL)"],
  ['assets/fonts/SpaceMono-Bold.ttf', "the app's data font, bold (OFL)"],
  ['assets/vendor/gsap.min.js', 'GSAP 3.13.0 (animation engine; standard GSAP licence)'],
  ['assets/css/kit.css', 'shared visual kit: tokens, phone frame, overlays, captions'],
  ['assets/js/kit.js', 'shared motion helpers (window.SetuKit)'],
];
const rows = [];
for (const [k, u] of [...uses.entries()].sort()) {
  const p = u.src ? path.join(HF, u.src) : null;
  rows.push({ key: k, kind: u.kind, file: u.src || '(built in the scene)', source: u.source || '', sizeKB: p ? await kb(p) : null,
    present: p ? await exists(p) : true, scenes: [...u.scenes], treatments: u.treatments });
}
const sharedRows = [];
for (const [f, what] of shared) sharedRows.push({ file: f, what, sizeKB: await kb(path.join(HF, f)), present: await exists(path.join(HF, f)) });
const compositions = [];
for (const s of sb.scenes) {
  const f = `compositions/${sceneId(s)}.html`;
  compositions.push({ scene: s.id, file: f, start: s.start, end: s.end, title: s.title, present: await exists(path.join(HF, f)) });
}
const unusedUi = [];
for (const g of (await readdir(path.join(HF, 'assets/ui'))).sort()) {
  for (const f of (await readdir(path.join(HF, 'assets/ui', g))).sort()) {
    if (!uses.has(`${g}/${f}`)) unusedUi.push(`${g}/${f}`);
  }
}
await mkdir(path.join(VP, 'reports'), { recursive: true });
await writeFile(path.join(VP, 'reports/asset-manifest.json'), JSON.stringify({ title: sb.title, totalSeconds: sb.totalSeconds, compositions, assets: rows, shared: sharedRows, capturedButUnused: unusedUi }, null, 1));
const t = (r) => `| ${r.join(' | ')} |`;
const md = [
  '# Asset manifest', '',
  `Film: ${sb.title} · ${sb.totalSeconds} s · 1920x1080 · 60 fps. Paths are relative to \`video-production/hyperframes/\` unless they start with \`assets/screens/\` (relative to \`video-production/\`).`, '',
  'Every app screen in the film is a real capture of the app, recorded with Playwright on an isolated demo copy (demo stalls, a demo persona and a labelled demo payment QR). Motion graphics are drawn in HTML/CSS/SVG inside the compositions.', '',
  '## Scene compositions', '',
  t(['Scene', 'File', 'Time', 'Title', 'Present']), t(['---', '---', '---', '---', '---']),
  ...compositions.map((c) => t([c.scene, `\`${c.file}\``, `${c.start}–${c.end} s`, c.title, c.present ? 'yes' : 'MISSING'])), '',
  '## Media used by the storyboard', '',
  t(['Asset', 'Kind', 'File', 'Source', 'KB', 'Scenes']), t(['---', '---', '---', '---', '---', '---']),
  ...rows.map((r) => t([`\`${r.key}\``, r.kind, r.file === '(built in the scene)' ? r.file : `\`${r.file}\``, r.source ? `\`${r.source}\`` : '', r.sizeKB ?? '', r.scenes.join(', ') + (r.present ? '' : ' · MISSING')])), '',
  '## Shared assets', '',
  t(['File', 'What it is', 'KB']), t(['---', '---', '---']),
  ...sharedRows.map((r) => t([`\`${r.file}\``, r.what, r.sizeKB ?? 'MISSING'])), '',
  '## Captured but not used in this cut', '',
  unusedUi.length ? unusedUi.map((u) => `- \`assets/ui/${u}\``).join('\n') : '- none', '',
].join('\n');
await writeFile(path.join(VP, 'reports/asset-manifest.md'), md);
// Asset checklist: per scene, every asset it needs, whether it exists, and how it is used.
const chk = ['# Asset checklist', '',
  'Generated from storyboard/scene-timing.json. ✔ = present on disk. "Real capture" = a genuine screen of the app recorded on the isolated demo copy; "motion graphic" = drawn in the scene (type, shapes, the real campus boundary, the official logo).', ''];
for (const s of sb.scenes) {
  const id = sceneId(s);
  const comp = compositions.find((c) => c.scene === s.id);
  chk.push(`## ${s.id} · ${s.title} (${s.start}–${s.end} s)`, '', `- ${comp?.present ? '✔' : '✘'} composition \`hyperframes/${comp?.file}\``);
  for (const x of s.shots) {
    const f = x.file.replace(/^(assets\/screens\/|assets\/ui\/)/, '');
    if (/^graphic:|^MOTION GRAPHIC/i.test(f)) { chk.push(`- ✔ motion graphic: ${f.replace(/^graphic:\s*/i, '')}`); continue; }
    if (f.endsWith('/')) {
      const [g, seq] = f.replace(/\/$/, '').split('/');
      const src = x.clipSeconds ? `assets/clips/${g}-${seq}.${Math.round(x.clipSeconds * 1000)}ms.mp4` : `assets/clips/${g}-${seq}.mp4`;
      chk.push(`- ${(await exists(path.join(HF, src))) ? '✔' : '✘'} real capture (typing/scroll clip): \`${src}\`${x.clipSeconds ? ` (re-timed to ${x.clipSeconds} s)` : ''}`);
      continue;
    }
    const src = `assets/ui/${f}`;
    chk.push(`- ${(await exists(path.join(HF, src))) ? '✔' : '✘'} real capture: \`${src}\``);
  }
  if ((s.demoBadge || []).length) chk.push(`- ✔ "Demo environment" badge: ${s.demoBadge.map((d) => `${d.start}–${d.end} s`).join(', ')}`);
  chk.push('');
}
chk.push('## Shared', '', ...sharedRows.map((r) => `- ${r.present ? '✔' : '✘'} \`hyperframes/${r.file}\` — ${r.what}`), '');
await writeFile(path.join(VP, 'reports/asset-checklist.md'), chk.join('\n'));
console.log(`manifest: ${rows.length} media assets, ${sharedRows.length} shared, ${compositions.length} compositions, ${unusedUi.length} unused captures`);
