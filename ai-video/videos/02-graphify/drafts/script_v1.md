# Kịch bản v1: "Đồ thị cho AI đọc code: 150 nghìn sao, và một kết quả tôi không ngờ"
Repo: Graphify-Labs/graphify (~151,6k ⭐ theo GitHub search 21/11/2026; YC S26) · Mục tiêu: ≤ 4:55 · Giọng: VieNeu "Hải Đăng"
Quy ước lời đọc: dùng từ tiếng Việt thay từ mượn ("đồ thị", "tìm kiếm văn bản", "bài đo"); tên riêng có bảng phiên âm cuối file; câu tối thiểu 7 chữ.

---

## Cảnh 1: Hook (0:00–0:28)
**Hình:** Số sao 151,6k đếm lên; logo-chữ "Graphify"; dòng hứa hẹn "Query instead of grepping". Rồi bảng điểm hai cột "Không có đồ thị" / "Có đồ thị": 5 câu, các ô lần lượt hiện dấu ✓ giống nhau. Cuối cùng một thẻ: "Haiku: rẻ hơn ~19 lần".
**Lời:**
Một dự án hơn một trăm năm mươi nghìn sao, được Y Combinator đầu tư, hứa một điều rất hấp dẫn. Thay vì để AI lục từng file, hãy cho nó một bản đồ của toàn bộ codebase. Tôi chạy hai mươi hai lượt Claude Code thật, trên hai codebase, với năm câu hỏi khó. Có bản đồ hay không, điểm số như nhau. Nhưng kết quả làm tôi bất ngờ nhất lại nằm ở chỗ khác.

## Cảnh 2: Graphify là gì (0:28–1:02)
**Hình:** Sơ đồ: thư mục code → (tree-sitter, chạy trên máy) → graph.json với nút và cạnh. Ba lệnh hiện lần lượt: `graphify query`, `graphify path`, `graphify explain`. Một khung nhỏ: "PreToolUse hook: nhắc Claude dùng graph trước khi grep". Chú thích: "Dựng graph: không gọi LLM, $0".
**Lời:**
Graphify đọc toàn bộ mã nguồn của bạn và dựng thành một đồ thị kiến thức. Mỗi hàm, mỗi lớp là một nút, còn quan hệ gọi hàm, kế thừa, nhập thư viện là các cạnh. Việc dựng đồ thị chạy hoàn toàn trên máy, không tốn tiền gọi mô hình. Sau đó AI có thể truy vấn đồ thị, tìm đường đi giữa hai thành phần, hoặc giải thích một khái niệm. Với Claude Code, Graphify còn cài một đoạn nhắc tự động, mỗi khi Claude định tìm kiếm văn bản thì được nhắc hãy hỏi đồ thị trước.

## Cảnh 3: Lời hứa và bài đo của họ (1:02–1:22)
**Hình:** Trích bảng trong BENCHMARKS.md: "ERPNext · key-fact coverage · 70.8% → 82.0%". Chú thích nhỏ: "Claude Opus 4.8 · tối đa 14 lượt · n=6".
**Lời:**
Bài đo của chính Graphify trên ERPNext, một phần mềm quản lý doanh nghiệp khoảng một triệu dòng, cho thấy độ đầy đủ của câu trả lời tăng từ bảy mươi mốt lên tám mươi hai phần trăm. Tôi muốn tự kiểm tra con số đó.

## Cảnh 4: Thí nghiệm (1:22–1:58)
**Hình:** Hai thẻ codebase: "Graphify (chính nó) · 106k dòng · graph 40s" và "ERPNext · 573k dòng Python · graph 102s". Danh sách 5 câu hỏi rút gọn. Hai cột biến thể A/B. Chú thích suốt cảnh: "22 lượt · chạy tự động · CLAUDE.md mô phỏng bằng system prompt · minh họa, không phải benchmark".
**Lời:**
Tôi dùng hai codebase. Thứ nhất là chính mã nguồn của Graphify, khoảng một trăm nghìn dòng, vừa được cập nhật hôm nay nên AI không thể trả lời bằng trí nhớ. Thứ hai là ERPNext, hơn năm trăm nghìn dòng Python. Năm câu hỏi đều phải lần theo code qua nhiều file, ví dụ từ lúc bấm gửi hóa đơn đến lúc ghi sổ cái, hay liệt kê mọi lớp kế thừa qua ba tầng. Đáp án tôi tự kiểm chứng bằng cách đọc code và phân tích cú pháp. Mỗi câu chạy hai cách: Claude Code bình thường, và Claude Code có Graphify đầy đủ.

