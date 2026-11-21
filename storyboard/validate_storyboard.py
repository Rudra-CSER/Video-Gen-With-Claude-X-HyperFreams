#!/usr/bin/env python3
"""Validate storyboard/scene-timing.json (and layout.json) against the storyboard contract.

    python3 storyboard/validate_storyboard.py [path/to/scene-timing.json]

Prints every problem found and exits 1 if there is at least one; prints "OK: no problems" and exits 0
otherwise. Lines starting with "info:" are notes, not problems.

Checks
- root fields, phoneSpec, scene ids (s01.. contiguous), compositionName, required scene fields;
- scenes tile 0..totalSeconds with no gaps or overlaps; total inside 105-120 s (info if outside 110-114 s);
- captions: <=2 lines, <=42 characters per line, >=1.3 s, <=2.6 words/s, no overlaps, inside their scene;
- narration == the scene's captions joined; wordCount == total narration words, inside 200-240;
- shots: real captures exist (hyperframes/assets/ui/<group>/<shot>.png, desktop too), clip dirs exist
  (assets/screens/<group>/<seq>/ with frames) with a known "clip:" base length, clipSeconds inside
  0.75x-2.5x of it, the clip's shot window matches its playback length, "graphic:" otherwise; inside the scene;
- onScreenText, sound cues and DEMO-badge windows inside their scene; rupee-sign strings never set in
  Sora or as a headline (and their role names Plus Jakarta Sans or Space Mono);
- at most 4 floating labels / chips / tags on screen at once per scene;
- handoffOut(N) == handoffIn(N+1) field for field, and each handoff is well formed;
- "<group>/<shot>.<mark>" references in the animation text exist in marks.json; animation starts "Local times.";
- the end card has the verbatim disclaimer, tagline and CTA (the emailed one-time code is a released sign-in
  method, so its scene no longer needs a DEMO badge; demo data stays labelled on the end card);
- forbidden phrases are absent from narration, captions and on-screen text (including "customer": the app
  calls them users);
- director's addendum A: the scene with the TONIGHT tag shows the saved-Home pick (location/30-home-unset →
  31-picker-saved → 32-confirm-saved → 33-home-set, in order) with taps on deliverTo, homeRow and confirm;
- director's addendum B: total <= 119.5 s; the end card lasts 8.0 s and its disclaimer is fully legible >= 6 s;
- captions are at least 0.1 s apart;
- each scene's kicker shows its chapter and has faded out at least 0.05 s before the scene's last frame;
- handoffIn.screen is a still that starts at the scene start, handoffOut.screen a still that ends at the scene end;
- app shots (stills and clips) inside a scene leave no uncovered gap between them.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VP = os.path.dirname(HERE)                                  # video-production/
HF = os.path.join(VP, 'hyperframes')
UI = os.path.join(HF, 'assets', 'ui')
SCREENS = os.path.join(VP, 'assets', 'screens')
MARKS = os.path.join(HF, 'assets', 'data', 'marks.json')

DISCLAIMER = ('SETU connects users with approved campus food providers. Food preparation, delivery and payment are '
              'handled by the respective provider. SETU does not collect payments or independently guarantee food hygiene.')
TAGLINE = 'Your campus. Your food. Your SETU.'
CTA = 'Explore SETU Food'

MAX_LINE, MAX_LINES, MIN_DUR, MAX_WPS = 42, 2, 1.3, 2.6
MIN_CAPTION_GAP = 0.1
MAX_TOTAL = 119.5            # director's addendum B (QC fails above 120 s)
END_CARD_SECONDS = 8.0       # director's addendum B
MIN_DISCLAIMER_LEGIBLE = 6.0
KICKER_CLEAR = 0.05          # the kicker's fade-out ends at least this long before the scene's last frame
SAVED_HOME = ['location/30-home-unset.png', 'location/31-picker-saved.png', 'location/32-confirm-saved.png', 'location/33-home-set.png']
SAVED_HOME_TAPS = [('location/30-home-unset.deliverTo', 'K.tap deliverTo'), ('location/31-picker-saved.homeRow', 'K.tap homeRow'),
                   ('location/32-confirm-saved.confirm', 'K.tap confirm')]
EPS = 1e-6

NUM = r'(?:\d+|one|two|three|four|five|ten|fifteen|twenty|thirty|forty|forty-five|sixty)'
FORBIDDEN = [
    (r'\bSETU\s+deliver', '"SETU delivers" (the stall delivers)'),
    (r'\bpick[\s-]?up\b', 'pickup (no pickup option exists)'),
    (r'\briders?\b', 'rider (no rider / map tracking)'),
    (r'\bGPS\b', 'GPS (no GPS tracking; say "location access")'),
    (r'\b(live|real[\s-]?time)\s+(tracking|map)\b', 'live tracking / live map'),
    (r'\btrack(ing)?\s+(on|with)\s+(a|the)\s+map\b', 'map tracking'),
    (r'\bfree\b', '"free"'),
    (r'\bzero[\s-]?cost\b', '"zero cost"'),
    (r'\bminimal\b', '"minimal" (charges)'),
    (r'\bguarantee', 'a hygiene / quality guarantee (only the verbatim disclaimer may use the word)'),
    (r'\b(swiggy|zomato|higi|tomato|zepto|blinkit|dunzo|uber\s*eats)\b', 'competitor name (real or disguised)'),
    (r'\b(deliver\w*|arriv\w*|reach\w*|at your door)\b[^.]{0,40}?\b(in|within|under)\s+' + NUM + r'\s*-?\s*(min|mins|minute|minutes)\b',
     'delivery-time promise'),
    (r'\b(in|within|under)\s+' + NUM + r'\s*-?\s*(min|mins|minute|minutes)\b[^.]{0,40}?\b(deliver\w*|arriv\w*|at your door)\b',
     'delivery-time promise'),
    (r'\b' + NUM + r'[\s-]*(min|mins|minute|minutes)\s+deliver', 'delivery-time promise'),
    (r'\bpay\s+first\b', '"pay first" (the stall accepts first)'),
    (r'\bQR\s+at\s+checkout\b', '"QR at checkout" (the QR appears after acceptance)'),
    (r'\bsetu\s+(collects?|takes?)\s+(your\s+)?(money|payment)', 'SETU collecting money'),
    (r'\bcustomers?\b', '"customer" (the app now says "user": a User account)'),
]
FLOATING_ROLE = re.compile(r'^(label|tag|dish chip|order-slip|demo|honesty note|persona chip|DEMO badge|number flight)', re.I)


def words(text):
    return len(text.split())


def is_num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'scene-timing.json')
    problems, infos = [], []

    def bad(msg):
        problems.append(msg)

    try:
        sb = json.load(open(path, encoding='utf-8'))
    except Exception as exc:  # noqa: BLE001
        print(f'cannot read {path}: {exc}')
        return 1
    marks = json.load(open(MARKS, encoding='utf-8'))

    # ---------------------------------------------------------------- root
    for key, typ in (('title', str), ('angle', str), ('totalSeconds', (int, float)), ('wordCount', int),
                     ('phoneSpec', dict), ('scenes', list)):
        if not isinstance(sb.get(key), typ):
            bad(f'root: "{key}" missing or not {typ}')
    if sb.get('phoneSpec') != {'left': 1150, 'top': 70, 'k': 1.08}:
        bad(f'root: phoneSpec must be {{left:1150, top:70, k:1.08}} (got {sb.get("phoneSpec")})')
    scenes = sb.get('scenes') or []
    total = sb.get('totalSeconds', 0)

    # ---------------------------------------------------------------- layout.json
    layout_path = os.path.join(os.path.dirname(path), 'layout.json')
    if os.path.exists(layout_path):
        layout = json.load(open(layout_path, encoding='utf-8'))
        ids = {s.get('id') for s in scenes}
        for sid in layout.get('captionCenter', []):
            if sid not in ids:
                bad(f'layout.json: captionCenter lists unknown scene {sid}')
        if not isinstance(layout.get('notes'), str):
            bad('layout.json: "notes" missing')
    else:
        bad('layout.json missing next to scene-timing.json')

    # ---------------------------------------------------------------- scenes, ids, tiling
    if len(scenes) != 12:
        bad(f'expected 12 scenes, found {len(scenes)}')
    required = ['id', 'compositionName', 'title', 'chapter', 'start', 'end', 'narration', 'captions', 'onScreenText', 'shots',
                'uiState', 'animation', 'transitionIn', 'transitionOut', 'handoffIn', 'handoffOut', 'demoBadge', 'soundCues',
                'accuracyNotes']
    names = set()
    prev_end = 0.0
    for i, s in enumerate(scenes):
        sid = s.get('id', f'#{i}')
        for k in required:
            if k not in s:
                bad(f'{sid}: missing field "{k}"')
        if sid != f's{i + 1:02d}':
            bad(f'{sid}: ids must be contiguous s01..s{len(scenes):02d} (expected s{i + 1:02d})')
        cn = s.get('compositionName', '')
        if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', cn or '') or len(cn) > 24:
            bad(f'{sid}: compositionName "{cn}" must be a kebab slug of at most 24 characters')
        if cn in names:
            bad(f'{sid}: duplicate compositionName "{cn}"')
        names.add(cn)
        if s.get('chapter') is not None and not isinstance(s.get('chapter'), str):
            bad(f'{sid}: chapter must be a string or null')
        st, en = s.get('start'), s.get('end')
        if not (is_num(st) and is_num(en)) or en <= st:
            bad(f'{sid}: bad start/end {st}..{en}')
            continue
        if abs(st - prev_end) > EPS:
            bad(f'{sid}: starts at {st} but the previous scene ends at {prev_end} (gap/overlap)')
        prev_end = en
        if not str(s.get('animation', '')).startswith('Local times.'):
            bad(f'{sid}: animation must start with "Local times."')
    if scenes and abs(scenes[0].get('start', 0)) > EPS:
        bad('the first scene must start at 0')
    if scenes and abs(prev_end - total) > EPS:
        bad(f'the last scene ends at {prev_end} but totalSeconds is {total}')
    if not 105 <= total <= 120:
        bad(f'totalSeconds {total} is outside the acceptable 105-120 s')
    elif not 110 <= total <= 114:
        infos.append(f'info: totalSeconds {total} is inside the acceptable 105-120 s but outside the 110-114 s target')

    def inside(sid, s, a, b, what):
        if not (is_num(a) and is_num(b)) or b < a:
            bad(f'{sid}: {what} has bad times {a}..{b}')
        elif a < s['start'] - EPS or b > s['end'] + EPS:
            bad(f'{sid}: {what} {a}..{b} is outside the scene {s["start"]}..{s["end"]}')

    # ---------------------------------------------------------------- captions + narration
    all_caps = []
    total_words = 0
    for s in scenes:
        sid = s.get('id')
        caps = s.get('captions', [])
        for c in caps:
            a, b, t = c.get('start'), c.get('end'), c.get('text', '')
            inside(sid, s, a, b, f'caption "{t[:30]}"')
            lines = t.split('\n')
            if len(lines) > MAX_LINES:
                bad(f'{sid}: caption "{t[:30]}" has {len(lines)} lines (max {MAX_LINES})')
            for ln in lines:
                if len(ln) > MAX_LINE:
                    bad(f'{sid}: caption line "{ln}" is {len(ln)} characters (max {MAX_LINE})')
                if ln != ln.strip() or not ln:
                    bad(f'{sid}: caption line "{ln}" has stray whitespace or is empty')
            if is_num(a) and is_num(b):
                dur = b - a
                if dur < MIN_DUR - EPS:
                    bad(f'{sid}: caption "{t[:30]}" lasts {dur:.2f} s (min {MIN_DUR})')
                if dur > 0 and words(t) / dur > MAX_WPS + EPS:
                    bad(f'{sid}: caption "{t[:30]}" runs {words(t) / dur:.2f} words/s (max {MAX_WPS})')
                all_caps.append((a, b, sid, t))
        joined = ' '.join(c.get('text', '').replace('\n', ' ') for c in caps)
        if ' '.join(joined.split()) != ' '.join(s.get('narration', '').split()):
            bad(f'{sid}: narration does not match the captions joined')
        total_words += words(s.get('narration', ''))
    all_caps.sort()
    for (a1, b1, s1, t1), (a2, b2, s2, t2) in zip(all_caps, all_caps[1:]):
        if a2 < b1 - EPS:
            bad(f'captions overlap: {s1} "{t1[:25]}" ({a1}-{b1}) and {s2} "{t2[:25]}" ({a2}-{b2})')
        elif a2 - b1 < MIN_CAPTION_GAP - EPS:
            bad(f'captions closer than {MIN_CAPTION_GAP} s: {s1} "{t1[:25]}" ends {b1}, {s2} "{t2[:25]}" starts {a2}')
    if total_words != sb.get('wordCount'):
        bad(f'wordCount is {sb.get("wordCount")} but the narration has {total_words} words')
    if not 200 <= total_words <= 240:
        bad(f'narration has {total_words} words (expected about 200-240)')

    # ---------------------------------------------------------------- shots
    for s in scenes:
        sid = s.get('id')
        for sh in s.get('shots', []):
            f = sh.get('file', '')
            inside(sid, s, sh.get('start'), sh.get('end'), f'shot {f}')
            if not isinstance(sh.get('treatment'), str) or not sh.get('treatment'):
                bad(f'{sid}: shot {f} has no treatment')
            if f.startswith('graphic:'):
                if 'clipSeconds' in sh:
                    bad(f'{sid}: graphic shot {f} must not carry clipSeconds')
                continue
            if f.endswith('/'):
                parts = f.strip('/').split('/')
                if len(parts) != 2:
                    bad(f'{sid}: clip "{f}" must be <group>/<seq>/')
                    continue
                g, seq = parts
                d = os.path.join(SCREENS, g, seq)
                if not os.path.isdir(d) or not any(x.endswith('.png') for x in os.listdir(d)):
                    bad(f'{sid}: clip dir {d} missing or has no frames')
                info = marks.get(f'clip:{g}/{seq}')
                if not info:
                    bad(f'{sid}: marks.json has no "clip:{g}/{seq}" base length')
                    continue
                base = info['seconds']
                length = sh.get('clipSeconds', base)
                if 'clipSeconds' in sh:
                    ratio = length / base
                    if ratio < 0.75 - EPS or ratio > 2.5 + EPS:
                        bad(f'{sid}: clip {f} clipSeconds {length} is {ratio:.3f}x of base {base} (allowed 0.75x-2.5x)')
                win = sh.get('end', 0) - sh.get('start', 0)
                if abs(win - length) > 0.02:
                    bad(f'{sid}: clip {f} shot window {win:.3f} s differs from its playback length {length} s')
                continue
            if f.endswith('.png') and f.count('/') == 1:
                if not os.path.isfile(os.path.join(UI, f)):
                    bad(f'{sid}: capture {f} not found under {UI}')
                if 'clipSeconds' in sh:
                    bad(f'{sid}: still {f} must not carry clipSeconds')
                continue
            bad(f'{sid}: unknown shot file form "{f}" (use <group>/<shot>.png, <group>/<seq>/, desktop/<shot>.png or graphic:...)')

    # ---------------------------------------------------------------- on-screen text, cues, badge, labels
    for s in scenes:
        sid = s.get('id')
        floating = []
        for o in s.get('onScreenText', []):
            t, role = o.get('text', ''), o.get('role', '')
            inside(sid, s, o.get('start'), o.get('end'), f'on-screen text "{t[:30]}"')
            if not t or not role:
                bad(f'{sid}: on-screen text needs text and role')
            if '₹' in t:
                if re.search(r'sora|headline', role, re.I):
                    bad(f'{sid}: "{t}" contains ₹ but its role says Sora/headline ({role})')
                if not re.search(r'plus jakarta sans|space mono', role, re.I):
                    bad(f'{sid}: "{t}" contains ₹ but its role names neither Plus Jakarta Sans nor Space Mono')
            if FLOATING_ROLE.match(role):
                floating.append((o.get('start'), o.get('end'), t))
        for tt in sorted({x[0] for x in floating}):
            live = [x[2] for x in floating if x[0] - EPS <= tt < x[1] - EPS]
            if len(live) > 4:
                bad(f'{sid}: {len(live)} floating labels/chips/tags on screen at {tt}: {live}')
        for cue in s.get('soundCues', []):
            at = cue.get('at')
            if not is_num(at) or not s['start'] - EPS <= at <= s['end'] + EPS:
                bad(f'{sid}: sound cue at {at} outside the scene')
        for w in s.get('demoBadge', []):
            inside(sid, s, w.get('start'), w.get('end'), 'demoBadge window')

    # ---------------------------------------------------------------- handoffs
    def check_handoff(sid, side, h):
        if not isinstance(h, dict):
            bad(f'{sid}: {side} must be an object')
            return
        for k in ('phone', 'screen', 'rig', 'leftColumn', 'overlays', 'notes'):
            if k not in h:
                bad(f'{sid}: {side} missing "{k}"')
        ph = h.get('phone')
        if ph not in ('default', 'none', 'custom'):
            bad(f'{sid}: {side}.phone must be default, none or custom')
        if ph == 'custom' and not isinstance(h.get('phoneSpec'), dict):
            bad(f'{sid}: {side} has phone "custom" but no phoneSpec')
        if ph != 'custom' and 'phoneSpec' in h:
            bad(f'{sid}: {side}.phoneSpec is only allowed with phone "custom"')
        scr = h.get('screen')
        if ph == 'none' and scr is not None:
            bad(f'{sid}: {side} has no phone but names a screen')
        if scr is not None and not (isinstance(scr, str) and scr.endswith('.png') and os.path.isfile(os.path.join(UI, scr))):
            bad(f'{sid}: {side}.screen "{scr}" is not an existing capture')
        if ph != 'none' and scr is None:
            bad(f'{sid}: {side} shows a phone but names no screen')
        r = h.get('rig')
        if r != 'identity':
            ok = (isinstance(r, dict) and is_num(r.get('s')) and isinstance(r.get('P'), list) and len(r['P']) == 2
                  and isinstance(r.get('T'), list) and len(r['T']) == 2 and all(is_num(v) for v in r['P'] + r['T']))
            if not ok:
                bad(f'{sid}: {side}.rig must be "identity" or {{s, P:[x,y], T:[x,y]}}')
        for k in ('leftColumn', 'overlays', 'notes'):
            if k in h and not isinstance(h[k], str):
                bad(f'{sid}: {side}.{k} must be a string')

    for s in scenes:
        check_handoff(s.get('id'), 'handoffIn', s.get('handoffIn'))
        check_handoff(s.get('id'), 'handoffOut', s.get('handoffOut'))
    for a, b in zip(scenes, scenes[1:]):
        if a.get('handoffOut') != b.get('handoffIn'):
            ha, hb = a.get('handoffOut') or {}, b.get('handoffIn') or {}
            diff = sorted(k for k in set(ha) | set(hb) if ha.get(k) != hb.get(k))
            bad(f'{a.get("id")}.handoffOut != {b.get("id")}.handoffIn (fields: {", ".join(diff)})')

    # ---------------------------------------------------------------- mark references in the build spec
    ref = re.compile(r'\b([a-z][a-z-]*/\d{2}-[a-z0-9-]+)\.([A-Za-z][A-Za-z0-9]*)\b')
    for s in scenes:
        for key, mark in ref.findall(s.get('animation', '')):
            if mark in ('png', 'mp4', 'json'):
                continue
            if key not in marks:
                bad(f'{s.get("id")}: animation names {key}.{mark} but marks.json has no "{key}"')
            elif mark not in marks[key]:
                bad(f'{s.get("id")}: animation names {key}.{mark} but "{key}" has marks {sorted(marks[key])}')

    # ---------------------------------------------------------------- end card + honesty copy
    texts = [o.get('text', '') for s in scenes for o in s.get('onScreenText', [])]
    if DISCLAIMER not in texts:
        bad('the verbatim disclaimer is missing from onScreenText')
    if TAGLINE not in texts:
        bad(f'the tagline "{TAGLINE}" is missing')
    if CTA not in texts:
        bad(f'the CTA "{CTA}" is missing')
    for s in scenes:
        sid = s.get('id')
        pool = [('narration', s.get('narration', ''))]
        pool += [('caption', c.get('text', '')) for c in s.get('captions', [])]
        pool += [('on-screen text', o.get('text', '')) for o in s.get('onScreenText', [])]
        for where, text in pool:
            if text == DISCLAIMER:
                continue
            flat = text.replace('\n', ' ')
            for pat, why in FORBIDDEN:
                if re.search(pat, flat, re.I):
                    bad(f'{sid}: {where} "{flat[:60]}" contains forbidden wording: {why}')

    # ---------------------------------------------------------------- addendum B: total and end card
    if total > MAX_TOTAL + EPS:
        bad(f'totalSeconds {total} is above the {MAX_TOTAL} s ceiling (director\'s addendum B)')
    if scenes:
        last = scenes[-1]
        dur = last.get('end', 0) - last.get('start', 0)
        if abs(dur - END_CARD_SECONDS) > 0.01:
            bad(f'{last.get("id")}: the end card lasts {dur:.2f} s (addendum B asks for {END_CARD_SECONDS} s)')
        for o in last.get('onScreenText', []):
            if o.get('text') != DISCLAIMER:
                continue
            m = re.search(r'fully legible (\d+(?:\.\d+)?)\s*[–-]\s*(\d+(?:\.\d+)?)', o.get('role', ''))
            if not m:
                bad(f'{last.get("id")}: the disclaimer role must state its "fully legible a–b" window (scene-local)')
            else:
                a, b = float(m.group(1)), float(m.group(2))
                if b - a < MIN_DISCLAIMER_LEGIBLE - EPS:
                    bad(f'{last.get("id")}: the disclaimer is fully legible for {b - a:.2f} s (min {MIN_DISCLAIMER_LEGIBLE})')
                if abs(last['start'] + b - o.get('end', 0)) > 0.01 or abs(last['start'] + b - last['end']) > 0.01:
                    bad(f'{last.get("id")}: the disclaimer\'s legible window must run to the last frame')

    # ---------------------------------------------------------------- addendum A: the saved-Home pick
    tonight = [s for s in scenes if any(o.get('text') == 'TONIGHT' for o in s.get('onScreenText', []))]
    if len(tonight) != 1:
        bad(f'addendum A: expected exactly one scene with the TONIGHT tag, found {len(tonight)}')
    else:
        s = tonight[0]
        starts = []
        for f in SAVED_HOME:
            hit = [x for x in s.get('shots', []) if x.get('file') == f]
            if not hit:
                bad(f'{s.get("id")}: addendum A: the saved-Home pick must show {f}')
            else:
                starts.append(hit[0].get('start', 0))
        if len(starts) == len(SAVED_HOME) and any(b <= a + EPS for a, b in zip(starts, starts[1:])):
            bad(f'{s.get("id")}: addendum A: {", ".join(SAVED_HOME)} must appear in this order')
        anim = s.get('animation', '')
        for mark, tap in SAVED_HOME_TAPS:
            if mark not in anim or tap not in anim:
                bad(f'{s.get("id")}: addendum A: the animation must ring and tap {mark} ("{tap}")')

    # ---------------------------------------------------------------- kicker = chapter, gone before the last frame
    for s in scenes:
        sid, chap = s.get('id'), s.get('chapter')
        kick = [o for o in s.get('onScreenText', []) if str(o.get('role', '')).startswith('kicker (kit .kicker')]
        if chap and not kick:
            bad(f'{sid}: has chapter "{chap}" but no kicker in onScreenText')
        for o in kick:
            if o.get('text') != chap:
                bad(f'{sid}: kicker text "{o.get("text")}" differs from the chapter "{chap}"')
            if is_num(o.get('end')) and o['end'] > s['end'] - KICKER_CLEAR + EPS:
                bad(f'{sid}: kicker ends at {o["end"]}, less than {KICKER_CLEAR} s before the scene ends ({s["end"]})')

    # ---------------------------------------------------------------- handoff screens = the shots live at the boundaries
    for s in scenes:
        sid = s.get('id')
        shots = s.get('shots', [])
        hi, ho = s.get('handoffIn') or {}, s.get('handoffOut') or {}
        if hi.get('screen') and not any(x.get('file') == hi['screen'] and abs(x.get('start', -1) - s['start']) <= 0.01 for x in shots):
            bad(f'{sid}: handoffIn.screen {hi["screen"]} is not a shot starting at the scene start')
        if ho.get('screen') and not any(x.get('file') == ho['screen'] and abs(x.get('end', -1) - s['end']) <= 0.01 for x in shots):
            bad(f'{sid}: handoffOut.screen {ho["screen"]} is not a shot ending at the scene end')
        app = sorted((x for x in shots if not x.get('file', '').startswith('graphic:')), key=lambda x: (x.get('start', 0), x.get('end', 0)))
        reach = None
        for x in app:
            if reach is not None and x.get('start', 0) > reach + 0.01:
                bad(f'{sid}: no app shot covers {reach}..{x.get("start")} (before {x.get("file")})')
            reach = max(reach if reach is not None else x.get('end', 0), x.get('end', 0))

    for line in infos:
        print(line)
    if problems:
        for p in problems:
            print('PROBLEM:', p)
        print(f'{len(problems)} problem(s)')
        return 1
    print(f'OK: no problems ({len(scenes)} scenes, {total} s, {total_words} words, {len(all_caps)} captions)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
