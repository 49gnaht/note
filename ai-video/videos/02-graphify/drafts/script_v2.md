# Kịch bản v2: "Đồ thị cho AI đọc code: 150 nghìn sao, và một kết quả tôi không ngờ"
Repo: Graphify-Labs/graphify (~151,6k ⭐ theo GitHub search 21/11/2026; YC S26) · graphify 0.9.115 · Claude Code 2.1.330 · Mục tiêu: ≤ 4:55 · Giọng: VieNeu "Hải Đăng"
Quy ước: "lần chạy" = một run; "bước" = một turn. Lời đọc dùng từ tiếng Việt thay từ mượn; câu tối thiểu 7 chữ; tên riêng có bảng phiên âm cuối file.

Thay đổi so với v1 (review vòng 1: 6,2/10): bỏ "nhắc ba lần" (thực tế: hỏi đồ thị trước, lời nhắc chỉ 1 lần, đến sau); bỏ "470 nút" (thay bằng output thật q1-B: 778 tìm thấy, 62 hiện); bỏ lời khuyên AGENTS.md (Claude Code mặc định có đọc AGENTS.md; hiện tượng là do môi trường cloud); thay lý do "14 lượt" bằng lý do thật: câu hỏi có sẵn tên định danh; explain cần `--all`; Haiku: 4 câu, 1 lần, giá API; "miễn phí" chỉ với phần mã nguồn; thêm phần cài đặt và ví dụ Graphify làm tốt; nêu cấu hình chưa thử (strict, MCP).

---

## Cảnh 1: Hook (0:00–0:30)
**Hình:** Số sao 151,6k đếm lên; chữ "Graphify"; dòng hứa hẹn "query instead of grepping". Bảng điểm hai cột "Không có đồ thị" / "Có đồ thị", nhãn "mô hình lớn": 5 câu, các ô hiện dấu ✓ giống nhau. Cuối: thẻ "Haiku: rẻ hơn ~19 lần (giá API)".
**Lời:**
Một dự án hơn một trăm năm mươi nghìn sao, thuộc khóa S26 của Y Combinator, hứa một điều rất hấp dẫn. Thay vì để AI lục từng file, hãy cho nó một bản đồ của toàn bộ codebase. Tôi cho Claude Code chạy thật hai mươi hai lần, trên hai codebase, với năm câu hỏi khó. Với mô hình lớn, có bản đồ hay không thì điểm số vẫn như nhau. Nhưng điều làm tôi bất ngờ nhất lại nằm ở chỗ khác.

## Cảnh 2: Graphify là gì (0:30–1:02)
**Hình:** Sơ đồ: thư mục code → (tree-sitter, chạy trên máy) → graph.json với nút và cạnh. Ba lệnh: `graphify query`, `graphify path`, `graphify explain`. Khung nhỏ: "Claude Code: hướng dẫn trong CLAUDE.md + lời nhắc tự động trước Grep/Read". Chú thích: "Phần mã nguồn: không gọi LLM, $0 · docs/PDF/ảnh: cần LLM".
**Lời:**
Graphify đọc mã nguồn của bạn và dựng thành một đồ thị kiến thức. Mỗi hàm, mỗi lớp là một nút, còn quan hệ gọi hàm, kế thừa và nhập thư viện là các cạnh. Với phần mã nguồn, việc dựng đồ thị chạy hoàn toàn trên máy, không tốn tiền gọi mô hình. Sau đó AI có thể truy vấn đồ thị, tìm đường đi giữa hai thành phần, hoặc giải thích một khái niệm. Với Claude Code, Graphify ghi thêm hướng dẫn và một lời nhắc tự động. Mỗi khi Claude định tìm kiếm văn bản mà chưa hỏi đồ thị, nó sẽ được nhắc.

## Cảnh 3: Bài đo của họ (1:02–1:22)
**Hình:** Trích BENCHMARKS.md: "ERPNext · key-fact coverage · 70.8% → 82.0%". Chú thích: "Claude Opus 4.8 · harness riêng · graphify là một tool · n=6".
**Lời:**
Graphify có bài đo riêng trên ERPNext, một phần mềm quản lý doanh nghiệp rất lớn. Theo bài đo đó, độ đầy đủ của câu trả lời tăng từ bảy mươi mốt lên tám mươi hai phần trăm. Tôi muốn tự kiểm tra kết quả này trong cách dùng hằng ngày.

## Cảnh 4: Thí nghiệm (1:22–2:00)
**Hình:** Hai thẻ: "Graphify (chính nó) · ~106k dòng Python · dựng graph 40s" và "ERPNext · ~573k dòng Python (chưa tính JS) · dựng graph 102s". 5 câu hỏi rút gọn. Hai cột A/B. Chú thích suốt cảnh: "22 lần chạy · chạy tự động · CLAUDE.md đưa vào system prompt · minh họa, không phải benchmark".
**Lời:**
Tôi thử nghiệm trên hai codebase có quy mô rất khác nhau. Thứ nhất là chính mã nguồn của Graphify, khoảng một trăm nghìn dòng, vừa cập nhật hôm nay nên AI khó trả lời bằng trí nhớ. Thứ hai là ERPNext, hơn năm trăm nghìn dòng Python. Năm câu hỏi đều phải lần theo code qua nhiều file. Ví dụ, từ lúc gửi một hóa đơn bán hàng đến lúc ghi sổ cái. Hay liệt kê mọi lớp kế thừa qua ba tầng. Đáp án tôi tự kiểm chứng bằng cách đọc code và phân tích cú pháp. Mỗi câu chạy hai cách: Claude Code bình thường, và Claude Code có đồ thị cùng hướng dẫn và lời nhắc của Graphify.

