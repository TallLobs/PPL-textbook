# Private Pilot Textbook Workspace

This repository contains the instructional content pipeline for the Private Pilot course (not the question bank).

## Purpose

- Maintain and evolve private pilot textbook content.
- Store oral exam preparation JSON assets (seed for a future oral exam quiz engine).
- Store required exam figures/assets.
- Build a condensed **test guide** for fast review and memorization.

## Folder Structure

- `textbook-content/`
  - Main textbook outputs (chapter content in English/Spanish, exports, indexes).

- `oral-exam-json/`
  - Oral exam preparatory JSON components (temporary structure, kept intentionally).
  - `chapters/` contains chapter-level oral prep data.

- `figures/`
  - Required private pilot figures and figure-generation pipeline assets.

- `test-guide/`
  - Condensed study guide meant for memorization, quick review, and exam prep notes.
  - `notes/` is the working area for concise study content.

- `sources/`
  - Source PDFs and reference material used to derive instructional content.

- `scripts/`
  - Generation, formatting, export, and upload tooling.

- `docs/`
  - Supporting planning/structure documents.

## Scope Boundary

This project is for textbook and oral-prep instructional content.
Question bank data lives in a separate project.

## Immediate Next Steps

1. Keep chapter content normalized in `textbook-content/chapters` and `textbook-content/chapters-es`.
2. Continue expanding `oral-exam-json/chapters` for oral exam engine readiness.
3. Build `test-guide/notes` as a condensed memory-first companion to the textbook.
4. Version all structural/content changes through Git.
