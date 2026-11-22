# AI video pipeline: review repo AI bằng thí nghiệm thật

Quy trình làm video review khoảng 4–5 phút cho một repo AI: thí nghiệm thật bằng Claude Code, kịch bản qua agent review, hình dựng bằng HTML, giọng đọc tiếng Việt chạy offline, soát lỗi phát âm bằng Whisper.
Mọi bước chạy trong container cloud. Chỉ bước thí nghiệm và review dùng hạn mức gói Claude; render, giọng đọc và Whisper chạy local, miễn phí.

| Video | Repo | Kết quả |
|---|---|---|
| [01](videos/01-karpathy-claude-md/) | multica-ai/andrej-karpathy-skills | 4:02 · 21 lượt A/B · review 5,8 → 7,5 → 8,0 |
| [02](videos/02-graphify/) | Graphify-Labs/graphify | ~4:00 · 22 lần chạy, 2 codebase · review 6,2 → 7,5 → v3 |

## Quy trình (video 01 mất khoảng nửa ngày)

```
1. Thí nghiệm   run_ab.sh + summarize_runs.py   -> experiment/RESULTS.md
2. Kịch bản     script.md (cảnh: **Hình:** / **Lời:**)
3. Review       agent review theo pipeline/review_prompt.md, tối đa 3 vòng, dừng khi ≥ 8/10
4. Dựng hình    video.html (window.seek(t) vẽ frame tại thời điểm t)
5. Giọng đọc    build_timeline.py -> voice_vieneu.py -> asr_check.py (sửa, tạo lại câu lỗi)
6. Render       make_data.py -> render.js -> ffmpeg ghép tiếng
```

### Lệnh cụ thể

```bash
P=ai-video/pipeline; V=ai-video/videos/NN-ten-video

# 1. Thí nghiệm: 3 biến thể × 3 lượt, rồi lượt "ok" cho biến thể hỏi trước
$P/run_ab.sh $V/experiment/base /tmp/runs feature-base     "<yêu cầu>"
$P/run_ab.sh $V/experiment/base /tmp/runs feature-prompt   "<yêu cầu> Chỗ nào chưa rõ thì hỏi mình trước khi code."
$P/run_ab.sh $V/experiment/base /tmp/runs feature-karpathy "<yêu cầu>" path/to/CLAUDE.md
RESUME=1 $P/run_ab.sh $V/experiment/base /tmp/runs feature-karpathy "ok, làm theo phương án đề xuất của bạn."

# 5. Giọng đọc (cần: pip install vieneu faster-whisper soundfile; HF_HUB_DISABLE_XET=1)
python3 $P/build_timeline.py $V/script.md timeline.json
HF_HUB_DISABLE_XET=1 python $P/voice_vieneu.py timeline.json timeline_voiced.json voice.m4a --voice "Hải Đăng"
HF_HUB_DISABLE_XET=1 python $P/asr_check.py timeline_voiced.json          # ~10 phút trên CPU

# 6. Render (Chromium + Playwright có sẵn trong container)
python3 $P/make_data.py timeline_voiced.json $V/data.js $V/subs.vi.srt [$V/diff_sample.txt]
node $P/render.js $V/video.html silent.mp4 $(python3 -c "import json;print(json.load(open('timeline_voiced.json'))['duration'])") 30
ffmpeg -i silent.mp4 -i voice.m4a -c:v copy -c:a aac -b:a 160k -af "apad,loudnorm=I=-16:TP=-1.5:LRA=11" -shortest out.mp4
```

Render 4 phút ở 1080p/30fps mất khoảng 8 phút. Trước khi render cả video, chụp thử 1–2 frame mỗi cảnh để soát bố cục.

## Cài đặt môi trường (một lần)

