#!/usr/bin/env python3
"""
WingWing PPL Textbook - Parallel Spanish Translation

Translates all remaining English units to Spanish using 2 parallel workers
with staggered starts to respect Anthropic rate limits.
"""

import anthropic
import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
import httpx
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent

# Load environment variables
env_path = PROJECT_ROOT / ".env"
if not load_dotenv(env_path, override=True):
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()

OUTPUT_DIR = PROJECT_ROOT / "output" / "chapters"
OUTPUT_ES_DIR = PROJECT_ROOT / "output" / "chapters-es"

MODEL = "claude-sonnet-4-5-20250929"

SYSTEM_PROMPT = """You are an expert aviation translator specializing in pilot training materials.
You translate English aviation textbook content into neutral Latin American Spanish.

CRITICAL RULES:
1. Translate ALL body text into clear, professional Latin American Spanish
2. Keep the following in ENGLISH (do not translate):
   - YAML frontmatter KEYS (wingwing_chapter, wingwing_unit, unit_title, etc.)
   - YAML frontmatter VALUES (keep as-is for system compatibility)
   - FAA, ICAO, ATC, IFR, VFR, GPS, VOR, NDB, ADF abbreviations and acronyms
   - Aircraft model names and designations (Cessna 172, Piper Cherokee, etc.)
   - Proper nouns: organization names (FAA, NTSB, AOPA), regulation codes (14 CFR Part 61)
   - Technical aviation terms that are internationally used in English in aviation contexts
3. Preserve ALL Markdown formatting exactly: ##, ###, **, *, -, ---
4. Translate section headings, learning objectives, key terms definitions, and review questions
5. When a technical term has a standard Spanish equivalent used in Latin American aviation, use it
6. Maintain the professional, textbook tone throughout
7. Do NOT add explanatory notes or translator comments"""


def get_client():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found in environment")
    http_client = httpx.Client(verify=False)
    return anthropic.Anthropic(api_key=api_key, http_client=http_client)


def split_into_sections(content):
    """Split markdown content into translatable chunks by ## headings."""
    frontmatter = ""
    body = content
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            frontmatter = content[:end + 3]
            body = content[end + 3:].lstrip("\n")

    sections = []
    current = ""
    for line in body.split("\n"):
        if line.startswith("## ") and current.strip():
            sections.append(current)
            current = line + "\n"
        else:
            current += line + "\n"
    if current.strip():
        sections.append(current)

    return frontmatter, sections


def translate_section(client, section_text, section_num, total_sections, unit_label):
    """Translate a single section with retry logic."""
    for attempt in range(3):
        try:
            message = client.messages.create(
                model=MODEL,
                max_tokens=8000,
                messages=[
                    {
                        "role": "user",
                        "content": f"""Translate the following aviation textbook section from English to Latin American Spanish.
Follow all rules from your system instructions precisely.

ENGLISH SOURCE:
{section_text}

SPANISH TRANSLATION:"""
                    }
                ],
                system=SYSTEM_PROMPT
            )
            return message.content[0].text
        except Exception as e:
            if "rate_limit" in str(e).lower() and attempt < 2:
                wait = 60 * (attempt + 1)
                print(f"    [{unit_label}] Rate limit on section {section_num}, waiting {wait}s...")
                time.sleep(wait)
            else:
                raise
    return None


def translate_unit(unit_path, output_path):
    """Translate a complete unit file. Each unit gets its own client."""
    client = get_client()
    unit_label = f"{unit_path.parent.name}/{unit_path.name}"

    print(f"\n  → Starting: {unit_label}")
    content = unit_path.read_text(encoding="utf-8")
    frontmatter, sections = split_into_sections(content)
    print(f"    Sections: {len(sections)}")

    translated_sections = []
    for i, section in enumerate(sections, 1):
        if i > 1:
            time.sleep(3)
        translated = translate_section(client, section, i, len(sections), unit_label)
        translated_sections.append(translated)
        print(f"    [{unit_label}] {i}/{len(sections)} sections done")

    translated_content = frontmatter + "\n\n" + "\n\n".join(translated_sections)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(translated_content, encoding="utf-8")
    print(f"  ✓ Complete: {unit_label}")
    return unit_label


def get_pending_units():
    """Get all units that haven't been translated yet."""
    pending = []
    for chapter_dir in sorted(OUTPUT_DIR.iterdir()):
        if not chapter_dir.is_dir():
            continue
        for unit_file in sorted(chapter_dir.glob("unit-*.md")):
            relative = unit_file.relative_to(OUTPUT_DIR)
            output_path = OUTPUT_ES_DIR / relative
            if not output_path.exists():
                pending.append((unit_file, output_path))
    return pending


def run_chapter(chapter_num, units):
    """Translate units in a chapter using parallel processing (max 2 at a time)."""
    print(f"\n{'='*60}")
    print(f"Chapter {chapter_num} — {len(units)} unit(s) to translate")
    print(f"{'='*60}")

    chapter_start = time.time()

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {}
        for i, (unit_path, output_path) in enumerate(units):
            if i > 0:
                print(f"  Staggering next unit start by 30s...")
                time.sleep(30)
            future = executor.submit(translate_unit, unit_path, output_path)
            futures[future] = unit_path.name

        for future in as_completed(futures):
            unit_name = futures[future]
            try:
                result = future.result()
            except Exception as e:
                print(f"  ✗ FAILED: {unit_name} — {e}")

    elapsed = time.time() - chapter_start
    print(f"\n  Chapter {chapter_num} complete in {elapsed/60:.1f} min")
    return elapsed


def main():
    pending = get_pending_units()

    if not pending:
        print("All units already translated!")
        return

    print(f"\n{'='*60}")
    print(f"WingWing PPL Textbook - Full Spanish Translation")
    print(f"{'='*60}")
    print(f"Units remaining: {len(pending)}")

    # Group by chapter
    chapters = {}
    for unit_path, output_path in pending:
        ch = unit_path.parent.name
        if ch not in chapters:
            chapters[ch] = []
        chapters[ch].append((unit_path, output_path))

    print(f"Chapters to process: {len(chapters)}")

    total_start = time.time()

    for chapter_name in sorted(chapters.keys()):
        chapter_num = chapter_name.split("-")[0]
        units = chapters[chapter_name]
        run_chapter(chapter_num, units)

    total_elapsed = time.time() - total_start
    print(f"\n{'='*60}")
    print(f"FULL TRANSLATION COMPLETE")
    print(f"  Total units: {len(pending)}")
    print(f"  Total time:  {total_elapsed/60:.1f} minutes")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
