// Turn the approved storyboard (storyboard/scene-timing.json) into the written deliverables:
//   storyboard/script.md, storyboard/storyboard.md, captions/narration.txt,
//   captions/subtitles.srt, captions/subtitles.vtt, reports/sound-cue-sheet.md
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';

const VP = path.resolve(new URL('../..', import.meta.url).pathname);
const sb = JSON.parse(await readFile(path.join(VP, 'storyboard/scene-timing.json'), 'utf8'));
const scenes = sb.scenes;

const pad = (n, w = 2) => String(n).padStart(w, '0');
function tc(sec, sep) { // 00:01:02,345
  const ms = Math.round(sec * 1000);
  const h = Math.floor(ms / 3600000); const m = Math.floor((ms % 3600000) / 60000);
  const s = Math.floor((ms % 60000) / 1000); const r = ms % 1000;
  return `${pad(h)}:${pad(m)}:${pad(s)}${sep}${pad(r, 3)}`;
}
const mmss = (sec) => `${Math.floor(sec / 60)}:${pad(Math.floor(sec % 60))}.${pad(Math.round((sec % 1) * 10), 1)}`;
const words = (t) => (t.trim() ? t.trim().split(/\s+/).length : 0);

const caps = scenes.flatMap((s) => s.captions.map((c) => ({ ...c, scene: s.id })));
const total = sb.totalSeconds ?? scenes.at(-1).end;
const wordCount = scenes.reduce((a, s) => a + words(s.narration), 0);

// narration.txt
await mkdir(path.join(VP, 'captions'), { recursive: true });
await writeFile(path.join(VP, 'captions/narration.txt'),
  scenes.map((s) => `[${mmss(s.start)}–${mmss(s.end)}] ${s.title}\n${s.narration.trim()}\n`).join('\n'));

// SRT + VTT (timed to the approved script; no audio exists yet)
const lines = (t) => t.replace(/\s*\n\s*/g, '\n').trim();
await writeFile(path.join(VP, 'captions/subtitles.srt'),
  caps.map((c, i) => `${i + 1}\n${tc(c.start, ',')} --> ${tc(c.end, ',')}\n${lines(c.text)}\n`).join('\n'));
await writeFile(path.join(VP, 'captions/subtitles.vtt'),
  `WEBVTT\n\nNOTE Timed to the approved narration script; no narration audio exists yet. Re-align to audio when it is recorded.\n\n${
    caps.map((c, i) => `${i + 1}\n${tc(c.start, '.')} --> ${tc(c.end, '.')}\n${lines(c.text)}\n`).join('\n')}`);

// script.md
await mkdir(path.join(VP, 'storyboard'), { recursive: true });
await writeFile(path.join(VP, 'storyboard/script.md'), [
  `# ${sb.title} — narration script`, '',
  `Total ${mmss(total)} · ${wordCount} words · delivered as burned-in captions (no voice-over or music in the master).`, '',
  ...scenes.map((s) => `## ${s.id} · ${s.title} (${mmss(s.start)}–${mmss(s.end)})\n\n${s.narration.trim()}\n`),
].join('\n'));

// storyboard.md
const tbl = (rows) => rows.map((r) => `| ${r.join(' | ')} |`).join('\n');
await writeFile(path.join(VP, 'storyboard/storyboard.md'), [
  `# ${sb.title} — storyboard`, '',
  `Angle: ${sb.angle}`, '',
  `1920x1080 · 60 fps · ${mmss(total)} · ${scenes.length} scenes · ${wordCount} narration words · ${caps.length} captions`, '',
  tbl([['Scene', 'Time', 'Title', 'Real UI shown'], ['---', '---', '---', '---'],
    ...scenes.map((s) => [s.id, `${mmss(s.start)}–${mmss(s.end)}`, s.title, s.shots.map((x) => `\`${x.file}\``).join('<br>')])]), '',
  ...scenes.map((s) => [
    `## ${s.id} · ${s.title}`, '',
    `**Time** ${mmss(s.start)} → ${mmss(s.end)} (${(s.end - s.start).toFixed(1)} s)`, '',
    `**Narration** ${s.narration.trim()}`, '',
    `**On-screen text**`, ...s.onScreenText.map((o) => `- ${mmss(o.start)}–${mmss(o.end)} · *${o.role}* · ${o.text}`), '',
    `**UI state** ${s.uiState}`, '',
    `**Shots**`, ...s.shots.map((x) => `- ${mmss(x.start)}–${mmss(x.end)} · \`${x.file}\` · ${x.treatment}`), '',
    `**Animation** ${s.animation}`, '',
    `**Transition in** ${s.transitionIn} · **out** ${s.transitionOut}`, '',
    `**Captions**`, ...s.captions.map((c) => `- ${mmss(c.start)}–${mmss(c.end)} · ${c.text.replace(/\n/g, ' / ')}`), '',
    `**Sound cues (placeholders)**`, ...s.soundCues.map((c) => `- ${mmss(c.at)} · ${c.cue}`), '',
    `**Accuracy notes** ${s.accuracyNotes}`, '',
  ].join('\n')),
].join('\n'));

// sound cue sheet
await mkdir(path.join(VP, 'reports'), { recursive: true });
const cues = scenes.flatMap((s) => s.soundCues.map((c) => ({ ...c, scene: s.id, title: s.title })))
  .sort((a, b) => a.at - b.at);
await writeFile(path.join(VP, 'reports/sound-cue-sheet.md'), [
  '# Sound cue sheet', '',
  'The master is silent by design: no music, effects or voice. These are placement suggestions for the owner\'s soundtrack, timed to picture.', '',
  tbl([['Timecode', 'Scene', 'Cue'], ['---', '---', '---'], ...cues.map((c) => [tc(c.at, '.').slice(3, 11), `${c.scene} ${c.title}`, c.cue])]), '',
  'Scene boundaries (for music edits):', '',
  ...scenes.map((s) => `- ${tc(s.start, '.').slice(3, 11)} ${s.id} ${s.title}`), '',
].join('\n'));

console.log(`docs: ${scenes.length} scenes, ${caps.length} captions, ${wordCount} words, ${total}s`);
