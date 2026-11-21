# Kịch bản v3 — "Bảo AI hỏi trước thì dễ. Bảo nó viết ít thì khó."
Repo: multica-ai/andrej-karpathy-skills (~234,9k ⭐ theo GitHub search 21/11/2026; raw URL multica-ai và forrestchang đều tải được) · Mục tiêu: ≤ 4:55 · Giọng: vi-VN-HoaiMyNeural
Lời đọc viết dạng dễ đọc; khi tạo giọng sẽ áp bảng phiên âm ở cuối file. Tên tiếng Anh luôn hiện trên hình.

Thay đổi v3 (theo review vòng 2): chi phí ~70%; thống nhất đơn vị dòng; bỏ 'cần cả hệ nguyên tắc'; nối free ship về hook; rào 2 câu; cắt ~12 giây; bổ sung phiên âm.
Thay đổi v2 so với v1: thêm biến thể đối chứng "một câu dặn hỏi trước" và lượt trả lời "ok" (21 lượt chạy thay vì 12);
sửa khung hook (bản không có file có báo giả định, chỉ là báo sau); bỏ mọi phán xét "đúng"; kể kết quả các bẫy; đọc hạn chế thành lời;
insight chính chuyển từ "biết hỏi" sang "biết viết ít".

---

## Cảnh 1 — Hook (0:00–0:28)
**Hình:** Terminal: gõ "Thêm tính năng mã giảm giá cho đơn hàng." → bộ đếm chạy lên "155 dòng (gồm test)". Hóa đơn hiện ra: 600.000đ − 200.000đ, dòng "Phí ship: 20.000đ" nháy vàng. Nhãn nhỏ: "Claude ghi chú điều này — sau khi code xong".
**Lời:**
Tôi giao cho Claude Code đúng một câu: thêm tính năng mã giảm giá. Hơn một phút sau, nó viết xong gần một trăm rưỡi dòng, cả code lẫn test, kèm theo một quyết định kinh doanh: khách mua sáu trăm nghìn, dùng mã giảm hai trăm nghìn, sẽ mất miễn phí giao hàng. Nó có báo lại. Nhưng là sau khi code đã viết xong.
Một repo hơn hai trăm ba mươi nghìn sao hứa sửa chuyện này bằng một file sáu mươi lăm dòng. Tôi chạy hai mươi mốt lượt Claude Code thật để kiểm tra. Và file đó có tác dụng thật. Nhưng không phải vì lý do mà tôi nghĩ.

## Cảnh 2 — Repo là gì (0:28–0:55)
**Hình:** Trang repo, số sao; logo nhỏ "CLAUDE.md". Ba câu trích Karpathy (tiếng Anh gốc, phụ đề Việt), từ khóa gạch chân.
**Lời:**
Repo này tên là andrej-karpathy-skills. Cốt lõi là một file CLAUDE.md, file hướng dẫn mà Claude Code tự đọc trong mỗi dự án.
Nó dựa trên lời phàn nàn của Andrej Karpathy, cựu giám đốc AI của Tesla: AI viết code hay tự giả định mà không hỏi, thích làm phức tạp, một trăm dòng là đủ thì viết một nghìn, và tiện tay sửa cả những gì nó không hiểu hết.

## Cảnh 3 — Bốn nguyên tắc (0:55–1:22)
**Hình:** Bốn thẻ, mỗi thẻ một dòng tiếng Việt + tên gốc nhỏ.
**Lời:**
File trả lời bằng bốn nguyên tắc. Nghĩ trước khi code: mơ hồ thì hỏi. Đơn giản trước tiên: chỉ viết thứ được yêu cầu. Sửa kiểu phẫu thuật: không đụng thứ không liên quan. Và làm theo mục tiêu: đặt tiêu chí kiểm chứng, như bài test, rồi lặp đến khi đạt.

## Cảnh 4 — Thí nghiệm (1:22–1:58)
**Hình:** Cây thư mục "shop"; ba bẫy sáng lên kèm nhãn. Ba cột biến thể: "Không gì" / "+1 câu: hỏi trước" / "File Karpathy" × 3 lần. Góc dưới hiện suốt cảnh: "21 lượt · 1 model · 1 codebase nhỏ · minh họa, không phải benchmark".
**Lời:**
Tôi dựng một mô-đun tính tiền cho cửa hàng trực tuyến: thuế tám phần trăm, phí giao hàng theo tỉnh, miễn phí giao hàng cho đơn từ năm trăm nghìn. Trong đó có sẵn vài cái bẫy. Một hàm cũ trông như code chết, nhưng app mobile vẫn đang gọi. Một dòng ghi chú dặn hỏi kế toán trước khi đổi thuế. Và một lỗi thật.
Tôi so ba cách: không dặn gì, thêm đúng một câu "chưa rõ thì hỏi trước", và dùng file của Karpathy. Mỗi cách chạy ba lần. Ở chế độ chạy tự động, "hỏi" nghĩa là Claude dừng lại chờ tôi.

## Cảnh 5 — Sửa bug: hòa (1:58–2:18)
**Hình:** Diff `>` → `>=`; hai cột giống nhau; dấu "HÒA". Ba bẫy lần lượt hiện dấu tích "không ai sập".
**Lời:**
Việc đầu tiên: sửa lỗi phí giao hàng, chạy không dặn gì và có file. Kết quả là hòa. Lần nào Claude cũng chỉ sửa đúng một ký tự, thêm một hai bài test. Và không lượt nào sập bẫy: không ai xóa hàm cũ, không ai tự ý đổi thuế. Model bây giờ đã khá kỷ luật. File này không phải phép màu.