## Cảnh 5: Kết quả với mô hình lớn (1:58–2:35)
**Hình:** Bảng 5 dòng, hai cột điểm giống hệt (9/9, 2/2, 6/6, 7/7, 22/22). Dưới bảng: "Thời gian tb 51s vs 52s · Chi phí tb $0.30 vs $0.33". Rồi dòng thời gian một lượt có graph: 1 ô "graphify query" ở đầu, tiếp theo là chuỗi dài ô "Grep / Read".
**Lời:**
Với mô hình lớn, kết quả hòa tuyệt đối. Cả hai cách đều trả lời đúng mọi ý, kể cả câu có bẫy là các lớp trùng tên trong mã JavaScript. Thời gian và chi phí cũng gần như bằng nhau. Điều thú vị là cách Claude làm việc. Khi có đồ thị, nó hỏi đồ thị một lần ở đầu để định hướng, rồi quay về tìm kiếm văn bản và đọc file như bình thường, dù được nhắc ba lần mỗi lượt.

## Cảnh 6: Vì sao? (2:35–3:12)
**Hình:** Màn hình `graphify query "how does graphify update write graph.json"` → "470 nodes found · TRUNCATED", vài dòng kết quả lạc đề (index.ts, test). Bên cạnh: `graphify explain StockController` → đúng 6 cạnh inherits. Cuối: hai cột "Bài đo của họ: model cũ, tối đa 14 lượt" / "Ở đây: model mới, không giới hạn".
**Lời:**
Tôi thấy hai lý do. Thứ nhất, truy vấn bằng câu tự nhiên khá nhiễu. Một câu hỏi trả về bốn trăm bảy mươi nút, lẫn cả mã TypeScript và file kiểm thử không liên quan. Ngược lại, hỏi theo đúng tên một lớp thì đồ thị trả lời rất chính xác. Thứ hai, mô hình bây giờ tìm kiếm văn bản quá giỏi, nên đã đạt điểm tối đa và không còn chỗ để cải thiện. Bài đo của Graphify dùng mô hình cũ hơn và giới hạn mười bốn lượt, điều kiện đó khác với thí nghiệm của tôi.

## Cảnh 7: Mô hình nhỏ (3:12–3:50)
**Hình:** Bảng Haiku: A 9/9, 2/2, 7/7, 22/22 · B 8/9, 2/2, 7/7, 22/22. Thẻ lớn: "$0,016 vs $0,31 mỗi câu · rẻ hơn ~19 lần".
**Lời:**
Vậy đồ thị có giúp mô hình nhỏ đỡ lạc hơn không? Tôi chạy lại bằng Haiku, mô hình nhỏ và rẻ nhất. Khi có đồ thị, Haiku hỏi đồ thị nhiều hơn, nhưng điểm vẫn không tăng, thậm chí còn thiếu một ý ở một câu. Và đây là điều tôi không ngờ: không có đồ thị, Haiku vẫn trả lời đúng gần như mọi ý, với chi phí rẻ hơn khoảng mười chín lần. Nếu muốn tiết kiệm khi hỏi về code, hãy thử đổi mô hình trước khi thêm công cụ.

## Cảnh 8: Khi nào vẫn nên dùng Graphify (3:50–4:30)
**Hình:** Ảnh graph.html (đồ thị màu theo cụm). Checklist: "Người mới vào dự án · Xem kiến trúc tổng quan · explain/path theo tên chính xác · Dựng graph miễn phí". Một thẻ cảnh báo: "Repo có sẵn AGENTS.md → hướng dẫn ghi vào đó; Claude Code (bản thử) không đọc file này".
**Lời:**
Thí nghiệm này chỉ đo một việc là AI trả lời câu hỏi về code. Tôi chưa đo những việc Graphify cũng nhắm tới: trang đồ thị cho con người xem, giúp người mới làm quen dự án, hay câu hỏi về kiến trúc tổng thể. Nếu dùng, hãy hỏi theo tên chính xác thay vì câu tự nhiên. Và nếu dự án của bạn đã có file AGENTS.md, hãy kiểm tra lại, vì Graphify sẽ ghi hướng dẫn vào đó, mà Claude Code trong thử nghiệm của tôi không đọc file này.

## Cảnh 9: Kết (4:30–4:50)
**Hình:** Dòng chữ lớn; chú thích: "22 lượt · 2 codebase · 5 câu hỏi · minh họa, không phải benchmark".
**Lời:**
Đừng tin số sao, cũng đừng tin bài đo, kể cả bài đo của tôi. Dựng đồ thị chỉ mất một đến hai phút và hoàn toàn miễn phí, nên hãy tự thử trên chính codebase của bạn.

---

## Bảng phiên âm (áp khi tạo giọng)
| Viết | Đọc |
|---|---|
| Graphify | Gráp-phi-phai |
| ERPNext | E-R-P Nếch |
| Claude Code | Cờ-lốt Cốt |
| Claude | Cờ-lốt |
| Haiku | Hai-cu |
| Y Combinator | Uai Com-bi-nây-tơ |
| TypeScript | Tai-sờ-cờ-ríp |
| JavaScript | Gia-va-sờ-cờ-ríp |
| AGENTS.md | Ây-giần chấm em-đê |
| codebase | cốt-bết |
| code | cốt |
| file | phai |
| AI | ây-ai |
