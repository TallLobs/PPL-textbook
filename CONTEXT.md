# WingWing PPL Textbook Generator - Project Context

> **Purpose**: This document provides all context needed for an AI assistant to continue work on this project. Read this file first before starting any task.

---

## Project Overview

**Goal**: Create a Private Pilot License (PPL) textbook for the WingWing flight training app.

**Approach**:
- Use **FAA PHAK** (Pilot's Handbook of Aeronautical Knowledge) as the content source (public domain)
- Use **Jeppesen Private Pilot** textbook as the structural/pedagogical template (copyrighted - structure only, no text copying)
- Generate original educational content in a consistent WingWing format

**Owner**: Alessandro (anocera27@outlook.com)

---

## Project Structure

```
PPL-textbook/
├── .env                    # Claude API key (NEVER commit)
├── .gitignore              # Git ignore rules
├── CONTEXT.md              # THIS FILE - read first
│
├── docs/
│   └── WINGWING_MASTER_STRUCTURE.md   # Complete chapter mapping
│
├── sources/
│   ├── faa-phak/           # FAA PHAK chapters (17 PDFs)
│   └── reference/
│       └── Jeppesen-Private-Pilot.pdf  # Layout reference only
│
├── scripts/                # Generation scripts
│   └── generate.py         # Main generation script (to be created)
│
├── templates/              # Output templates
│   └── unit_template.md    # Template for each unit
│
└── output/
    └── chapters/           # Generated content goes here
        ├── 01-regulations/
        ├── 02-airplane-systems/
        ├── 03-aerodynamics/
        ├── 04-flight-environment/
        ├── 05-communication/
        ├── 06-meteorology/
        ├── 07-weather-data/
        ├── 08-performance/
        ├── 09-navigation/
        └── 10-human-factors/
```

---

## Chapter Structure (10 Chapters)

| # | WingWing Chapter | FAA Source Chapters | Units |
|---|------------------|---------------------|-------|
| 1 | Regulations and Pilot Qualifications | Ch 01 | A, B |
| 2 | Airplane Systems | Ch 03, 06, 07, 08 | A, B, C |
| 3 | Aerodynamic Principles | Ch 04, 05 | A, B, C |
| 4 | The Flight Environment | Ch 02*, 14, 15, 16* | A, B, C, D |
| 5 | Communication and Flight Information | Ch 09 + AIM | A, B, C |
| 6 | Meteorology for Pilots | Ch 12 | A, B, C |
| 7 | Interpreting Weather Data | Ch 13 | A, B, C, D |
| 8 | Airplane Performance | Ch 10, 11 | A, B, C |
| 9 | Navigation | Ch 16 | A, B, C |
| 10 | Applying Human Factors Principles | Ch 02, 17 | A, B |

*See `docs/WINGWING_MASTER_STRUCTURE.md` for complete section-by-section mapping.*

---

## Jeppesen Layout Template

Each unit follows this structure (derived from analyzing the Jeppesen textbook):

### Opening
1. **Section Header** - "SECTION A: [Title]"
2. **Introductory Hook** - Historical context or engaging opener (2-3 sentences)
3. **Overview** - What this section covers

### Main Content
4. **CAPS HEADINGS** - Major topic divisions
5. **Body Text** - Short paragraphs (2-5 sentences each)
6. **Figure References** - `[Figure X-X: Description]` inline
7. **Sidebars** - Historical context, technical deep-dives (boxed)
8. **Bold Terms** - Key vocabulary bolded on first use
9. **Memory Aids** - Acronyms like ARROW, IMSAFE, etc.

### Closing
10. **Summary Checklist** - Bulleted key takeaways (5-10 points)
11. **KEY TERMS** - Two-column vocabulary list
12. **QUESTIONS** - Mixed formats:
    - Diagram/figure identification
    - Short answer
    - True/False
    - Matching
    - Multiple choice (3-4 options)

---

## Output Format for Each Unit

```markdown
---
wingwing_chapter: [1-10]
wingwing_unit: [A, B, C, D]
unit_title: "[Title]"
faa_sources: ["PHAK Chapter XX"]
estimated_read_time: [X] minutes
---

# Unit [X]: [Title]

[Introductory paragraph with hook]

## Learning Objectives

After completing this unit, you will be able to:
- Objective 1
- Objective 2
- Objective 3 (3-6 total)

## [MAIN CONTENT HEADING]

[Content paragraphs...]

[Figure X-X: Description - FAA PHAK Ch XX, Fig XX-X]

### [Subheading]

[More content...]

> **Historical Note**: [Sidebar content]

## Summary

- Key point 1
- Key point 2
- Key point 3 (5-10 total)

## Key Terms

| Term | Definition |
|------|------------|
| Term 1 | Definition 1 |
| Term 2 | Definition 2 |

## Review Questions

1. [Question]
   - A) Option
   - B) Option
   - C) Option
   - D) Option

2. True or False: [Statement]

3. [Short answer question]

---
*FAA References: PHAK Chapter XX, Sections YY-ZZ*
```

---

## Content Guidelines

### Style
- **Tone**: Clear, calm, confident. No filler words.
- **Sentences**: Short to medium length.
- **Structure**: Use headings and bullets for scannability.
- **Acronyms**: Define on first use, e.g., "Visual Flight Rules (VFR)"

### Copyright Rules
- **FAA content**: Public domain - use freely for facts, definitions, figures
- **Jeppesen**: COPYRIGHTED - use for structure/pedagogy inspiration ONLY
- **Never copy Jeppesen text verbatim**
- **All paraphrasing must be original, derived from FAA content**

### Figure References
- Reference FAA figures with: `[Figure X-X: Description - PHAK Ch XX]`
- Do not embed actual images in markdown output
- Figures will be added separately in the final app

---

## API Configuration

- **API Key**: Stored in `.env` file (never commit)
- **Recommended Model**: `claude-sonnet-4-20250514` (best quality/cost balance)
- **Budget**: ~$10 available (~10-12 units worth)

### Using the API

```python
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
```

---

## Current Progress

### Completed
- [x] Project structure organized
- [x] FAA-to-WingWing chapter mapping complete
- [x] Jeppesen layout analysis complete
- [x] Output format defined

### Next Steps
1. Create generation script (`scripts/generate.py`)
2. Generate prototype unit (Chapter 3, Unit A: Four Forces of Flight recommended)
3. Review and refine output format
4. Generate remaining units systematically

---

## Quick Start for New Session

1. **Read this file** (CONTEXT.md)
2. **Read the mapping**: `docs/WINGWING_MASTER_STRUCTURE.md`
3. **Check the template**: `templates/unit_template.md`
4. **Pick a unit to generate** from the chapter structure above
5. **Read the relevant FAA source** from `sources/faa-phak/`
6. **Generate content** following the output format
7. **Save to**: `output/chapters/[XX-chapter-name]/unit-[X]-[title].md`

---

## Commands Reference

### Generate a unit manually
```
Read sources/faa-phak/PHAK - Chapter XX - [Name].pdf
Generate Unit [X] following the template in templates/unit_template.md
Save to output/chapters/[folder]/unit-[x]-[name].md
```

### Run generation script (when created)
```bash
python scripts/generate.py --chapter 3 --unit A
```

---

*Last Updated: January 2026*
*Project Version: 1.0*
