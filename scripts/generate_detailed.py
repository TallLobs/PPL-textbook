#!/usr/bin/env python3
"""
WingWing PPL Textbook - Detailed Section-by-Section Generator

This script generates comprehensive textbook units by:
1. Creating a detailed outline from FAA sources
2. Generating each section individually with depth
3. Assembling sections into a complete, textbook-quality unit
"""

import anthropic
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import PyPDF2
import argparse
import httpx
import json
import time

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

SOURCES_DIR = PROJECT_ROOT / "sources" / "faa-phak"
OUTPUT_DIR = PROJECT_ROOT / "output" / "chapters"
TEMP_DIR = PROJECT_ROOT / "output" / "temp"
TEMP_DIR.mkdir(parents=True, exist_ok=True)

# Chapter mapping (same as generate.py)
CHAPTER_MAP = {
    1: {
        "name": "01-regulations",
        "title": "Regulations and Pilot Qualifications",
        "units": {
            "A": {
                "title": "Pilot Training",
                "faa_sources": ["PHAK - Chapter 01 - Introduction To Flying.pdf"],
                "focus": "History of flight, pilot certificates and ratings, medical certification, student pilot requirements, knowledge and skill tests, flight training options, role of flight instructors"
            },
            "B": {
                "title": "Aviation Opportunities",
                "faa_sources": ["PHAK - Chapter 01 - Introduction To Flying.pdf"],
                "focus": "Career opportunities in aviation, recreational flying, aviation organizations, continuing education"
            }
        }
    },
    2: {
        "name": "02-airplane-systems",
        "title": "Airplane Systems",
        "units": {
            "A": {
                "title": "Airplanes",
                "faa_sources": ["PHAK - Chapter 03 - Aircraft Construction.pdf"],
                "focus": "Aircraft design and certification, fuselage structures (truss, monocoque, semi-monocoque), wing structures and configurations, empennage, landing gear types"
            },
            "B": {
                "title": "The Powerplant and Related Systems",
                "faa_sources": ["PHAK - Chapter 07 - Aircraft Systems.pdf"],
                "focus": "Reciprocating engines, induction systems (carbureted vs fuel-injected), ignition systems, fuel systems, oil systems, cooling systems, electrical systems, propeller systems"
            },
            "C": {
                "title": "Flight Instruments",
                "faa_sources": ["PHAK - Chapter 08 - Flight Instruments.pdf", "PHAK - Chapter 06 - Flight Controls.pdf"],
                "focus": "Pitot-static system (airspeed, altimeter, VSI), gyroscopic instruments (attitude, heading, turn coordinator), magnetic compass, electronic flight displays (glass cockpit), primary and secondary flight controls"
            }
        }
    },
    3: {
        "name": "03-aerodynamics",
        "title": "Aerodynamic Principles",
        "units": {
            "A": {
                "title": "Four Forces of Flight",
                "faa_sources": ["PHAK - Chapter 04 - Principles of Flight.pdf"],
                "focus": "Structure of the atmosphere, Newton's laws of motion, Bernoulli's principle, airfoil design and lift production, four forces (lift, weight, thrust, drag), angle of attack, stalls"
            },
            "B": {
                "title": "Stability",
                "faa_sources": ["PHAK - Chapter 05 - Aerodynamics of Flight.pdf"],
                "focus": "Static and dynamic stability, longitudinal stability, lateral stability, directional stability, stability characteristics"
            },
            "C": {
                "title": "Aerodynamics of Maneuvering Flight",
                "faa_sources": ["PHAK - Chapter 05 - Aerodynamics of Flight.pdf"],
                "focus": "Turning flight, climbs and descents, load factor and maneuvering, stalls and spins, ground effect"
            }
        }
    },
    4: {
        "name": "04-flight-environment",
        "title": "The Flight Environment",
        "units": {
            "A": {
                "title": "Safety of Flight",
                "faa_sources": ["PHAK - Chapter 02 - Aeronautical Decision-Making.pdf"],
                "focus": "Aeronautical decision-making, risk management, hazardous attitudes (IMSAFE), single-pilot resource management, situational awareness"
            },
            "B": {
                "title": "Airports",
                "faa_sources": ["PHAK - Chapter 14 - Airport Operations.pdf"],
                "focus": "Airport types and ownership, runway markings and lighting, taxiway markings and signs, airport traffic patterns, wake turbulence, collision avoidance"
            },
            "C": {
                "title": "Aeronautical Charts",
                "faa_sources": ["PHAK - Chapter 16 - Navigation.pdf"],
                "focus": "Sectional charts, chart symbols and legend, latitude and longitude, chart reading and interpretation"
            },
            "D": {
                "title": "Airspace",
                "faa_sources": ["PHAK - Chapter 15 - Airspace.pdf"],
                "focus": "Controlled airspace (A, B, C, D, E), uncontrolled airspace (G), special use airspace, other airspace areas (TFRs, MOAs, etc.)"
            }
        }
    },
    5: {
        "name": "05-communication",
        "title": "Communication and Flight Information",
        "units": {
            "A": {
                "title": "ATC Services",
                "faa_sources": ["PHAK - Chapter 09 - Flight Manuals and Other Documents.pdf"],
                "focus": "Air traffic control services, radar services, terminal services, flight service stations, ATC clearances and instructions"
            },
            "B": {
                "title": "Radio Procedures",
                "faa_sources": ["PHAK - Chapter 09 - Flight Manuals and Other Documents.pdf"],
                "focus": "Radio communication phraseology, phonetic alphabet, communication procedures, emergency procedures, lost communication procedures"
            },
            "C": {
                "title": "Sources of Flight Information",
                "faa_sources": ["PHAK - Chapter 09 - Flight Manuals and Other Documents.pdf"],
                "focus": "Pilot's Operating Handbook (POH), Airplane Flight Manual (AFM), required documents (ARROW), airworthiness directives, weight and balance documents"
            }
        }
    },
    6: {
        "name": "06-meteorology",
        "title": "Meteorology for Pilots",
        "units": {
            "A": {
                "title": "Basic Weather Theory",
                "faa_sources": ["PHAK - Chapter 12 - Weather Theory.pdf"],
                "focus": "Atmosphere composition and structure, atmospheric pressure and altimetry, temperature effects, moisture and humidity"
            },
            "B": {
                "title": "Weather Patterns",
                "faa_sources": ["PHAK - Chapter 12 - Weather Theory.pdf"],
                "focus": "Wind patterns and circulation, air masses and fronts, clouds and precipitation, atmospheric stability"
            },
            "C": {
                "title": "Weather Hazards",
                "faa_sources": ["PHAK - Chapter 12 - Weather Theory.pdf"],
                "focus": "Turbulence, thunderstorms, icing, fog and visibility restrictions, wind shear"
            }
        }
    },
    7: {
        "name": "07-weather-data",
        "title": "Interpreting Weather Data",
        "units": {
            "A": {
                "title": "The Forecasting Process",
                "faa_sources": ["PHAK - Chapter 13 - Aviation Weather Services.pdf"],
                "focus": "Weather observation systems, forecasting methods, weather service providers"
            },
            "B": {
                "title": "Aviation Weather Reports and Forecasts",
                "faa_sources": ["PHAK - Chapter 13 - Aviation Weather Services.pdf"],
                "focus": "METARs and TAFs, PIREPs, winds and temperatures aloft, AIRMETs and SIGMETs"
            },
            "C": {
                "title": "Graphic Weather Products",
                "faa_sources": ["PHAK - Chapter 13 - Aviation Weather Services.pdf"],
                "focus": "Radar and satellite imagery, prognostic charts, surface analysis, convective outlooks"
            },
            "D": {
                "title": "Sources of Weather Information",
                "faa_sources": ["PHAK - Chapter 13 - Aviation Weather Services.pdf"],
                "focus": "1800wxbrief and online resources, Flight Service Stations, weather apps and tools"
            }
        }
    },
    8: {
        "name": "08-performance",
        "title": "Airplane Performance",
        "units": {
            "A": {
                "title": "Predicting Performance",
                "faa_sources": ["PHAK - Chapter 11 - Aircraft Performance.pdf"],
                "focus": "Density altitude effects, performance charts, takeoff and landing performance, climb and cruise performance"
            },
            "B": {
                "title": "Weight and Balance",
                "faa_sources": ["PHAK - Chapter 10 - Weight and Balance.pdf"],
                "focus": "Weight terminology, center of gravity, weight and balance calculations, loading graphs"
            },
            "C": {
                "title": "Flight Computers",
                "faa_sources": ["PHAK - Chapter 11 - Aircraft Performance.pdf"],
                "focus": "E6B flight computer, electronic flight computers, performance calculations, flight planning computations"
            }
        }
    },
    9: {
        "name": "09-navigation",
        "title": "Navigation",
        "units": {
            "A": {
                "title": "Pilotage and Dead Reckoning",
                "faa_sources": ["PHAK - Chapter 16 - Navigation.pdf"],
                "focus": "Visual navigation techniques, dead reckoning calculations, chart reading, flight planning"
            },
            "B": {
                "title": "VOR Navigation",
                "faa_sources": ["PHAK - Chapter 16 - Navigation.pdf"],
                "focus": "VOR principles and operation, VOR navigation procedures, VOR-DME, limitations"
            },
            "C": {
                "title": "Satellite Navigation - GPS",
                "faa_sources": ["PHAK - Chapter 16 - Navigation.pdf"],
                "focus": "GPS fundamentals, RAIM and WAAS, GPS navigation procedures, limitations and errors"
            }
        }
    },
    10: {
        "name": "10-human-factors",
        "title": "Applying Human Factors Principles",
        "units": {
            "A": {
                "title": "Aviation Physiology",
                "faa_sources": ["PHAK - Chapter 17 - Aeromedical Factors.pdf"],
                "focus": "Hypoxia, hyperventilation, spatial disorientation, motion sickness, carbon monoxide, stress and fatigue, vision, drugs and alcohol"
            },
            "B": {
                "title": "Single-Pilot Resource Management",
                "faa_sources": ["PHAK - Chapter 02 - Aeronautical Decision-Making.pdf"],
                "focus": "Risk management, hazardous attitudes, decision-making models, automation management, crew resource management principles"
            }
        }
    }
}


