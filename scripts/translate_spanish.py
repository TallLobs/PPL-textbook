#!/usr/bin/env python3
"""
WingWing PPL Textbook - Spanish Translation Script

Translates existing English Markdown units into Spanish using Claude.
- Preserves all Markdown formatting and YAML frontmatter structure
- Keeps YAML frontmatter keys in English (system compatibility)
- Translates body content into neutral Latin American Spanish
- Preserves aviation/FAA/ICAO technical terms in English where internationally standard
- Handles large files by translating section by section
"""

import anthropic
import os
import re
import sys
import time
from pathlib import Path
from dotenv import load_dotenv
import httpx

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
    # Separate YAML frontmatter
    frontmatter = ""
    body = content

    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            frontmatter = content[:end + 3]
            body = content[end + 3:].lstrip("\n")

    # Split body by ## headings (keep heading with its content)
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


def translate_section(client, section_text, section_num, total_sections):
    """Translate a single section of markdown content."""
    print(f"    Translating section {section_num}/{total_sections}...")

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


def translate_unit(client, input_path, output_path):
    """Translate a complete unit file."""
    print(f"\n  Reading: {input_path.name}")
    content = input_path.read_text(encoding="utf-8")

    # Count input tokens for cost tracking
    word_count = len(content.split())
    print(f"  Word count: {word_count:,}")

    # Split into sections
    frontmatter, sections = split_into_sections(content)
    print(f"  Sections to translate: {len(sections)}")

    # Translate each section with delay to respect rate limits
    translated_sections = []
    for i, section in enumerate(sections, 1):
        if i > 1:
            time.sleep(3)  # Rate limit protection
        translated = translate_section(client, section, i, len(sections))
        translated_sections.append(translated)

    # Reassemble: keep original YAML frontmatter + translated body
    translated_content = frontmatter + "\n\n" + "\n\n".join(translated_sections)

    # Save output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(translated_content, encoding="utf-8")
    print(f"  ✓ Saved: {output_path}")

    return len(sections)


def get_chapter_dirs():
    """Get all chapter directories sorted."""
    return sorted([d for d in OUTPUT_DIR.iterdir() if d.is_dir()])


def get_output_path(input_path):
    """Mirror the input path structure under chapters-es."""
    relative = input_path.relative_to(OUTPUT_DIR)
    return OUTPUT_ES_DIR / relative


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Translate PPL textbook units to Spanish")
    parser.add_argument("--chapter", type=int, help="Chapter number (1-10), omit for all")
    parser.add_argument("--unit", type=str, help="Unit letter (A, B, C...), requires --chapter")
    parser.add_argument("--list", action="store_true", help="List all available units")
    args = parser.parse_args()

    # Discover all unit files
    all_units = []
    for chapter_dir in get_chapter_dirs():
        for unit_file in sorted(chapter_dir.glob("unit-*.md")):
            all_units.append(unit_file)

    if args.list:
        print(f"\nAvailable units ({len(all_units)} total):")
        for u in all_units:
            es_path = get_output_path(u)
            status = "✓ translated" if es_path.exists() else "  pending"
            print(f"  {status}  {u.parent.name}/{u.name}")
        return

    # Filter by chapter/unit if specified
    if args.chapter:
        chapter_str = f"{args.chapter:02d}-"
        all_units = [u for u in all_units if chapter_str in str(u.parent.name)]
    if args.unit:
        unit_letter = args.unit.upper()
        all_units = [u for u in all_units if f"/unit-{unit_letter.lower()}-" in str(u).lower()
                     or str(u.name).startswith(f"unit-{unit_letter.lower()}-")]

    if not all_units:
        print("No units found matching the specified filters.")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"WingWing PPL Textbook - Spanish Translation")
    print(f"{'='*60}")
    print(f"Units to translate: {len(all_units)}")
    print(f"Output directory: {OUTPUT_ES_DIR}")

    client = get_client()

    total_sections = 0
    start_time = time.time()

    for unit_path in all_units:
        output_path = get_output_path(unit_path)

        if output_path.exists():
            print(f"\n  SKIPPING (already translated): {unit_path.name}")
            continue

        chapter_name = unit_path.parent.name
        print(f"\n[{chapter_name}] {unit_path.name}")

        sections = translate_unit(client, unit_path, output_path)
        total_sections += sections

    elapsed = time.time() - start_time
    print(f"\n{'='*60}")
    print(f"Translation complete!")
    print(f"  Units translated: {len(all_units)}")
    print(f"  Total sections:   {total_sections}")
    print(f"  Time elapsed:     {elapsed/60:.1f} minutes")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
