"""Tóm tắt các lượt chạy A/B: thời gian, chi phí tham chiếu, số dòng code/test, kết quả pytest.

Dùng: python summarize_runs.py <runs_dir> [name_prefix]
"Dòng code" = dòng '+' không trống, ngoài thư mục tests/ (cách đếm dùng trong video 01).
"""
import glob, json, os, re, sys

runs, prefix = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else "")
for j in sorted(glob.glob(os.path.join(runs, f"{prefix}*.json"))):
    b = j[:-5]
    try:
        d = json.load(open(j))
    except Exception as e:
        print(os.path.basename(b), "LỖI đọc json:", e); continue
    diff = open(b + ".diff").read() if os.path.exists(b + ".diff") else ""
    code = tests_l = new_tests = 0; files = set(); in_test = False
    for line in diff.splitlines():
        if line.startswith("diff --git"):
            path = line.split()[2][2:]; files.add(path); in_test = path.startswith("tests/")
        elif line.startswith("+") and not line.startswith("+++") and line[1:].strip():
            if in_test:
                tests_l += 1; new_tests += bool(re.match(r"\+\s*def test_", line))
            else:
                code += 1
    t = open(b + ".tests").read().strip().splitlines()[-1] if os.path.exists(b + ".tests") else "?"
    secs = open(b + ".secs").read().strip() if os.path.exists(b + ".secs") else "?"
    print(f"{os.path.basename(b):28} {secs:>4}s  ${d.get('total_cost_usd', 0):.2f}  files={len(files)}  "
          f"code={code}  test_lines={tests_l}  new_tests={new_tests}  pytest: {t}")