## Cảnh 5: Kết quả với mô hình lớn (2:00–2:32)
**Hình:** Bảng 5 dòng, hai cột điểm giống hệt (9/9, 2/2, 6/6, 7/7, 22/22). Dưới: "Thời gian tb 49s vs 52s · Chi phí tb $0,30 vs $0,33 (giá API)". Dòng thời gian một lần chạy có đồ thị (q1-B): ô "graphify query" đầu tiên → các ô "Grep / Read"; ô "lời nhắc" xuất hiện một lần, sau ô query.
**Lời:**
Với mô hình lớn, kết quả hòa tuyệt đối. Cả hai cách đều trả lời đúng mọi ý, kể cả câu có bẫy là các lớp trùng tên trong mã JavaScript. Thời gian và chi phí cũng gần như bằng nhau. Điều thú vị là cách Claude làm việc. Khi có đồ thị, nó luôn hỏi đồ thị một hai lần ở đầu, đúng như hướng dẫn. Sau đó nó quay về tìm kiếm văn bản và đọc file như bình thường.

## Cảnh 6: Vì sao? (2:32–3:12)
**Hình:** Output thật của q1-B: `graphify query "…"` → "778 nodes found · showing 62 · TRUNCATED", vài dòng lạc đề (index.ts, test_*.py). Bên cạnh: `graphify explain StockController --all` → 6 lớp con "inherits [EXTRACTED]". Cuối: hai cột "Câu hỏi có sẵn tên hàm, tên lớp" / "Bài đo của họ: mô hình cũ hơn, câu hỏi khác, harness riêng".
**Lời:**
Theo tôi, có hai lý do chính dẫn đến kết quả này. Thứ nhất, truy vấn bằng câu tự nhiên khá nhiễu. Với câu hỏi đầu tiên, đồ thị tìm ra gần tám trăm nút nhưng chỉ hiện khoảng sáu mươi, lẫn cả mã TypeScript và file kiểm thử không liên quan. Ngược lại, hỏi theo đúng tên một lớp thì đồ thị trả lời chính xác, miễn là nhớ thêm cờ all để không bị cắt bớt. Thứ hai, câu hỏi của tôi thường có sẵn tên hàm, tên lớp, nên tìm kiếm văn bản đi thẳng tới đích. Cả hai cách đều đạt điểm tối đa, không còn chỗ cho đồ thị cải thiện. Bài đo của Graphify dùng mô hình cũ hơn và câu hỏi khác, nên hai kết quả không mâu thuẫn.

## Cảnh 7: Mô hình nhỏ (3:12–3:46)
**Hình:** Bảng Haiku (4 câu, mỗi ô 1 lần chạy): A 9/9, 2/2, 7/7, 22/22 · B 8/9, 2/2, 7/7, 22/22. Thẻ: "$0,017 vs $0,33 mỗi câu (cùng 4 câu, không đồ thị, giá API) · ~19 lần".
**Lời:**
Vậy đồ thị có giúp mô hình nhỏ đỡ lạc hơn không? Tôi chạy lại bốn câu bằng Haiku, mô hình nhỏ và rẻ nhất, mỗi cách một lần. Khi có đồ thị, Haiku hỏi đồ thị nhiều hơn, nhưng điểm không tăng, còn thiếu một ý ở một câu. Và đây là điều tôi không ngờ nhất. Không có đồ thị, Haiku vẫn trả lời đúng mọi ý, với chi phí theo giá API rẻ hơn khoảng mười chín lần. Mỗi câu chỉ chạy một lần, nên hãy coi đây là tín hiệu, chưa phải kết luận.

## Cảnh 8: Dùng Graphify thế nào cho đáng (3:46–4:32)
**Hình:** Terminal:
```
uv tool install graphifyy        # hai chữ y
graphify update .                # dựng phần code, không cần API key
echo "tests/" >> .graphifyignore # bỏ thư mục kiểm thử khỏi đồ thị
graphify explain "StockController" --all
graphify path "SalesInvoice" "make_entry"
```
Output thật của `path`: SalesInvoice → .make_gl_entries() → make_reverse_gl_entries() → make_entry() (đi qua nhánh hủy). Rồi ảnh graph.html. Khung "Chưa đo: chế độ --strict · MCP server · phiên dài nhiều câu hỏi".
**Lời:**
Nếu dùng Graphify, đây là cách tôi sẽ làm. Cài đúng gói có hai chữ y, dựng đồ thị cho phần mã nguồn, và bỏ thư mục kiểm thử ra ngoài cho đỡ nhiễu. Khi hỏi, hãy dùng giải thích và tìm đường theo tên chính xác thay vì câu tự nhiên. Nhưng hãy đọc kỹ kết quả. Đường ngắn nhất từ hóa đơn đến hàm ghi sổ lại đi qua nhánh hủy chứng từ, không phải nhánh gửi hóa đơn. Trang đồ thị trực quan rất hữu ích cho người mới vào dự án. Tôi chưa đo chế độ bắt buộc dùng đồ thị, cũng chưa đo phiên làm việc dài với nhiều câu hỏi.

## Cảnh 9: Kết (4:32–4:50)
**Hình:** Dòng chữ lớn; chú thích: "22 lần chạy · 2 codebase · 5 câu hỏi · graphify 0.9.115 · minh họa, không phải benchmark".
**Lời:**
Đừng tin số sao, cũng đừng tin bài đo, kể cả bài đo của tôi. Dựng đồ thị cho phần mã nguồn chỉ mất một đến hai phút và không tốn tiền, nên hãy tự thử trên chính codebase của bạn.

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
| S26 | ét hai mươi sáu |
| TypeScript | Tai-sờ-cờ-ríp |
| JavaScript | Gia-va-sờ-cờ-ríp |
| codebase | cốt-bết |
| code | cốt |
| file | phai |
| AI | ây-ai |
| all | o |
