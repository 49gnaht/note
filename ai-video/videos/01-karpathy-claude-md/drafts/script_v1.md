# Kịch bản v1 — "Một file 65 dòng khiến Claude Code biết dừng lại"
Repo: multica-ai/andrej-karpathy-skills (~235k ⭐) · Mục tiêu: ≤ 5:00 · Giọng: vi-VN-HoaiMyNeural

---

## Cảnh 1 — Hook (0:00–0:30)
**Hình:** Terminal gõ đúng một câu "Thêm tính năng mã giảm giá cho đơn hàng." → số dòng code chạy vụt lên ~150, 11 test mới xanh. Đóng băng. Một hóa đơn hiện ra: đơn 600.000đ, mã giảm 200.000đ, dòng "Phí ship: 20.000đ" nháy đỏ.
**Lời:**
Tôi giao cho Claude Code đúng một câu: "Thêm tính năng mã giảm giá". Một phút sau, nó viết gần một trăm rưỡi dòng code, mười một bài test, tất cả đều xanh. Và nó vừa lặng lẽ quyết định rằng khách mua sáu trăm nghìn, dùng mã giảm hai trăm nghìn, sẽ bị mất miễn phí ship.
Không ai trong team quyết định điều đó. Model quyết định.
Lần thứ hai, cùng model, cùng câu lệnh, tôi chỉ thêm một file text sáu mươi lăm dòng. Lần này nó không viết một dòng code nào. Và đó mới là câu trả lời đúng.

## Cảnh 2 — Repo là gì (0:30–1:05)
**Hình:** Trang GitHub repo, số sao 235k đếm lên. Ba câu trích của Karpathy hiện lần lượt, gạch chân từ khóa.
**Lời:**
File đó đến từ repo andrej-karpathy-skills, hơn hai trăm ba mươi nghìn sao trên GitHub. Toàn bộ repo thực chất chỉ là một file CLAUDE.md, viết dựa trên một bài đăng của Andrej Karpathy, người từng dẫn dắt AI ở Tesla và là thành viên sáng lập OpenAI.
Karpathy phàn nàn ba điều về AI viết code. Một: nó tự giả định thay bạn rồi cứ thế chạy, không hỏi lại. Hai: nó thích làm phức tạp, một trăm dòng là đủ thì nó viết một nghìn. Ba: nó tiện tay sửa cả những đoạn code nó không hiểu hết.

## Cảnh 3 — Bốn nguyên tắc (1:05–1:45)
**Hình:** Bốn thẻ lật lần lượt, mỗi thẻ một câu tiếng Việt.
**Lời:**
File CLAUDE.md trả lời bằng bốn nguyên tắc.
Nghĩ trước khi code: nêu rõ giả định, chỗ nào mơ hồ thì dừng lại và hỏi.
Đơn giản trước tiên: chỉ viết đúng thứ được yêu cầu, không thêm tính năng phòng hờ.
Sửa kiểu phẫu thuật: mỗi dòng thay đổi phải truy ngược được về yêu cầu của bạn.
Và làm việc theo mục tiêu: biến yêu cầu thành tiêu chí kiểm chứng được, ví dụ viết test trước, rồi lặp đến khi pass.
Nghe thì hợp lý. Nhưng câu hỏi thật là: với model năm 2026, nó còn tạo ra khác biệt không? Tôi đã thử.

## Cảnh 4 — Thí nghiệm (1:45–2:15)
**Hình:** Cây thư mục codebase "shop". Các "bẫy" sáng lên từng cái kèm nhãn. Sơ đồ 2 task × 2 biến thể × 3 lần = 12 lượt.
**Lời:**
Tôi dựng một codebase nhỏ: module tính tiền cho một shop online, có VAT tám phần trăm, phí ship theo tỉnh, miễn ship cho đơn từ năm trăm nghìn. Và tôi cài sẵn những cái bẫy mà code thật nào cũng có: một hàm cũ trông như code chết nhưng app mobile vẫn đang gọi, một dòng comment dặn "hỏi kế toán trước khi đổi VAT", và một bug thật.
Hai nhiệm vụ: sửa một bug rõ ràng, và thêm một tính năng mơ hồ. Mỗi nhiệm vụ chạy ba lần không có file, ba lần có file. Mười hai lượt, Claude Code thật, không dàn dựng.

