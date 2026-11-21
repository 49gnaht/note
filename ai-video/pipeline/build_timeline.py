# Parse script_final.md -> timeline.json (scene + subtitle timing estimated from syllables)
import re, json, sys
SRC = sys.argv[1]; OUT = sys.argv[2]
RATE = 3.8; PAUSE = {',': 0.22, ':': 0.3, '.': 0.45, '?': 0.45, '!': 0.45}
s = open(SRC).read()
scenes = re.findall(r'## Cảnh (\d+)\s*[—:-]\s*(.*?) \(.*?\)\n.*?\*\*Lời:\*\*\n(.*?)(?=\n## |\n---)', s, re.S)
t = 0.6; out = []
for num, name, narr in scenes:
    sents0 = [x.strip() for x in re.split(r'(?<=[.?!])\s+', narr.strip().replace('\n', ' ')) if x.strip()]
    sents=[]
    for x in sents0:
        if sents and len(x.split())<7 and len(sents[-1])<80: sents[-1]+=' '+x
        elif sents and len(sents[-1].split())<7: sents[-1]+=' '+x
        else: sents.append(x)
    subs = []; start = t
    for sent in sents:
        # split long sentences at commas/colons into subtitle chunks <= 90 chars
        parts, cur = [], ''
        for piece in re.split(r'(?<=[,:])\s+', sent):
            if cur and len(cur) + len(piece) > 90: parts.append(cur); cur = piece
            else: cur = (cur + ' ' + piece).strip()
        parts.append(cur)
        merged=[]
        for p_ in parts:
            if merged and len(p_.split())<7: merged[-1]+=' '+p_
            else: merged.append(p_)
        if len(merged)>1 and len(merged[0].split())<7: merged[1]=merged[0]+' '+merged[1]; merged=merged[1:]
        parts=merged
        for p in parts:
            syl = len(re.findall(r"[\wÀ-ỹ]+", p))
            d = syl / RATE + sum(PAUSE.get(c, 0) for c in p)
            subs.append({'t0': round(t, 2), 't1': round(t + d, 2), 'text': p}); t += d
    t += 0.8  # breath between scenes
    out.append({'id': int(num), 'name': name, 'start': round(start - (0.6 if num == '1' else 0.4), 2), 'end': round(t - 0.4, 2), 'subs': subs})
out[-1]['end'] = round(t + 1.5, 2)
json.dump({'duration': round(t + 1.5, 2), 'scenes': out}, open(OUT, 'w'), ensure_ascii=False, indent=1)
for sc in out: print(sc['id'], sc['name'], sc['start'], '→', sc['end'], f"({sc['end']-sc['start']:.1f}s)")
print('TOTAL', round(t + 1.5, 1), 's')
