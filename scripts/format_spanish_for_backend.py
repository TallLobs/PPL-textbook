#!/usr/bin/env python3
"""
WingWing PPL Textbook - Format Spanish JSON for Backend

Transforms the raw Spanish JSON files into backend-ready rows that
match the exact schema of the textbook_content Supabase table:

  title        - Spanish title (extracted from first # heading)
  slug         - slugified Spanish title + "-es"
  chapter      - integer
  section      - integer (A=1, B=2, C=3, D=4, E=5)
  path         - public/content/es/chapters/{folder}/{file}.md
  content      - raw markdown without YAML frontmatter
  metadata     - {unit_title (ES), faa_sources, wingwing_unit, wingwing_chapter, estimated_read_time}
  language     - "es"

Output: output/json-es-backend/{chapter_folder}_{filename}.json
"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
JSON_ES_DIR  = PROJECT_ROOT / "output" / "json-es"
OUT_DIR      = PROJECT_ROOT / "output" / "json-es-backend"

UNIT_LETTER_TO_INT = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-")


def strip_frontmatter(markdown):
    """Remove YAML frontmatter block."""
    if markdown.startswith("---"):
        end = markdown.find("---", 3)
        if end != -1:
            return markdown[end + 3:].lstrip("\n")
    return markdown


def extract_spanish_title(content):
    """Extract the first # heading, stripping 'Unit X:' / 'Unidad X:' prefix."""
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("# "):
            title = line[2:].strip()
            # Strip "Unit A:", "Unidad B:", "Unit C:", etc.
            title = re.sub(r"^(Unit|Unidad)\s+[A-E]\s*:\s*", "", title, flags=re.IGNORECASE)
            return title.strip()
    return None


def transform(json_path):
    with open(json_path, encoding="utf-8") as f:
        data = json.load(f)

    chapter_num    = data["chapter_num"]
    unit_letter    = data["unit_letter"].upper()
    faa_sources    = data.get("faa_sources", [])
    read_time      = data.get("estimated_read_time", 0)
    chapter_folder = data["chapter_folder"]
    filename       = data["filename"]

    # Strip YAML frontmatter — content is now pure Spanish markdown
    content = strip_frontmatter(data["content_markdown"])

    # Extract Spanish title from the first # heading
    spanish_title = extract_spanish_title(content)
    if not spanish_title:
        # Fallback: use English title with note
        spanish_title = data["unit_title"]
        print(f"  ⚠ No Spanish title found in {json_path.name}, using English: {spanish_title}")

    # Build backend row
    slug = slugify(spanish_title) + "-es"
    path = f"public/content/es/chapters/{chapter_folder}/{filename}"

    row = {
        "title":    spanish_title,
        "slug":     slug,
        "chapter":  chapter_num,
        "section":  UNIT_LETTER_TO_INT.get(unit_letter, 1),
        "path":     path,
        "content":  content,
        "language": "es",
        "metadata": {
            "unit_title":          spanish_title,
            "faa_sources":         faa_sources,
            "wingwing_unit":       unit_letter,
            "wingwing_chapter":    chapter_num,
            "estimated_read_time": read_time,
        }
    }

    return row


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    json_files = sorted(JSON_ES_DIR.glob("*.json"))
    print(f"\nFormatting {len(json_files)} Spanish units for backend...\n")

    for json_path in json_files:
        row = transform(json_path)
        out_path = OUT_DIR / json_path.name
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(row, f, ensure_ascii=False, indent=2)

        content_chars = len(row["content"])
        print(f"  ✓ ch{row['chapter']} s{row['section']}  {row['title']:<45}  {content_chars:,} chars  →  {json_path.name}")

    print(f"\n{'='*60}")
    print(f"Done! {len(json_files)} backend-ready Spanish JSON files")
    print(f"Output: {OUT_DIR}")
    print(f"{'='*60}\n")

    # Spot-check one file
    sample_path = OUT_DIR / sorted(OUT_DIR.glob("*.json"))[0].name
    with open(sample_path) as f:
        sample = json.load(f)
    print("Sample row keys:    ", list(sample.keys()))
    print("Sample title:       ", sample["title"])
    print("Sample slug:        ", sample["slug"])
    print("Sample path:        ", sample["path"])
    print("Sample metadata:    ", sample["metadata"])
    print("Content preview:    ", sample["content"][:120].replace("\n", " "))


if __name__ == "__main__":
    main()
