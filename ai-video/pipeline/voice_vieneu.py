"""Tạo giọng đọc tiếng Việt bằng VieNeu-TTS và canh lại timeline theo audio thật.

Dùng:
  HF_HUB_DISABLE_XET=1 python voice_vieneu.py timeline.json timeline_voiced.json voice.m4a [--voice "Hải Đăng"] [--cache tts]

- Mỗi câu phụ đề -> 1 file wav trong thư mục cache (tts/s{scene}_{i}.wav).
  File đã có thì bỏ qua: muốn tạo lại câu nào, xoá đúng file đó rồi chạy lại.
- Ghi timeline_voiced.json (thời gian thật) và voice.m4a (ghép cả bài, có khoảng nghỉ).
- PHON: bảng phiên âm áp trước khi đọc. Kinh nghiệm video 01: thay từ mượn bằng
  tiếng Việt ("ship" -> "giao hàng", "diff" -> "phần thay đổi") tốt hơn phiên âm.
"""
import argparse, json, os, re, subprocess

import soundfile as sf  # noqa: F401  (VieNeu save() cần)
from vieneu import Vieneu

# Chuỗi dài trước; chỉ thay nguyên từ, phân biệt hoa thường.
PHON = [
    ("andrej-karpathy-skills", "An-đrây Các-pa-thi Sờ-kiu"), ("CLAUDE.md", "Cờ-lốt chấm em-đê"),
    ("Claude Code", "Cờ-lốt Cốt"), ("Andrej Karpathy", "An-đrây Các-pa-thi"), ("Karpathy", "Các-pa-thi"),
    ("Claude", "Cờ-lốt"), ("Tesla", "Tét-la"), ("benchmark", "bén-mác"), ("plugin", "plờ-gin"),
    ("module", "mô-đun"), ("model", "mô-đen"), ("repo", "ri-pô"), ("test", "tét"), ("code", "cốt"),
    ("AI", "ây-ai"), ("ok", "ô-kê"),
]
GAP, SCENE_GAP, LEAD_IN, TAIL = 0.35, 1.1, 0.6, 1.5


def speakable(text):
    for a, b in PHON:
        text = re.sub(r"(?<![\w-])" + re.escape(a) + r"(?![\w-])", b, text)
    return text.replace('"', "")


def dur(path):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]))


def silence(cache, s):
    p = os.path.join(cache, f"sil_{int(s * 1000)}.wav")
    if not os.path.exists(p):
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono",
                        "-t", str(s), p], check=True)
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dst"); ap.add_argument("audio")
    ap.add_argument("--voice", default="Hải Đăng"); ap.add_argument("--cache", default="tts")
    a = ap.parse_args()
    os.makedirs(a.cache, exist_ok=True)
    tl = json.load(open(a.src))
    tts = None
    t, parts = LEAD_IN, [silence(a.cache, LEAD_IN)]
    for sc in tl["scenes"]:
        sc_start = t
        for i, sub in enumerate(sc["subs"]):
            wav = os.path.join(a.cache, f"s{sc['id']}_{i}.wav")
            if not os.path.exists(wav):
                tts = tts or Vieneu()
                tts.save(tts.infer(speakable(sub["text"]), voice=a.voice), wav)
            d = dur(wav)
            sub["t0"], sub["t1"] = round(t, 2), round(t + d, 2)
            parts += [wav, silence(a.cache, GAP)]
            t += d + GAP
        parts.append(silence(a.cache, SCENE_GAP)); t += SCENE_GAP
        sc["start"] = round(sc_start - (LEAD_IN if sc is tl["scenes"][0] else 0.4), 2)
        sc["end"] = round(t - 0.4, 2)
    tl["scenes"][-1]["end"] = tl["duration"] = round(t + TAIL, 2)
    json.dump(tl, open(a.dst, "w"), ensure_ascii=False, indent=1)
    lst = os.path.join(a.cache, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{os.path.abspath(p)}'\n" for p in parts)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
                    "-ar", "48000", "-ac", "1", "-c:a", "aac", "-b:a", "128k", a.audio], check=True)
    print("voiced duration:", tl["duration"], "s")


if __name__ == "__main__":
    main()
