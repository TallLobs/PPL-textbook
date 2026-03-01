#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <input.pdf> <output-dir> [dpi=220] [quality=80]"
  exit 1
fi

INPUT_PDF="$1"
OUT_DIR="$2"
DPI="${3:-220}"
QUALITY="${4:-80}"
RAW_DIR="$OUT_DIR/raw-png"
WEBP_DIR="$OUT_DIR/pages"

if [ ! -f "$INPUT_PDF" ]; then
  echo "Input file not found: $INPUT_PDF"
  exit 1
fi

for cmd in pdfinfo pdftocairo cwebp; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "Missing dependency: $cmd"
    echo "Install with: brew install poppler webp"
    exit 1
  fi
done

TOTAL_PAGES="$(pdfinfo "$INPUT_PDF" | awk '/^Pages:/ {print $2}')"
if [ -z "${TOTAL_PAGES:-}" ]; then
  echo "Unable to detect page count with pdfinfo"
  exit 1
fi

mkdir -p "$RAW_DIR" "$WEBP_DIR"

for page in $(seq 1 "$TOTAL_PAGES"); do
  page_name="$(printf '%03d' "$page")"
  png_file="$RAW_DIR/$page_name.png"
  webp_file="$WEBP_DIR/$page_name.webp"

  # Render one PDF page to PNG.
  pdftocairo -singlefile -f "$page" -l "$page" -r "$DPI" -png "$INPUT_PDF" "$RAW_DIR/$page_name"

  # Convert PNG to a lightweight WebP page file.
  cwebp -quiet -mt -q "$QUALITY" "$png_file" -o "$webp_file"

done

echo "WebP export complete: $WEBP_DIR"
