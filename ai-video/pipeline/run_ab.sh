#!/bin/bash
# Chạy thí nghiệm A/B bằng Claude Code headless (`claude -p`). Mỗi lượt chạy trong một bản sao riêng của codebase mẫu.
#
# Dùng: run_ab.sh <base_dir> <runs_dir> <name> "<prompt>" [claude_md_file] [n_runs=3]
#   ví dụ: run_ab.sh exp/base exp/runs feature-karpathy "Thêm tính năng mã giảm giá." karpathy/CLAUDE.md 3
# Trả lời tiếp một lượt (resume cùng session):
#   RESUME=1 run_ab.sh exp/base exp/runs feature-karpathy "ok, làm theo phương án đề xuất của bạn."
#   -> đọc session_id từ <name>-<n>.json, ghi kết quả vào <name>-ok-<n>.*
#
# Kết quả mỗi lượt: .json (câu trả lời cuối + chi phí + session_id), .diff (so với base), .tests, .secs
# Lưu ý từ video 01:
#   - Cho phép CẢ `python -m pytest` lẫn `python3 -m pytest`, nếu không model không tự chạy được test.
#   - Codebase base phải là git repo sạch, không có __pycache__ (nếu không diff lẫn file .pyc).
#   - Gói Pro: các lượt chạy trừ vào hạn mức gói, không phát sinh tiền (trừ khi bật extra usage).
set -u
BASE=$(realpath "$1"); RUNS=$(realpath -m "$2"); NAME=$3; PROMPT=$4; CMD=${5:-}; N=${6:-3}
ALLOW="Read,Edit,Write,Glob,Grep,Bash(python3 -m pytest*),Bash(python -m pytest*),Bash(pytest*),Bash(git diff*),Bash(git status*),Bash(ls*)"
mkdir -p "$RUNS"

one() {
  local n=$1 D O SID
  if [ -n "${RESUME:-}" ]; then
    D=$RUNS/$NAME-$n; O=$RUNS/$NAME-ok-$n
    SID=$(python3 -c "import json;print(json.load(open('$D.json'))['session_id'])")
    cd "$D" || return
    local s=$(date +%s)
    timeout 900 claude -p "$PROMPT" --resume "$SID" --output-format json --allowedTools "$ALLOW" > "$O.json" 2> "$O.err"
  else
    D=$RUNS/$NAME-$n; O=$D
    rm -rf "$D"; cp -r "$BASE" "$D"; cd "$D" || return
    [ -d .git ] || { git init -q && git add -A && git -c user.email=x@x -c user.name=x commit -qm base; }
    if [ -n "$CMD" ]; then cp "$CMD" CLAUDE.md && git add CLAUDE.md && git -c user.email=x@x -c user.name=x commit -qm claudemd; fi
    local s=$(date +%s)
    timeout 900 claude -p "$PROMPT" --output-format json --allowedTools "$ALLOW" > "$O.json" 2> "$O.err"
  fi
  echo $(( $(date +%s) - s )) > "$O.secs"
  find . -name __pycache__ -prune -exec rm -rf {} +
  git add -A >/dev/null 2>&1; git diff --cached -- . ':!CLAUDE.md' > "$O.diff"
  python3 -m pytest -q -p no:cacheprovider > "$O.tests" 2>&1
  find . -name __pycache__ -prune -exec rm -rf {} +
}

for n in $(seq 1 "$N"); do one "$n" & done; wait
python3 "$(dirname "$0")/summarize_runs.py" "$RUNS" "$NAME"
