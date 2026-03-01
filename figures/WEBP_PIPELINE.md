# Simple WebP Plan (No Tiles)

This is a one-file-per-page plan with direct Supabase Storage integration.

## Output model

- One WebP per PDF page, named by PDF page number:
  - `001.webp`, `002.webp`, ..., `113.webp`
- One manifest JSON file:
  - `manifest.json`

## 1) Dependencies

```bash
brew install poppler webp ffmpeg
```

## 2) Convert PDF -> WebP pages

```bash
/Users/alessandro/Documents/VS-Code/pdf-web/scripts/pdf-to-webp.sh \
  /Users/alessandro/Documents/VS-Code/pdf-web/sport_rec_private_akts.pdf \
  /Users/alessandro/Documents/VS-Code/pdf-web/output-webp \
  220 \
  80
```

Arguments:
- `220` = render DPI (increase for sharper zoom, larger files)
- `80` = WebP quality (higher is sharper, larger files)

## 3) Build manifest

```bash
node /Users/alessandro/Documents/VS-Code/pdf-web/scripts/build-webp-manifest.mjs \
  /Users/alessandro/Documents/VS-Code/pdf-web/output-webp/pages \
  /Users/alessandro/Documents/VS-Code/pdf-web/output-webp/manifest.json \
  sport-rec-private-akts
```

## 4) Supabase Storage structure

Recommended object paths:
- `manuals/<docId>/pages/001.webp`
- `manuals/<docId>/pages/002.webp`
- `manuals/<docId>/manifest.json`

Use long cache headers:
- `Cache-Control: public, max-age=31536000, immutable`

## 5) Supabase upload example (Node)

```js
import fs from 'node:fs';
import path from 'node:path';
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_SERVICE_ROLE_KEY);
const bucket = 'manual-assets';
const docId = 'sport-rec-private-akts';
const base = '/Users/alessandro/Documents/VS-Code/pdf-web/output-webp';

for (const file of fs.readdirSync(path.join(base, 'pages'))) {
  const body = fs.readFileSync(path.join(base, 'pages', file));
  await supabase.storage
    .from(bucket)
    .upload(`manuals/${docId}/pages/${file}`, body, {
      upsert: true,
      contentType: 'image/webp',
      cacheControl: '31536000',
    });
}

const manifest = fs.readFileSync(path.join(base, 'manifest.json'));
await supabase.storage
  .from(bucket)
  .upload(`manuals/${docId}/manifest.json`, manifest, {
    upsert: true,
    contentType: 'application/json',
    cacheControl: '3600',
  });
```