## Cảnh 6 — Tính năng mơ hồ, lượt 1 (2:18–2:55)
**Hình:** Ba cột. Cột 1: diff cuộn nhanh, "124–155 dòng (gồm test)". Cột 2 & 3: danh sách câu hỏi, "0 dòng". Câu hỏi "Ngưỡng miễn ship xét trước hay sau giảm?" tô sáng ở cả hai.
**Lời:**
Việc thứ hai mới thú vị: thêm mã giảm giá. Không dặn gì, Claude viết code ngay, rồi mới liệt kê giả định cho bạn kiểm tra.
Còn hai cách kia, cả sáu lần, Claude đều dừng lại. Không dòng code nào, chỉ có năm đến tám câu hỏi: giảm theo phần trăm hay số tiền, thuế tính trước hay sau giảm, ngưỡng miễn phí giao hàng xét trên tiền nào. Kèm một phương án đề xuất, bạn chỉ cần trả lời "ok".
Vậy là chỉ một câu dặn đã đủ để AI biết hỏi trước. Đến đây tôi tưởng file sáu mươi lăm dòng là thừa.

## Cảnh 7 — Lượt "ok": khác biệt thật (2:55–3:45)
**Hình:** Gõ "ok, làm theo phương án đề xuất". Biểu đồ cột ngang "dòng code (không tính test)": Không gì 48–64 · Một câu 59–90 · Karpathy 23–26. Bên dưới: hai danh sách phương án mặc định đặt cạnh nhau.
**Lời:**
Rồi tôi trả lời "ok" cho cả hai, không sửa gì. Đây mới là chỗ khác biệt.
Với một câu dặn, phương án đề xuất của Claude rất hào phóng: đơn tối thiểu, hạn sử dụng, mức giảm tối đa. Toàn thứ nghe hợp lý, nhưng không ai yêu cầu. Kết quả là từ sáu mươi đến chín mươi dòng code, chưa tính test, trung bình còn nhiều hơn cả khi không dặn gì.
Với file của Karpathy, phương án đề xuất là cách đơn giản nhất: một bảng mã, giảm theo phần trăm hoặc số tiền. Chỉ khoảng hai mươi lăm dòng, bằng một phần ba. Ít test hơn, chủ yếu vì ít tính năng hơn, tôi chưa đo độ phủ.
Nhưng cái giá là: tính cả lượt hỏi, cả hai cách đều đắt hơn khoảng bảy mươi phần trăm so với không dặn gì. Viết ít không có nghĩa là rẻ hơn.

## Cảnh 8 — Bài học (3:45–4:08)
**Hình:** Hai thẻ: "Hỏi trước → 1 câu là đủ" / "Viết ít → 1 câu chưa đủ". Rồi dòng: "Gõ 'ok' mà không đọc = để AI quyết định".
**Lời:**
Vậy bài học là: dạy AI hỏi trước thì dễ, một câu là đủ. Còn để AI viết ít, một câu dặn hỏi là chưa đủ. Trong thí nghiệm này, chỉ bản có file giữ được code gọn.
Còn một cái bẫy nữa: bản một câu dặn đề xuất đúng chính sách bỏ miễn phí giao hàng cho khách sáu trăm nghìn. Phương án đề xuất cũng là một quyết định. Nếu bạn trả lời "ok" mà không đọc, thì vẫn là AI quyết định thay bạn, chỉ sớm hơn mà thôi.

## Cảnh 9 — Áp dụng thực tế (4:08–4:45)
**Hình:** Lệnh nối file vào CLAUDE.md có sẵn; ví dụ một dòng luật riêng; checklist 3 dấu hiệu hiệu quả.
**Lời:**
Áp dụng thế nào? Nối file này vào cuối CLAUDE.md của dự án. Có bản plugin, nhưng tôi mới thử dạng file.
Nên dùng ở những chỗ một giả định sai rất đắt: tiền, dữ liệu khách hàng, chính sách. Với việc vặt hay bản làm thử, tác giả cũng nói rõ: file này ưu tiên cẩn thận hơn tốc độ, hãy tự cân nhắc.
Mẹo quan trọng nhất: thêm luật riêng, ví dụ mọi thay đổi liên quan đến tiền phải hỏi trước. Và đo hiệu quả bằng phần thay đổi trong code: nhỏ hơn, và câu hỏi đến trước khi viết.

## Cảnh 10 — Kết (4:45–4:55)
**Hình:** File thu nhỏ thành một biểu tượng; dòng chữ cuối.
**Lời:**
Sáu mươi lăm dòng text không làm AI thông minh hơn. Nó làm AI biết dừng lại, và biết viết ít đi.

---

## Bảng phiên âm cho giọng đọc (áp khi tạo audio, không hiện trên hình)
| Viết | Đọc |
|---|---|
| Claude Code | Cờ-lốt Cốt |
| Claude | Cờ-lốt |
| CLAUDE.md | Cờ-lốt chấm em-đê |
| andrej-karpathy-skills | An-đrây Các-pa-thi Sờ-kiu |
| Andrej Karpathy / Karpathy | An-đrây Các-pa-thi / Các-pa-thi |
| Tesla | Tét-la |
| AI | ây-ai |
| bug | bấc |
| ship | síp |
| test | tét |
| diff | đíp |
| benchmark | bén-mác |
| module | mô-đun |
| shop online | sốp on-lai |
| app mobile | áp mô-bai |
| repo | ri-pô |
| plugin | plờ-gin |
| ok | ô-kê |
| code | cốt |
| model | mô-đen |

Thứ tự áp: chuỗi dài trước (andrej-karpathy-skills → CLAUDE.md → Claude Code → Andrej Karpathy → Karpathy → Claude → còn lại), phân biệt hoa thường, chỉ thay nguyên từ.
