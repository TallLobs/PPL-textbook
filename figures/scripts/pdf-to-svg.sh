#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <input.pdf> <output-dir>"
  exit 1
fi

INPUT_PDF="$1"
OUT_DIR="$2"
SVG_DIR="$OUT_DIR/svg"
RAW_DIR="$OUT_DIR/raw-svg"

if [ ! -f "$INPUT_PDF" ]; then
  echo "Input file not found: $INPUT_PDF"
  exit 1
fi

if ! command -v pdftocairo >/dev/null 2>&1; then
  echo "Missing dependency: pdftocairo"
  echo "Install with: brew install poppler"
  exit 1
fi

mkdir -p "$SVG_DIR" "$RAW_DIR"
shopt -s nullglob

# Generate one SVG per page from the PDF (named by page number).
TOTAL_PAGES="$(pdfinfo "$INPUT_PDF" | awk '/^Pages:/ {print $2}')"
if [ -z "${TOTAL_PAGES:-}" ]; then
  echo "Unable to detect page count with pdfinfo."
  exit 1
fi

for page in $(seq 1 "$TOTAL_PAGES"); do
  page_name="$(printf '%03d' "$page")"
  pdftocairo -f "$page" -l "$page" -svg "$INPUT_PDF" "$RAW_DIR/$page_name.svg"
done

if command -v svgo >/dev/null 2>&1; then
  raw_svgs=("$RAW_DIR"/*.svg)
  if [ "${#raw_svgs[@]}" -eq 0 ]; then
    echo "No SVG files generated in $RAW_DIR"
    exit 1
  fi
  for f in "${raw_svgs[@]}"; do
    base="$(basename "$f")"
    svgo --input "$f" --output "$SVG_DIR/$base" >/dev/null
  done
else
  echo "svgo not found. Copying unoptimized SVGs."
  echo "Install optimization tool with: npm i -g svgo"
  raw_svgs=("$RAW_DIR"/*.svg)
  if [ "${#raw_svgs[@]}" -eq 0 ]; then
    echo "No SVG files generated in $RAW_DIR"
    exit 1
  fi
  cp "${raw_svgs[@]}" "$SVG_DIR/"
fi

echo "SVG export complete: $SVG_DIR"