def extract_pdf_text(pdf_path):
    """Extract text from a PDF file (with caching)."""
    # Check for cached version
    cache_name = pdf_path.stem.replace(' - ', '_').replace(' ', '_') + '.txt'
    cache_path = TEMP_DIR / cache_name

    if cache_path.exists():
        print(f"  Using cached text from {cache_path.name}")
        with open(cache_path, 'r', encoding='utf-8') as f:
            return f.read()

    # Extract from PDF
    text = []
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            total_pages = len(pdf_reader.pages)
            print(f"  Reading {total_pages} pages (this may take a minute)...")
            for i, page in enumerate(pdf_reader.pages, 1):
                if i % 10 == 0:
                    print(f"    Progress: {i}/{total_pages} pages")
                text.append(page.extract_text())

        full_text = "\n\n".join(text)

        # Cache for next time
        with open(cache_path, 'w', encoding='utf-8') as f:
            f.write(full_text)
        print(f"  Cached to {cache_path.name}")

        return full_text

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""


def create_api_client():
    """Create and return an Anthropic API client."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in .env file")
        sys.exit(1)

    http_client = httpx.Client(verify=False)
    return anthropic.Anthropic(api_key=api_key, http_client=http_client)


def generate_outline(client, chapter_num, unit_letter, source_text, model):
    """
    Generate a detailed outline for the unit by analyzing FAA source material.
    Returns a structured outline with 6-10 major sections.
    """
    chapter_info = CHAPTER_MAP[chapter_num]
    unit_info = chapter_info["units"][unit_letter]

    print("\n" + "="*60)
    print("STAGE 1: GENERATING DETAILED OUTLINE")
    print("="*60)

    prompt = f"""You are creating a detailed outline for a Private Pilot License (PPL) textbook unit.

