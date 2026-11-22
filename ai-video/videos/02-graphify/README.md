# 02: Graphify, đồ thị cho AI đọc code

Review [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) (~151,6k ⭐, 21/11/2026, YC S26). graphify 0.9.115, Claude Code 2.1.330. Video dài khoảng 4:00, giọng VieNeu "Hải Đăng".

**Kết luận chính:** trên 2 codebase (Graphify ~106k dòng, ERPNext ~573k dòng Python), 5 câu hỏi lần theo code, có đồ thị hay không thì mô hình lớn đều đạt điểm tối đa, thời gian và chi phí ngang nhau. Haiku (4 câu, 1 lần chạy mỗi ô) cũng không cải thiện khi có đồ thị. Không có đồ thị, Haiku vẫn đúng mọi ý với giá API rẻ hơn khoảng 19 lần. Chưa đo: chế độ `--strict`, MCP server, phiên dài, graph.html cho người đọc.

| File | Nội dung |
|---|---|
| `script.md` | Kịch bản cuối (v3: review 6,2 → 7,5 → áp sửa vòng 2), có bảng phiên âm |
| `drafts/` | Kịch bản v1, v2 |
| `experiment/RESULTS.md` | Số liệu 22 lần chạy và các quan sát |
| `experiment/RUBRIC.md` | Đáp án chuẩn và thang chấm (đọc code + AST) |
| `experiment/questions.json`, `run.sh`, `tools.py` | Câu hỏi, script chạy A/B, script đếm tool trong transcript |
| `experiment/runs/` | Câu trả lời cuối (.json) và thời gian (.secs) của 22 lần chạy |
| `video.html`, `timeline_voiced.json`, `graphify_v1.vi.srt` | Dựng hình, mốc thời gian theo giọng, phụ đề |
| `q1_query_output.txt` | Output thật của `graphify query` ở lần chạy q1-B (778 nút, hiện 62) |

**Tái lập:** `run.sh` đang có đường dẫn cố định tới thư mục tạm của phiên làm. Muốn chạy lại thì sửa biến `D`. Thư mục `target/` là bản sao repo Graphify, `erp/` là bản sao ERPNext (`git clone --depth 1`), mỗi thư mục được dựng graph bằng `graphify update .`.
Môi trường cloud lồng nhau không tự nạp CLAUDE.md, nên bản B đưa CLAUDE.md vào bằng `--append-system-prompt`. Transcript không được commit vì chứa thông tin phiên.
