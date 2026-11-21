"""Soát giọng đọc bằng Whisper (chạy trên CPU): nghe lại từng câu và so với kịch bản.

Dùng: HF_HUB_DISABLE_XET=1 python asr_check.py timeline_voiced.json [--cache tts] [--model medium] [--only list.txt]
In ra các câu khớp kém nhất. Lưu ý khi đọc kết quả:
- Whisper viết số bằng chữ số ("25" vs "hai mươi lăm") -> điểm thấp nhưng KHÔNG phải lỗi.
- Tên riêng tiếng Anh thường bị nghe sai -> tên đã hiện trên hình thì bỏ qua.
- Lỗi thật: cùng một từ bị nghe sai giống nhau ở nhiều câu (video 01: "mặc định" -> "mắc bệnh",
  "diff" -> "đít"). Sửa bằng cách đổi từ trong kịch bản, xoá wav câu đó, tạo lại.
- Model "small" quá kém với tiếng Việt; dùng "medium".
"""
import argparse, difflib, io, json, re, subprocess, unicodedata

import soundfile as sf
from faster_whisper import WhisperModel

ap = argparse.ArgumentParser()
ap.add_argument("timeline"); ap.add_argument("--cache", default="tts")
ap.add_argument("--model", default="medium"); ap.add_argument("--only")
ap.add_argument("--show", type=int, default=15)
a = ap.parse_args()
only = set(open(a.only).read().split()) if a.only else None
norm = lambda s: re.findall(r"[\wÀ-ỹ]+", unicodedata.normalize("NFC", s.lower()))
m = WhisperModel(a.model, device="cpu", compute_type="int8")
res = []
for sc in json.load(open(a.timeline))["scenes"]:
    for i, x in enumerate(sc["subs"]):
        wav = f"{a.cache}/s{sc['id']}_{i}.wav"
        if only and wav not in only:
            continue
        raw = subprocess.check_output(["ffmpeg", "-loglevel", "error", "-i", wav, "-ar", "16000", "-ac", "1", "-f", "wav", "-"])
        audio, _ = sf.read(io.BytesIO(raw), dtype="float32")  # tránh lỗi PyAV khi mở file trực tiếp
        segs, _ = m.transcribe(audio, language="vi", beam_size=5)
        heard = " ".join(s.text.strip() for s in segs)
        res.append((difflib.SequenceMatcher(None, norm(x["text"]), norm(heard)).ratio(), wav, x["text"], heard))
res.sort()
print(f"avg {sum(r[0] for r in res) / len(res):.2f} | >=0.9: {sum(r[0] >= .9 for r in res)}/{len(res)}")
for r, wav, kb, heard in res[:a.show]:
    print(f"\n{r:.2f} {wav}\n  KỊCH BẢN: {kb}\n  NGHE:     {heard}")
