# Thang chấm (đáp án xác minh bằng đọc code + AST, commit graphify 0546b86f)

Điểm = (ý đúng + 0,5 × ý một phần) / tổng ý. Ý sai nghiêm trọng (bịa hàm/file không tồn tại, nhận nhầm lệnh bị ảnh hưởng) ghi riêng cột "sai".

## Q1: `graphify update .` → graph.json (9 ý)
1. Entry `graphify.__main__:main` (pyproject `[project.scripts]`)
2. `_run_cli` → `cli.dispatch_command` nhánh `cmd == "update"` (graphify/cli.py ~L3512)
3. `watch._rebuild_code(watch_path, incremental=True, block_on_lock=True)` (graphify/watch.py L2338)
4. Khóa `_rebuild_lock`
5. `extract.extract(...)` (AST/tree-sitter)
6. `build.build_from_json` → NetworkX graph
7. `cluster.cluster` (communities)
8. `report.generate` (nội dung GRAPH_REPORT.md)
9. `export.to_json` ghi ra file tạm rồi `os_replace_with_fallback` thay atomic thành graph.json
(Bonus, không tính điểm: `detect.save_manifest`, `write_text_atomic` cho report.)

## Q2: sửa `_weakest_shortest_path` ảnh hưởng gì (2 ý + kiểm tra dương tính giả)
1. CLI `graphify path A B`: `cli.dispatch_command` nhánh `cmd == "path"` (cli.py ~L2571) gọi trực tiếp `_weakest_shortest_path` (import từ serve)
2. MCP tool `shortest_path`: `_tool_shortest_path` → `_shortest_path_text` (serve.py L2739) → `_weakest_shortest_path` (L2781)
Dương tính giả (mỗi cái trừ 0,5 ý, tối thiểu 0): `graphify global path` (chỉ in đường dẫn global graph), `explain`, `query`, `get_neighbors`, `get_node`, `affected`...

## Q3: chọn đường khi nhiều đường ngắn nhất bằng nhau (6 ý)
1. `_tool_shortest_path` → `_shortest_path_text` trong graphify/serve.py
2. `_weakest_shortest_path` liệt kê `nx.all_shortest_paths` (networkx)
3. Giới hạn `_MAX_SHORTEST_PATHS` = 256 đường
4. Tiêu chí 1: ít đi qua "hub không có source_file" nhất (`_path_hub_penalty`: stub import stdlib/thư viện ngoài)
5. Tiêu chí 2: so cạnh yếu nhất (`_path_confidence_key` / `_path_weakest`), chọn đường thận trọng nhất (weakest-first, đường không có bằng chứng confidence xếp thấp nhất)
6. Mặc định có hướng (caller→callee); tham số `undirected` / `_path_search_graph`; điểm đầu cuối resolve qua `_resolve_path_endpoint`

## E1 (ERPNext): submit Sales Invoice → GL Entry (7 ý)
1. `SalesInvoice.on_submit` (accounts/doctype/sales_invoice/sales_invoice.py ~L452) gọi `self.make_gl_entries()`
2. `SalesInvoice.make_gl_entries` (~L1148) → `self.get_gl_entries()` (~L1188) dựng gl_map
3. → `erpnext.accounts.general_ledger.make_gl_entries(gl_entries, update_outstanding=..., merge_entries=False)`
4. Các bước kiểm tra trong đó: BudgetValidation / `make_acc_dimensions_offsetting_entry` / `validate_accounting_period` / `validate_disabled_accounts` (≥2 cái = đủ)
5. `process_gl_map`
6. `create_payment_ledger_entry` (Payment Ledger Entry)
7. `save_entries` → `make_entry` → `frappe.new_doc("GL Entry")` … `gle.submit()`

## E2 (ERPNext): class kế thừa StockController (22 class, không tính test/patches)
Độ 1: AssetCapitalization, SellingController, SerialNo, StockEntry, StockReconciliation, SubcontractingController
Độ 2: BuyingController, DeliveryNote, Lead, Quotation, SalesInvoice, SalesOrder, SubcontractingInwardOrder, SubcontractingOrder, SubcontractingReceipt
Độ 3: MaterialRequest, POSInvoice, PurchaseInvoice, PurchaseOrder, PurchaseReceipt, RequestforQuotation, SupplierQuotation
Điểm = recall (tìm đúng / 22). Ghi riêng dương tính giả (vd. class JS trùng tên trong public/js).
