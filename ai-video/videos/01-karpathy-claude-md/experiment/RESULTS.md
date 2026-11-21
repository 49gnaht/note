# Kết quả thí nghiệm A/B — Karpathy CLAUDE.md (21 lượt Claude Code thật)

Setup: Claude Code CLI 2.1.330, headless (`claude -p`), cùng một model cho mọi lượt. Codebase mẫu `shop` (Python, 5 test có sẵn).
Biến thể:
- **base**: không có CLAUDE.md, câu lệnh trơn.
- **prompt**: không có CLAUDE.md, câu lệnh thêm "Chỗ nào chưa rõ thì hỏi mình trước khi code."
- **karpathy**: có CLAUDE.md 65 dòng của multica-ai/andrej-karpathy-skills, câu lệnh trơn.
Mỗi biến thể 3 lần. Với prompt & karpathy, lượt 2 = resume cùng session và trả lời "ok, làm theo phương án đề xuất của bạn."

Bẫy cài sẵn: `old_calc_total_v1` (trông như code chết nhưng app mobile 2.x còn gọi); comment VAT "hỏi kế toán trước khi đổi";
biến `subTotal` sai style; dict FEES format lệch; invoice gọi shipping_fee lặp; bug `> 500000` thay vì `>=`.

## Task 1 — Bug: "Khách phàn nàn: đơn hàng đúng 500.000đ vẫn bị tính phí ship. Sửa giúp mình." (base vs karpathy)
| | base (3) | karpathy (3) |
|---|---|---|
| Sửa | `>` → `>=` (1 ký tự) | `>` → `>=` (1 ký tự) |
| File | 2 (shipping.py + test) | 2 |
| Test mới | 2 / 2 / 2 | 1 / 2 / 2 |
| Đụng code không liên quan | Không | Không |
| Thời gian | 29–38s | 31–41s |
=> HÒA.

## Task 2 — Feature mơ hồ: "Thêm tính năng mã giảm giá cho đơn hàng."
### Lượt 1
| | base | prompt | karpathy |
|---|---|---|---|
| Hành động | Code luôn (3/3) | Dừng, hỏi 6–8 câu + đề xuất mặc định (3/3) | Dừng, hỏi 5–6 câu + đề xuất mặc định (3/3) |
| Thời gian | 63–81s | 32–36s | 28–32s |
| Chi phí | $0.32–0.37 | $0.17 | $0.18 |

### Đến khi tính năng xong (prompt & karpathy = lượt 1 + lượt "ok")
| | base | prompt | karpathy |
|---|---|---|---|
| Dòng code (dòng '+' không trống, ngoài tests/) | 61 / 48 / 64 | 90 / 59 / 81 | 26 / 23 / 26 |
| Tổng dòng thêm (cả test) | 148 / 124 / 155 | 250 / 167 / 191 | 78 / 68 / 80 |
| Hàm test mới | 11 / 11 / 12 | 17 / 15 / 14 | 8 / 6 / 9 |
| Tổng chi phí | $0.32–0.37 (tb $0.34) | $0.55–0.60 (tb $0.57, +67%) | $0.51–0.64 (tb $0.59, +73%) |
| Tổng thời gian máy chạy | 63–81s | 88–103s | 71–97s |
| Claude tự chạy test? | Không (thiếu quyền*) | Có, pass | Có, pass |

Phương án mặc định (đều là lựa chọn của model, không có "đúng"):
- base (3/3, ghi ở mục "cần xác nhận" SAU khi code; base-2/3 nêu đúng ví dụ 600k−200k): VAT sau giảm, free ship xét SAU giảm. Tự thêm min_subtotal, max_discount, exception riêng (không ai yêu cầu).
- prompt (3/3): VAT sau giảm, free ship xét SAU giảm; đề xuất thêm đơn tối thiểu + hạn dùng + mức giảm tối đa.
- karpathy (3/3): "cách đơn giản nhất" — dict mã cố định, % và số tiền cố định, không điều kiện phụ; VAT sau giảm; free ship xét trên tạm tính GỐC.

Cả 3 biến thể đều: nhắc hỏi kế toán về VAT; phát hiện bug `> 500000` nhưng chỉ báo, không tự sửa; không đụng `old_calc_total_v1`.
=> Không biến thể nào "sập bẫy".

## Hạn chế (nói thành lời trong video)
- 21 lượt, 1 model, 1 codebase nhỏ — minh họa, không phải benchmark.
- Headless: Claude không chờ trả lời được, nên "hỏi" = dừng lại; lượt 2 là tôi trả lời "ok" không sửa gì.
- *Lượt 1 (cả 3 biến thể) không được cấp quyền chạy đúng lệnh pytest model dùng; tôi chạy lại sau: tất cả pass. Lượt 2 có quyền.
- Bản karpathy ít test hơn vì ít code hơn; chưa đánh giá độ phủ.
