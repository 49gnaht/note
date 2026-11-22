# Kết quả thí nghiệm: Graphify có giúp Claude Code hiểu codebase tốt hơn không? (14 lượt thật)

Setup: Claude Code CLI 2.1.330, headless (`claude -p`), cùng model cho mọi lượt, graphify 0.9.115 (PyPI `graphifyy`).
- **A**: Claude Code trơn, không có graph.
- **B**: graph dựng sẵn + `graphify claude install` (CLAUDE.md section + PreToolUse hook nhắc dùng graph trước Grep/Read).
  Vì Claude Code lồng trong môi trường cloud này không tự nạp CLAUDE.md, nội dung CLAUDE.md được đưa vào bằng `--append-system-prompt` (mô phỏng máy local). Hook chạy thật.
- Tool cho phép như nhau: Read, Glob, Grep, Bash (graphify, grep, rg, find, cat, sed, head, tail, ls, wc, awk). Không cho chạy python.
- Câu hỏi chỉ hỏi, không sửa code. Đáp án chuẩn: tự đọc code + phân tích AST (xem RUBRIC.md).

## Codebase
| | Graphify (chính nó) | ERPNext |
|---|---|---|
| Quy mô | 103 file .py, ~106k dòng | 3.146 file .py, ~573k dòng (+2.052 JS/JSON) |
| Dựng graph | 40 giây, 27.100 node, 57.475 cạnh, $0 | 102 giây, 40.332 node, 109.161 cạnh, $0 |

## Câu hỏi
- **q1** (Graphify): `graphify update .` → graph.json, chuỗi hàm (9 ý)
- **q2** (Graphify): sửa `_weakest_shortest_path` ảnh hưởng lệnh/tool nào (2 ý + bẫy `graphify global path`)
- **q3** (Graphify): tool `shortest_path` chọn đường nào khi hòa (6 ý)
- **e1** (ERPNext): submit Sales Invoice → GL Entry (7 ý)
- **e2** (ERPNext): mọi class kế thừa StockController, 3 tầng (22 class; bẫy: Lead/SerialNo, class JS trùng tên)

## Kết quả
| Lượt | Điểm | Thời gian | Turns | Chi phí tham chiếu | Gọi graphify |
|---|---|---|---|---|---|
| q1-A | 9/9 | 51s | 14 | $0.38 | — |
| q1-B | 9/9 | 58s | 18 | $0.46 | 1 query |
| q2-A | 2/2, né bẫy | 52s | 14 | $0.35 | — |
| q2-B | 2/2, né bẫy | 59s | 10 | $0.34 | 2 explain |
| q3-A | 6/6 | 34s | 7 | $0.26 | — |
| q3-B | 6/6 | 35s | 6 | $0.27 | 1 query |
| e1-A ×2 | 7/7, 7/7 | 47s, 41s | 11, 6 | $0.27, $0.24 | — |
| e1-B ×2 | 7/7, 7/7 | 41s, 44s | 6, 10 | $0.26, $0.29 | 1 query mỗi lượt |
| e2-A ×2 | 22/22*, 22/22 | 54s, 64s | 13, 14 | $0.30, $0.33 | — |
| e2-B ×2 | 22/22, 22/22 | 69s, 61s | 12, 12 | $0.35, $0.31 | 1 query mỗi lượt |
\* e2-A-1 liệt kê đủ 22 nhưng dòng tóm tắt ghi nhầm "29 class".

Tổng: A trung bình 49,0s / $0.30; B trung bình 52,4s / $0.33 (từ .secs, total_cost_usd). **Chất lượng bằng nhau ở mọi câu (đều đạt trần). Thời gian, turns, chi phí chênh trong phạm vi nhiễu.**