**Unit Information:**
- Chapter {chapter_num}: {chapter_info['title']}
- Unit {unit_letter}: {unit_info['title']}
- Focus Areas: {unit_info['focus']}

**Your Task:**
Analyze the FAA source material below and create a comprehensive outline for this unit. This is a TEXTBOOK, not a summary - it needs exam-level depth.

**Requirements:**
1. Create 6-10 MAJOR SECTIONS that thoroughly cover the focus areas
2. Each major section should have 3-5 subsections
3. Include specific topics, procedures, regulations, and technical details
4. Think about what a student needs to know to pass the FAA exam
5. Order sections logically (fundamentals → applications → specifics)

**Output Format:**
Return ONLY a JSON structure like this:
{{
  "unit_title": "{unit_info['title']}",
  "estimated_total_words": 8000,
  "sections": [
    {{
      "section_number": 1,
      "section_title": "SECTION TITLE IN CAPS",
      "estimated_words": 1200,
      "subsections": [
        "Subsection 1 title",
        "Subsection 2 title",
        "Subsection 3 title"
      ],
      "key_topics": [
        "Specific topic or concept 1",
        "Specific topic or concept 2"
      ]
    }}
  ]
}}

**FAA Source Material (first 50,000 chars):**
{source_text[:50000]}

Generate the outline now as valid JSON only:"""

    try:
        print("  Sending request to Claude API...")
        print("  (This may take 1-2 minutes for outline generation)")

        message = client.messages.create(
            model=model,
            max_tokens=4000,
            temperature=0.5,
            messages=[{"role": "user", "content": prompt}]
        )

        print("  ✓ Received response, parsing...")
        response_text = message.content[0].text.strip()

        # Try to extract JSON if wrapped in markdown
        if "```json" in response_text:
            response_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            response_text = response_text.split("```")[1].split("```")[0].strip()

        outline = json.loads(response_text)

        print(f"\n✓ Outline generated successfully!")
        print(f"  Sections planned: {len(outline['sections'])}")
        print(f"  Estimated total words: {outline.get('estimated_total_words', 'N/A')}")
        print(f"  Tokens used: {message.usage.input_tokens} input, {message.usage.output_tokens} output")

        return outline

    except json.JSONDecodeError as e:
        print(f"Error: Could not parse outline JSON: {e}")
        print(f"Response was: {response_text[:500]}")
        sys.exit(1)
    except Exception as e:
        print(f"Error generating outline: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def generate_section(client, chapter_num, unit_letter, section_info, outline, source_text, model):
    """
    Generate a single section with deep, textbook-level detail.
    """
    chapter_info = CHAPTER_MAP[chapter_num]
    unit_info = chapter_info["units"][unit_letter]

    section_num = section_info['section_number']
    section_title = section_info['section_title']

    print(f"\n  Section {section_num}/{len(outline['sections'])}: {section_title}")
    print(f"  Target: ~{section_info['estimated_words']} words")

    # Add 3-second delay between sections to avoid rate limits
    if section_num > 1:
        time.sleep(3)

    print(f"  Sending request to API (may take 1-2 minutes)...")

    # Create context from previous sections if any
    context_sections = [s for s in outline['sections'] if s['section_number'] < section_num]
    context_text = ""
    if context_sections:
        context_text = "\n**Previous sections covered:**\n"
        for s in context_sections:
            context_text += f"- {s['section_title']}: {', '.join(s['subsections'][:3])}\n"

    prompt = f"""You are writing ONE SECTION of a comprehensive PPL textbook unit.

