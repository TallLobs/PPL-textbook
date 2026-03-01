#!/usr/bin/env python3
"""
WingWing PPL Textbook - Backend Export Script

Generates:
1. index.csv  — manifest of all units (both languages) with metadata
2. output/json-en/*.json — English unit JSON files
3. output/json-es/*.json — Spanish unit JSON files

Each JSON file contains:
  - All YAML frontmatter fields
  - language code ("en" or "es")
  - full markdown content
  - parsed sections list
  - word_count
"""

import json
import csv
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
CHAPTERS_EN = PROJECT_ROOT / "output" / "chapters"
CHAPTERS_ES = PROJECT_ROOT / "output" / "chapters-es"
JSON_EN_DIR = PROJECT_ROOT / "output" / "json-en"
JSON_ES_DIR = PROJECT_ROOT / "output" / "json-es"
INDEX_CSV   = PROJECT_ROOT / "output" / "index.csv"


def parse_frontmatter(content):
    """Extract YAML frontmatter as a dict and return (meta, body)."""
    meta = {}
    body = content
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            fm_block = content[4:end].strip()
            body = content[end + 3:].lstrip("\n")
            for line in fm_block.splitlines():
                if ":" in line:
                    key, _, val = line.partition(":")
                    key = key.strip()
                    val = val.strip()
                    # Parse lists like ['item1', 'item2']
                    if val.startswith("[") and val.endswith("]"):
                        inner = val[1:-1]
                        items = [i.strip().strip("'\"") for i in inner.split(",") if i.strip()]
                        meta[key] = items
                    # Parse quoted strings
                    elif val.startswith(("'", '"')) and val.endswith(("'", '"')):
                        meta[key] = val[1:-1]
                    # Parse integers
                    elif val.isdigit():
                        meta[key] = int(val)
                    else:
                        meta[key] = val
    return meta, body


def parse_sections(body):
    """Extract section titles and their content."""
    sections = []
    current_title = None
    current_lines = []

    for line in body.splitlines():
        if line.startswith("## "):
            if current_title is not None:
                sections.append({
                    "title": current_title,
                    "content": "\n".join(current_lines).strip()
                })
            current_title = line[3:].strip()
            current_lines = []
        else:
            if current_title is not None:
                current_lines.append(line)

    if current_title is not None:
        sections.append({
            "title": current_title,
            "content": "\n".join(current_lines).strip()
        })

    return sections


def process_unit(md_path, language, chapter_dir_name):
    """Parse a markdown unit and return a structured dict."""
    content = md_path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(content)
    sections = parse_sections(body)
    word_count = len(content.split())

    # Build the JSON record
    record = {
        "language": language,
        "chapter_num": meta.get("wingwing_chapter", 0),
        "unit_letter": meta.get("wingwing_unit", ""),
        "unit_title": meta.get("unit_title", md_path.stem),
        "faa_sources": meta.get("faa_sources", []),
        "estimated_read_time": meta.get("estimated_read_time", 0),
        "chapter_folder": chapter_dir_name,
        "filename": md_path.name,
        "word_count": word_count,
        "section_count": len(sections),
        "content_markdown": content,
        "sections": sections
    }
    return record


def slugify(text):
    """Simple slugify for filenames."""
    return re.sub(r"[^a-z0-9-]", "-", text.lower()).strip("-")


def export_all():
    JSON_EN_DIR.mkdir(parents=True, exist_ok=True)
    JSON_ES_DIR.mkdir(parents=True, exist_ok=True)

    index_rows = []
    total_en = 0
    total_es = 0

    for language, src_dir, json_dir in [
        ("en", CHAPTERS_EN, JSON_EN_DIR),
        ("es", CHAPTERS_ES, JSON_ES_DIR),
    ]:
        for chapter_dir in sorted(src_dir.iterdir()):
            if not chapter_dir.is_dir():
                continue
            for md_file in sorted(chapter_dir.glob("unit-*.md")):
                record = process_unit(md_file, language, chapter_dir.name)

                # Write JSON
                json_filename = f"{chapter_dir.name}_{md_file.stem}.json"
                json_path = json_dir / json_filename
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(record, f, ensure_ascii=False, indent=2)

                # Add to index
                index_rows.append({
                    "language":            language,
                    "chapter_num":         record["chapter_num"],
                    "unit_letter":         record["unit_letter"],
                    "unit_title":          record["unit_title"],
                    "chapter_folder":      record["chapter_folder"],
                    "filename":            record["filename"],
                    "json_file":           json_filename,
                    "word_count":          record["word_count"],
                    "section_count":       record["section_count"],
                    "estimated_read_time": record["estimated_read_time"],
                    "faa_sources":         "|".join(record["faa_sources"]),
                })

                if language == "en":
                    total_en += 1
                else:
                    total_es += 1

                print(f"  [{language}] {chapter_dir.name}/{md_file.name} → {json_filename}")

    # Write CSV index
    fieldnames = [
        "language", "chapter_num", "unit_letter", "unit_title",
        "chapter_folder", "filename", "json_file",
        "word_count", "section_count", "estimated_read_time", "faa_sources"
    ]
    with open(INDEX_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(index_rows)

    print(f"\n{'='*60}")
    print(f"Export complete!")
    print(f"  English JSON files : {total_en}  →  {JSON_EN_DIR}")
    print(f"  Spanish JSON files : {total_es}  →  {JSON_ES_DIR}")
    print(f"  CSV index          : {INDEX_CSV}")
    print(f"  Total rows in CSV  : {len(index_rows)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    print("WingWing PPL Textbook — Backend Export\n")
    export_all()
