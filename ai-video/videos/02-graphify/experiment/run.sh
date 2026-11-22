#!/bin/bash
# usage: run.sh <variant A|B> <q1|q2|q3> <n>
D=/tmp/claude-0/-home-user-note/11178d96-6c29-565c-bc0e-b64ce1d0de62/scratchpad/v02
V=$1; Q=$2; N=$3; R=$D/runs/$Q-$V${MODEL:+-h}-$N; O=$R
PROMPT=$(python3 -c "import json;print(json.load(open('$D/questions.json'))['$Q'])")
ALLOW="Read,Glob,Grep,Bash(graphify *),Bash(grep *),Bash(rg *),Bash(find *),Bash(cat *),Bash(sed *),Bash(head *),Bash(tail *),Bash(ls *),Bash(wc *),Bash(awk *)"
TGT=${TGT:-target}; rm -rf $R; cp -r $D/$TGT $R; cd $R; rm -f AGENTS.md
EXTRA=()
if [ "$V" = B ]; then
  export PATH=$D/gvenv/bin:$PATH
  $D/gvenv/bin/graphify claude install >/dev/null 2>&1
  EXTRA=(--append-system-prompt "$(cat CLAUDE.md)")
else
  rm -rf graphify-out
fi
s=$(date +%s)
timeout 1200 claude -p "$PROMPT" ${MODEL:+--model $MODEL} --output-format json --allowedTools "$ALLOW" "${EXTRA[@]}" > $O.json 2> $O.err
echo $(( $(date +%s) - s )) > $O.secs