**Unit Context:**
- Chapter {chapter_num}: {chapter_info['title']}
- Unit {unit_letter}: {unit_info['title']}
- This is Section {section_num} of {len(outline['sections'])}

{context_text}

**Your Section:**
Title: {section_title}
Subsections to cover: {', '.join(section_info['subsections'])}
Key topics: {', '.join(section_info['key_topics'])}

**Critical Requirements:**
1. **Length**: Write {section_info['estimated_words']}-{section_info['estimated_words'] + 500} words
2. **Depth**: This is a TEXTBOOK - include specific details, procedures, numbers, regulations
3. **Structure**:
   - Start with ## {section_title}
   - Use ### for each subsection
   - Short paragraphs (2-5 sentences)
4. **Content**:
   - Bold **key terms** on first use
   - Include specific examples
   - Reference figures as [Figure X-X: Description - PHAK Ch {chapter_num}, Fig X-X]
   - Add sidebars with > **Title**: content for important notes
5. **Testability**: Include details that would appear on FAA exams
6. **Clarity**: Clear, confident tone. No filler words.

**FAA Source Material:**
{source_text[:80000]}

Write ONLY this section now (start with ## {section_title}):"""

    try:
        message = client.messages.create(
            model=model,
            max_tokens=8000,
            temperature=1,
            messages=[{"role": "user", "content": prompt}]
        )

        section_content = message.content[0].text.strip()
        word_count = len(section_content.split())

        print(f"    ✓ Generated {word_count} words")
        print(f"    Tokens: {message.usage.input_tokens} input, {message.usage.output_tokens} output")

        return section_content, message.usage

    except Exception as e:
        print(f"    ✗ Error generating section: {e}")
        import traceback
        traceback.print_exc()
        return None, None


def generate_front_matter(client, chapter_num, unit_letter, outline, model):
    """Generate introduction and learning objectives."""
    chapter_info = CHAPTER_MAP[chapter_num]
    unit_info = chapter_info["units"][unit_letter]

    print(f"\n  Generating front matter (introduction + learning objectives)")

    sections_summary = "\n".join([f"- {s['section_title']}" for s in outline['sections']])

    prompt = f"""You are writing the INTRODUCTION and LEARNING OBJECTIVES for a PPL textbook unit.

**Unit:**
- Chapter {chapter_num}: {chapter_info['title']}
- Unit {unit_letter}: {unit_info['title']}

**Sections that will follow:**
{sections_summary}

**Your Task:**
Write:
1. An engaging 2-3 sentence introductory paragraph (with hook)
2. Learning objectives section (## Learning Objectives)

**Format:**
```
[2-3 sentence intro paragraph with engaging hook about why this matters]

## Learning Objectives

After completing this unit, you will be able to:

- [Action verb] [specific outcome]
- [Action verb] [specific outcome]
- [5-7 objectives total covering all major topics]
```

Write the front matter now:"""

    try:
        message = client.messages.create(
            model=model,
            max_tokens=2000,
            temperature=1,
            messages=[{"role": "user", "content": prompt}]
        )

        content = message.content[0].text.strip()
        print(f"    ✓ Generated front matter")

        return content, message.usage

    except Exception as e:
        print(f"    ✗ Error: {e}")
        return None, None


def generate_back_matter(client, chapter_num, unit_letter, outline, all_sections_text, model):
    """Generate summary, key terms, and review questions."""
    chapter_info = CHAPTER_MAP[chapter_num]
    unit_info = chapter_info["units"][unit_letter]

    print(f"\n  Generating back matter (summary, key terms, questions)")

    prompt = f"""You are writing the BACK MATTER for a PPL textbook unit.

**Unit:**
- Chapter {chapter_num}: {chapter_info['title']}
- Unit {unit_letter}: {unit_info['title']}

**Content already written (use this to extract key points):**
{all_sections_text[:30000]}

**Your Task:**
Generate three sections:

1. ## Summary
   - 7-10 bullet points covering key concepts
   - One sentence each
   - Cover main topics from all sections

2. ## Key Terms
   - Table format with Term | Definition
   - 10-15 important terms from the unit
   - Clear, concise definitions

3. ## Review Questions
   - 10-12 questions total
   - Mix of: Multiple Choice (4 options), True/False, Short Answer, Matching
   - Test understanding at FAA exam level
   - Questions should cover all major sections

**Format exactly like this:**
```markdown
## Summary

Review the key points from this unit:

- Point 1
- Point 2
[...]

---

## Key Terms

| Term | Definition |
|------|------------|
| **Term 1** | Definition 1 |
| **Term 2** | Definition 2 |

---

## Review Questions

**Multiple Choice**

1. Question?
   - A) Option
   - B) Option
   - C) Option
   - D) Option

[... more questions in various formats ...]

---

## FAA References

- PHAK Chapter {chapter_num}: [Chapter Title], Sections X-X through X-X
```

Write the complete back matter now:"""

    try:
        message = client.messages.create(
            model=model,
            max_tokens=6000,
            temperature=1,
            messages=[{"role": "user", "content": prompt}]
        )

        content = message.content[0].text.strip()
        print(f"    ✓ Generated back matter")

        return content, message.usage

    except Exception as e:
        print(f"    ✗ Error: {e}")
        return None, None


def assemble_unit(chapter_num, unit_letter, outline, front_matter, sections, back_matter):
    """Assemble all parts into final unit markdown file."""
    chapter_info = CHAPTER_MAP[chapter_num]
    unit_info = chapter_info["units"][unit_letter]

    print("\n" + "="*60)
    print("STAGE 4: ASSEMBLING FINAL UNIT")
    print("="*60)

    # Build YAML frontmatter
    yaml_front = f"""---
wingwing_chapter: {chapter_num}
wingwing_unit: "{unit_letter}"
unit_title: "{unit_info['title']}"
faa_sources: {unit_info['faa_sources']}
estimated_read_time: {outline.get('estimated_total_words', 8000) // 200}
---

"""

    # Build unit title
    unit_header = f"# Unit {unit_letter}: {unit_info['title']}\n\n"

    # Combine all parts
    full_content = yaml_front + unit_header + front_matter + "\n\n---\n\n"

    # Add all sections with separators
    for i, section in enumerate(sections):
        full_content += section + "\n\n"
        if i < len(sections) - 1:
            full_content += "---\n\n"

    # Add back matter
    full_content += back_matter

    # Calculate stats
    total_words = len(full_content.split())

    print(f"\n✓ Unit assembled successfully!")
    print(f"  Total words: {total_words:,}")
    print(f"  Total sections: {len(sections)}")
    print(f"  Estimated read time: {total_words // 200} minutes")

    return full_content


def save_unit(chapter_num, unit_letter, content):
    """Save the completed unit to output folder."""
    chapter_info = CHAPTER_MAP[chapter_num]
    unit_info = chapter_info["units"][unit_letter]

    output_folder = OUTPUT_DIR / chapter_info["name"]
    output_folder.mkdir(parents=True, exist_ok=True)

    filename = f"unit-{unit_letter.lower()}-{unit_info['title'].lower().replace(' ', '-')}.md"
    output_path = output_folder / filename

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✓ Unit saved to: {output_path.relative_to(PROJECT_ROOT)}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Generate detailed WingWing PPL textbook units")
    parser.add_argument("--chapter", type=int, required=True, help="Chapter number (1-10)")
    parser.add_argument("--unit", type=str, required=True, help="Unit letter (A, B, C, D)")
    parser.add_argument("--model", type=str, default="claude-sonnet-4-20250514",
                       help="Claude model to use")

    args = parser.parse_args()

    # Validate inputs
    if args.chapter not in CHAPTER_MAP:
        print(f"Error: Chapter {args.chapter} not yet mapped")
        sys.exit(1)

    unit_upper = args.unit.upper()
    if unit_upper not in CHAPTER_MAP[args.chapter]["units"]:
        print(f"Error: Unit {unit_upper} not found in Chapter {args.chapter}")
        sys.exit(1)

    print("\n" + "="*60)
    print(f"DETAILED UNIT GENERATION: Chapter {args.chapter}, Unit {unit_upper}")
    print("="*60)

    chapter_info = CHAPTER_MAP[args.chapter]
    unit_info = chapter_info["units"][unit_upper]

    # Initialize API client
    client = create_api_client()

    # Stage 1: Extract PDF text
    print("\n" + "="*60)
    print("STAGE 0: EXTRACTING SOURCE MATERIAL")
    print("="*60)

    source_texts = []
    for source_file in unit_info["faa_sources"]:
        pdf_path = SOURCES_DIR / source_file
        if pdf_path.exists():
            print(f"\nReading: {source_file}")
            text = extract_pdf_text(pdf_path)
            source_texts.append(text)
        else:
            print(f"Warning: {source_file} not found")

    combined_sources = "\n\n".join(source_texts)
    print(f"\n✓ Extracted {len(combined_sources):,} characters from source PDFs")

    # Stage 2: Generate outline
    outline = generate_outline(client, args.chapter, unit_upper, combined_sources, args.model)

    # Save outline for reference
    outline_path = TEMP_DIR / f"outline_ch{args.chapter}_{unit_upper}.json"
    with open(outline_path, 'w') as f:
        json.dump(outline, f, indent=2)
    print(f"  Outline saved to: {outline_path.relative_to(PROJECT_ROOT)}")

    # Stage 3: Generate each section
    print("\n" + "="*60)
    print("STAGE 2: GENERATING SECTIONS")
    print("="*60)

    sections_content = []
    total_tokens_in = 0
    total_tokens_out = 0

    for section_info in outline['sections']:
        section_text, usage = generate_section(
            client, args.chapter, unit_upper, section_info,
            outline, combined_sources, args.model
        )

        if section_text:
            sections_content.append(section_text)
            if usage:
                total_tokens_in += usage.input_tokens
                total_tokens_out += usage.output_tokens
        else:
            print(f"  Failed to generate section {section_info['section_number']}")
            sys.exit(1)

        # Brief pause to avoid rate limits
        time.sleep(1)

    # Stage 4: Generate front matter
    print("\n" + "="*60)
    print("STAGE 3: GENERATING FRONT & BACK MATTER")
    print("="*60)

    front_matter, usage = generate_front_matter(client, args.chapter, unit_upper, outline, args.model)
    if usage:
        total_tokens_in += usage.input_tokens
        total_tokens_out += usage.output_tokens

    # Stage 5: Generate back matter
    all_sections_text = "\n\n".join(sections_content)
    back_matter, usage = generate_back_matter(
        client, args.chapter, unit_upper, outline, all_sections_text, args.model
    )
    if usage:
        total_tokens_in += usage.input_tokens
        total_tokens_out += usage.output_tokens

    # Stage 6: Assemble final unit
    final_content = assemble_unit(
        args.chapter, unit_upper, outline,
        front_matter, sections_content, back_matter
    )

    # Stage 7: Save unit
    output_path = save_unit(args.chapter, unit_upper, final_content)

    # Final summary
    print("\n" + "="*60)
    print("GENERATION COMPLETE!")
    print("="*60)
    print(f"Total tokens: {total_tokens_in:,} input, {total_tokens_out:,} output")
    print(f"Estimated cost: ${(total_tokens_in * 3 + total_tokens_out * 15) / 1_000_000:.4f}")
    print("="*60)


if __name__ == "__main__":
    main()