## Cảnh 5 — Kết quả 1: sửa bug (2:15–2:40)
**Hình:** Diff một dòng `>` → `>=`, hai cột base / karpathy giống hệt, chữ "HÒA" đóng dấu.
**Lời:**
Nhiệm vụ một: khách phàn nàn đơn đúng năm trăm nghìn vẫn bị tính ship. Kết quả: hòa. Cả sáu lần, Claude sửa đúng một ký tự, thêm một test, không đụng vào thứ gì khác. Nói thẳng: với bug rõ ràng, model bây giờ đã đủ kỷ luật. File này không phải phép màu.

## Cảnh 6 — Kết quả 2: tính năng mơ hồ (2:40–3:40)
**Hình:** Bảng so sánh hiện dần: 155 dòng / 5 file / 70 giây vs 0 dòng / 0 file / 30 giây. Sau đó màn hình chia đôi: trái là diff dài cuộn nhanh, phải là danh sách câu hỏi; câu hỏi về free ship được tô sáng.
**Lời:**
Nhưng với câu "thêm mã giảm giá", khác biệt rất lớn.
Không có file, cả ba lần Claude đều lao vào code ngay: khoảng một trăm năm mươi dòng, năm file, hơn chục test. Code sạch, test pass. Và cả ba lần nó đều tự chọn cùng một chính sách: tính ngưỡng miễn ship trên số tiền sau khi giảm. Công bằng mà nói, nó có ghi chú giả định này ở cuối câu trả lời, nhưng là sau khi đã viết xong một trăm năm mươi dòng.
Có file, cả ba lần Claude dừng lại. Không dòng code nào. Thay vào đó là năm, sáu câu hỏi: giảm theo phần trăm hay số tiền? VAT tính trước hay sau giảm, và nó còn trích lại đúng dòng comment "hỏi kế toán". Ngưỡng miễn ship xét trên tiền nào? Kèm theo một phương án mặc định, bạn chỉ cần gõ "ok".
Thú vị là phương án mặc định đó giữ miễn ship cho khách, ngược với cả ba bản kia. Và nó chỉ tốn một nửa chi phí, nửa thời gian.

## Cảnh 7 — Bài học thật sự (3:40–4:05)
**Hình:** Hai con đường: "Review 150 dòng code" (dài, quanh co) vs "Trả lời 5–6 câu hỏi" (ngắn, thẳng).
**Lời:**
Vậy bài học không phải là code bản nào tốt hơn. Bài học là ai đưa ra quyết định kinh doanh, và vào lúc nào. Trả lời vài câu hỏi mất một phút. Đọc một trăm năm mươi dòng code để tìm ra một quyết định chính sách bị chôn ở bên trong, mất lâu hơn nhiều, nếu bạn còn nhận ra.

## Cảnh 8 — Áp dụng thực tế (4:05–4:40)
**Hình:** Lệnh curl cài đặt; bốn gạch đầu dòng hiện lần lượt; một ví dụ dòng rule tự thêm.
**Lời:**
Áp dụng thế nào? Cài mất ba mươi giây: tải file CLAUDE.md về thư mục dự án, hoặc cài dạng plugin.
Nên dùng cho những dự án mà một giả định sai rất đắt: tiền, dữ liệu khách hàng, chính sách. Nên dùng khi team có nhiều người mới dùng AI, vì nó buộc AI hỏi những câu mà người mới chưa biết để hỏi.
Đừng dùng cho prototype hay script viết nhanh, chính tác giả cũng ghi rõ: file này ưu tiên cẩn thận hơn tốc độ.
Và mẹo quan trọng nhất: thêm luật riêng của bạn. Ví dụ: "mọi thay đổi liên quan đến tiền phải hỏi trước khi code".

## Cảnh 9 — Kết (4:40–4:55)
**Hình:** File CLAUDE.md thu nhỏ còn một biểu tượng; dòng chữ cuối. Chú thích nhỏ góc dưới: "12 lượt chạy · 1 codebase · minh họa, không phải benchmark".
**Lời:**
Sáu mươi lăm dòng text không làm AI thông minh hơn. Nó làm AI biết lúc nào nên dừng lại để hỏi bạn. Và đôi khi, đó chính là thứ đáng giá nhất.