- **Mạng** (environment Default): `huggingface.co`, `us.aws.cdn.hf.co` (CDN tải model VieNeu và Whisper). Cần đặt `HF_HUB_DISABLE_XET=1`, nếu không Hugging Face sẽ gọi `cas-server.xethub.hf.co` (chưa mở).
- **edge-tts** cần `speech.platform.bing.com`. Không còn dùng vì VieNeu hay hơn và chạy offline.
- **Python**: `python3 -m venv vnenv && vnenv/bin/pip install vieneu faster-whisper`
- **Font**: Inter (chữ) và JetBrains Mono (code). Không dùng DejaVu Sans Mono: font này hiển thị sai dấu tiếng Việt.

## Bài học từ video 01

**Thí nghiệm**
- Luôn có **biến thể đối chứng rẻ** (chỉ thêm một câu vào prompt). Ở video 01, chính biến thể này đổi hẳn thông điệp: "hỏi trước" chỉ cần một câu, giá trị thật của file là "viết ít".
- Đo **đến khi tính năng xong** (lượt "ok"), không dừng ở lượt đầu. Nếu dừng ở lượt đầu sẽ kết luận sai về chi phí.
- Codebase mẫu nên cài sẵn "bẫy" (code cũ còn được gọi, comment dặn hỏi, bug thật), và **phải báo kết quả bẫy** kể cả khi không bản nào dính.
- Ghi rõ hạn chế: số lượt, một model, headless thì "hỏi" nghĩa là "dừng lại".

**Kịch bản và review**
- Vòng 1 thường bị chê **thiếu công bằng** (phóng đại bản đối chứng). Agent review đọc dữ liệu thô nên bắt được các lỗi này.
- Không đưa suy đoán nhân quả chưa kiểm chứng vào lời đọc.

**Giọng đọc (VieNeu-TTS)**
- Tạo giọng **theo từng câu**. Câu dưới 7 chữ phải gộp với câu bên cạnh, nếu không sẽ bị đọc lơ lớ.
- **Thay từ mượn bằng tiếng Việt** thay vì phiên âm: `diff` bị đọc thành "đít", `ship` thành "xít", `bug` thành "bức", `shop` thành "xúc". Cụm "mặc định" bị nghe thành "mắc bệnh", đã thay bằng "đề xuất".
- **Phiên âm chữ cái không dùng dấu gạch nối** (video 02): "E-R-P Nếch" bị đọc thành "E gạch nối R gạch nối P". Viết cách nhau bằng dấu cách: "e rờ pê nếch", "ây pi ai".
- Truyền `--script script.md` cho `voice_vieneu.py` để dùng bảng phiên âm ở cuối kịch bản (`## Bảng phiên âm`).
- Tên tự đặt (như "Graphify") thì Whisper gần như luôn chép sai. Nếu tên đã hiện trên hình thì bỏ qua những câu điểm thấp chỉ vì tên.
- Khoảng nghỉ 0,35 giây giữa các câu và 1,1 giây giữa các cảnh. Giọng Hải Đăng đọc khoảng 4,4 âm tiết/giây.
- Kết quả soát bằng Whisper medium: trung bình 0,86. Câu điểm thấp chủ yếu do Whisper viết số bằng chữ số hoặc nghe sai tên riêng, không phải lỗi đọc.

**Hình**
- Cho hiệu ứng chạy theo **mốc thời gian của từng câu phụ đề** (`sc.subs[k].t0`), đừng chạy theo tỉ lệ thời lượng cảnh. Nếu không, khi đổi giọng đọc hình sẽ lệch lời (cảnh 7 của video 01 từng bị lệch như vậy).
- Tắt ligature của font code để `>=` không bị biến thành `≥`.

## Chi phí (gói Pro)

- Thí nghiệm (24 lượt `claude -p`) và 3 vòng review **trừ vào hạn mức gói**, không phát sinh tiền, trừ khi bạn bật extra usage. Giá API tham chiếu khoảng $8.
- Giọng đọc, Whisper, render: chạy local, $0.
- Video `.mp4` không commit vào git vì file nặng.
