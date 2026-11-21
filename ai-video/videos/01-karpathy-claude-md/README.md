# 01: "Bảo AI hỏi trước thì dễ. Bảo nó viết ít thì khó."

Review repo [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) (~234,9k ⭐, 21/11/2026). Video dài 4:02, giọng VieNeu "Hải Đăng".

| File | Nội dung |
|---|---|
| `script.md` | Kịch bản cuối (v3, đã qua 3 vòng review, đã sửa lời cho giọng đọc) |
| `drafts/` | Kịch bản v1 (5,8/10) và v2 (7,5/10), để so sánh |
| `experiment/RESULTS.md` | Số liệu 21 lượt Claude Code (+3 lượt "ok" của biến thể một câu) |
| `experiment/base/` | Codebase mẫu `shop` có cài sẵn bẫy |
| `experiment/runs/` | Dữ liệu thô: câu trả lời (.json), diff, kết quả pytest, thời gian |
| `video.html` | Trang dựng hình 10 cảnh (cần `data.js` tạo bằng `pipeline/make_data.py`) |
| `timeline_voiced.json` | Mốc thời gian thật theo giọng đọc |
| `karpathy_v1.vi.srt` | Phụ đề |
| `diff_sample.txt` | Diff thật (base-3) cuộn trên màn hình ở cảnh 6 |

Dựng lại video: xem lệnh ở [README chính](../../README.md). Bước giọng đọc cần chạy lại VieNeu, vì file wav không được commit.

**Kết luận chính:** chỉ cần thêm một câu "chưa rõ thì hỏi trước" là Claude cũng biết dừng lại hỏi. Nhưng khi bạn gõ "ok", code lại phình to hơn (59–90 dòng). Có file Karpathy thì chỉ 23–26 dòng. Cả hai cách hỏi trước đều tốn thêm khoảng 70% chi phí.
