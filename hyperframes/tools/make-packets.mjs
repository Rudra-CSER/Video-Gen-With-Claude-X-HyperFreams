// One build packet per scene for the scene builders: the scene's storyboard block with
// scene-local times, the marks of every real capture it uses, clip lengths, the boundary
// handoff contracts, and the neighbouring scenes' edges so cuts line up.
//   node tools/make-packets.mjs
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';

const HF = path.resolve(new URL('..', import.meta.url).pathname);
const VP = path.resolve(HF, '..');
const sb = JSON.parse(await readFile(path.join(VP, 'storyboard/scene-timing.json'), 'utf8'));
const marks = JSON.parse(await readFile(path.join(HF, 'assets/data/marks.json'), 'utf8'));
const layout = JSON.parse(await readFile(path.join(VP, 'storyboard/layout.json'), 'utf8').catch(() => '{}'));
const slug = (s) => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 28);
const sceneId = (s) => `s${String(s.id).replace(/\D/g, '').padStart(2, '0')}-${slug(s.compositionName || s.title)}`;
const r3 = (n) => +(+n).toFixed(3);
const variantSrc = (g, seq, seconds) => `assets/clips/${g}-${seq}.${Math.round(seconds * 1000)}ms.mp4`;

function assetFor(shot) {
  const file = shot.file;
  if (/^graphic:/i.test(file) || /^MOTION GRAPHIC/i.test(file)) return { kind: 'graphic', description: file.replace(/^graphic:\s*/i, '') };
  const f = file.replace(/^(assets\/screens\/|assets\/ui\/)/, '').replace(/^\/+/, '');
  if (/^(brand|data)\//.test(f)) return { kind: 'graphic', file: f, src: `assets/${f}` };
  if (f.startsWith('demo/')) return { kind: 'graphic', file: f, src: null, note: 'Not served by the HyperFrames project: show the demo QR only through the order-qr captures.' };
  if (f.endsWith('/')) {
    const [g, seq] = f.replace(/\/$/, '').split('/');
    const info = marks[`clip:${g}/${seq}`] || null;
    const seconds = shot.clipSeconds ? +shot.clipSeconds : info?.seconds;
    return {
      kind: 'clip', file: f,
      src: shot.clipSeconds ? variantSrc(g, seq, +shot.clipSeconds) : `assets/clips/${g}-${seq}.mp4`,
      baseSrc: `assets/clips/${g}-${seq}.mp4`,
      seconds: seconds != null ? r3(seconds) : null,
      info,
      note: 'Play it in a non-timed .layer inside the phone screen; put the matching still under it to hold the last frame.',
    };
  }
  if (f.endsWith('.png') && f.includes('/')) {
    const key = f.replace(/\.png$/, '');
    const isDesktop = f.startsWith('desktop/');
    return { kind: isDesktop ? 'desktop-still' : 'still', file: f, src: `assets/ui/${f}`, marks: marks[key] || null,
      size: isDesktop ? '1440x900 CSS px (2x PNG)' : '390x844 CSS px (3x PNG)' };
  }
  return { kind: 'graphic', file: f };
}

await mkdir(path.join(HF, '.packets'), { recursive: true });
const scenes = sb.scenes;
for (let i = 0; i < scenes.length; i++) {
  const s = scenes[i]; const id = sceneId(s); const t0 = s.start;
  const local = (x) => r3(x - t0);
  const packet = {
    sceneId: id,
    file: `compositions/${id}.html`,
    duration: r3(s.end - s.start),
    globalStart: r3(s.start),
    globalEnd: r3(s.end),
    title: s.title,
    chapter: s.chapter ?? null,
    phoneSpec: sb.phoneSpec || { left: 1150, top: 70, k: 1.08 },
    captionPlacement: (layout.captionCenter || []).includes(s.id) ? 'center (keep y 880-1050 clear across the whole width)' : 'left (keep x 120-1140, y 880-1050 clear)',
    narration: s.narration,
    captionsLocal: s.captions.map((c) => ({ start: local(c.start), end: local(c.end), text: c.text })),
    onScreenText: s.onScreenText.map((o) => ({ ...o, start: local(o.start), end: local(o.end) })),
    shots: s.shots.map((x) => ({ ...x, start: local(x.start), end: local(x.end), asset: assetFor(x) })),
    demoBadgeLocal: (s.demoBadge || []).map((d) => ({ start: local(d.start), end: local(d.end) })),
    uiState: s.uiState,
    animationLocal: s.animation,
    transitionIn: s.transitionIn,
    transitionOut: s.transitionOut,
    handoffIn: s.handoffIn ?? null,
    handoffOut: s.handoffOut ?? null,
    soundCuesLocal: s.soundCues.map((c) => ({ at: local(c.at), cue: c.cue })),
    accuracyNotes: s.accuracyNotes,
    globalSystem: sb.angle,
    previousScene: i > 0 ? { id: sceneId(scenes[i - 1]), title: scenes[i - 1].title, transitionOut: scenes[i - 1].transitionOut,
      handoffOut: scenes[i - 1].handoffOut ?? null, lastShots: scenes[i - 1].shots.slice(-2).map((x) => x.file) } : null,
    nextScene: i < scenes.length - 1 ? { id: sceneId(scenes[i + 1]), title: scenes[i + 1].title, transitionIn: scenes[i + 1].transitionIn,
      handoffIn: scenes[i + 1].handoffIn ?? null, firstShots: scenes[i + 1].shots.slice(0, 2).map((x) => x.file) } : null,
  };
  await writeFile(path.join(HF, '.packets', `${id}.json`), JSON.stringify(packet, null, 2));
  const missing = packet.shots.filter((x) => (x.asset.kind === 'still' && !x.asset.marks) || (x.asset.kind === 'clip' && !x.asset.info));
  console.log(`${id}  ${packet.duration}s  shots ${packet.shots.length}${missing.length ? `  MISSING: ${missing.map((m) => m.file).join(', ')}` : ''}`);
}
