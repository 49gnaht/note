"""timeline(.json) -> data.js (cho trang HTML dựng hình) + phụ đề .srt

Dùng: python make_data.py timeline_voiced.json data.js subs.srt [extra.txt]
extra.txt (tuỳ chọn): các dòng text đưa vào window.DIFF (ví dụ diff thật để cuộn trên màn hình).
"""
import json, sys

src, js_out, srt_out = sys.argv[1:4]
tl = json.load(open(src))
extra = [l.rstrip("\n") for l in open(sys.argv[4])] if len(sys.argv) > 4 else []
open(js_out, "w").write("window.TL=" + json.dumps(tl, ensure_ascii=False) + ";\nwindow.DIFF="
                        + json.dumps(extra, ensure_ascii=False) + ";\n")
f = lambda s: f"{int(s // 3600):02}:{int(s % 3600 // 60):02}:{int(s % 60):02},{int(round(s % 1 * 1000)) % 1000:03}"
cues = [x for sc in tl["scenes"] for x in sc["subs"]]
open(srt_out, "w").write("\n".join(f"{i}\n{f(x['t0'])} --> {f(x['t1'])}\n{x['text']}\n" for i, x in enumerate(cues, 1)))
print(len(cues), "cues,", tl["duration"], "s")
