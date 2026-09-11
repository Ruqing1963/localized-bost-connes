#!/bin/bash
# Compile every paper in the repository (3 passes each) and summarise the logs.
ROOT=${1:-/home/claude/work/repo}
cd "$ROOT" || exit 1
printf "%-45s %6s %6s %6s %6s %6s\n" "paper" "errors" "warn" "over" "under" "pages"
for f in paper/master_bost_connes_paper.tex papers/*/*.tex; do
  d=$(dirname "$f"); b=$(basename "$f" .tex)
  ( cd "$d" && for i in 1 2 3; do pdflatex -interaction=nonstopmode "$b.tex" >/dev/null 2>&1; done )
  log="$d/$b.log"
  err=$(grep -c -E "^!" "$log")
  warn=$(grep -c -E "Warning" "$log")
  over=$(grep -c -E "^Overfull" "$log")
  under=$(grep -c -E "^Underfull" "$log")
  pages=$(pdfinfo "$d/$b.pdf" 2>/dev/null | awk '/Pages/{print $2}')
  printf "%-45s %6s %6s %6s %6s %6s\n" "$b" "$err" "$warn" "$over" "$under" "$pages"
done
