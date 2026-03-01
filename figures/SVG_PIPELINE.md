# SVG-only PDF Pipeline

This setup converts a PDF into one SVG file per page, optimizes SVGs, packages them with stable names, and generates a manifest for backend/frontend usage.

## 1) Install dependencies

```bash
brew install poppler
npm i -g svgo
```

## 2) Convert PDF to SVG

```bash
/Users/alessandro/Documents/VS-Code/pdf-web/scripts/pdf-to-svg.sh \
  /Users/alessandro/Documents/VS-Code/pdf-web/sport_rec_private_akts.pdf \
  /Users/alessandro/Documents/VS-Code/pdf-web/output
```

This creates:
- `/Users/alessandro/Documents/VS-Code/pdf-web/output/raw-svg`
- `/Users/alessandro/Documents/VS-Code/pdf-web/output/svg`

## 3) Package to stable page names

```bash
node /Users/alessandro/Documents/VS-Code/pdf-web/scripts/package-svg.mjs \
  /Users/alessandro/Documents/VS-Code/pdf-web/output/svg \
  /Users/alessandro/Documents/VS-Code/pdf-web/output/pages
```

This creates page files like:
- `001.svg`
- `002.svg`
- `003.svg`

## 4) Generate manifest

```bash
node /Users/alessandro/Documents/VS-Code/pdf-web/scripts/build-manifest.mjs \
  /Users/alessandro/Documents/VS-Code/pdf-web/output/pages \
  /Users/alessandro/Documents/VS-Code/pdf-web/output/manifest.json \
  sport-rec-private-akts
```

## 5) Upload structure to Supabase Storage

Recommended object paths:
- `manuals/<docId>/pages/001.svg`
- `manuals/<docId>/pages/002.svg`
- `manuals/<docId>/manifest.json`

Set long cache headers on pages:
- `Cache-Control: public, max-age=31536000, immutable`

## Frontend rendering

- Load `manifest.json`
- Render each page as an `<object>` or inline `<img src="...svg">`
- Use CSS zoom/transform or viewport scaling for zoom UI