## Thêm: model nhỏ (Haiku 5.5), 8 lượt (mỗi câu 1 lượt mỗi biến thể)
Giả thuyết: graph giúp model yếu hơn đỡ lạc trong codebase lớn.
| Câu | A (Haiku) | B (Haiku + graphify) | Gọi graphify (B) |
|---|---|---|---|
| q1 | 9/9 · 52s | 8/9 (thiếu `_rebuild_lock`) · 37s | 2 query |
| q2 | 2/2, né bẫy · 38s | 2/2, né bẫy, ghi đảo nhãn có hướng/vô hướng · 60s | ~9 lệnh (query, explain, path) |
| e1 | 7/7 · 47s | 7/7 · 30s | 1 query |
| e2 | 22/22, tự loại đúng BaseStockEntry/ManufactureStockEntry · 23s | 22/22 · 44s | 1 query |
Chi phí tham chiếu: $0.014–0.021 mỗi lượt (A tb $0.017, B tb $0.016), **rẻ hơn ~19 lần** so với model lớn ($0.31) với chất lượng gần như ngang.
→ Graph cũng không giúp Haiku trên các câu này. Haiku gọi graph nhiều hơn model lớn nhưng không cải thiện kết quả.
(Chấm Haiku: kiểm tra từ khóa theo rubric + đọc tay các chỗ nghi ngờ.)

## Quan sát hành vi
- Bản B (model lớn) luôn gọi `graphify query`/`explain` **1–2 lần ngay đầu**, đúng hướng dẫn trong CLAUDE.md, rồi chuyển sang Grep/Read như bản A. Hook (PreToolUse) chỉ chèn lời nhắc **1 lần** mỗi lần chạy, và ở cả 7 lần chạy model lớn lời nhắc đến *sau* khi đã hỏi đồ thị (theo `_nudge_allowed` trong cli.py: lời nhắc đầu tiên mỗi phiên luôn hiện; sau đó bị chặn nếu vừa có truy vấn đồ thị trong 30 phút; tối đa 5 lần/phiên). (Bản đầu của file này ghi "nhắc 3 lần" là đếm trùng dòng log, đã sửa.)
- Cả hai bản đều tìm ra chi tiết đáp án chuẩn của tôi bỏ sót (`_reexec` với PYTHONHASHSEED; `SalesInvoiceGLComposer`).
- `graphify query` bằng câu tự nhiên trả kết quả nhiễu: q1-B tìm thấy 778 node nhưng chỉ hiện 62 (ngân sách mặc định ~2000 token, chỉnh bằng `--budget`), lẫn code TypeScript và test. e1-B: 1029 tìm thấy, 52 hiện. `explain StockController --all` thì chính xác (đủ 6 lớp con); không có `--all` chỉ in 20 kết nối và thiếu SerialNo.
- `graphify path SalesInvoice make_entry` (thử tay, ERPNext) trả đường đi qua `make_reverse_gl_entries` (nhánh hủy), không phải nhánh submit.
- Trong môi trường cloud lồng nhau này, Claude Code không tự nạp CLAUDE.md lẫn AGENTS.md; vì vậy CLAUDE.md được đưa vào bằng `--append-system-prompt`. Đây là đặc thù môi trường, không phải hành vi trên máy dev (Graphify cố ý ghi vào AGENTS.md khi repo đã có file đó, vì Claude Code mặc định đọc AGENTS.md khi không có CLAUDE.md, xem install.py ~L2353).

## So với benchmark của Graphify
README: trên ERPNext, agent Claude Opus 4.8 giới hạn 14 turns, độ phủ 70,8% (grep/read) → 82,0% (có graphify), n=6.
Ở đây baseline đã đạt trần trên các câu tôi hỏi, nên không còn chỗ cho graph cải thiện. Khác biệt có thể do: model mới hơn, không giới hạn turns, câu hỏi khác.

## Hạn chế (nói trong video)
- 14 lượt, 5 câu hỏi, 2 codebase, 1 model: minh họa, không phải benchmark. Câu hỏi đều là loại "lần theo code", có đáp án kiểm chứng được.
- Không đo: dùng graph.html cho người đọc, onboarding, câu hỏi kiến trúc tổng quan, model nhỏ hơn, phiên làm việc dài nhiều câu hỏi (graph dựng một lần, dùng nhiều lần).
- CLAUDE.md được mô phỏng bằng `--append-system-prompt`.
