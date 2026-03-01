#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const [,, pagesDir, outFile, docId = 'sport-rec-private-akts'] = process.argv;

if (!pagesDir || !outFile) {
  console.error('Usage: node build-webp-manifest.mjs <pages-dir> <out-manifest.json> [docId]');
  process.exit(1);
}

if (!fs.existsSync(pagesDir)) {
  console.error(`Pages directory not found: ${pagesDir}`);
  process.exit(1);
}

function probeDimensions(filePath) {
  try {
    const out = execFileSync('ffprobe', [
      '-v', 'error',
      '-select_streams', 'v:0',
      '-show_entries', 'stream=width,height',
      '-of', 'csv=s=x:p=0',
      filePath,
    ], { encoding: 'utf8' }).trim();

    const [w, h] = out.split('x').map(Number);
    if (Number.isFinite(w) && Number.isFinite(h)) {
      return { width: w, height: h };
    }
  } catch {
    // Keep null dimensions if probing fails.
  }
  return { width: null, height: null };
}

const files = fs.readdirSync(pagesDir)
  .filter((name) => name.endsWith('.webp'))
  .sort((a, b) => a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' }));

const pages = files.map((file) => {
  const pageMatch = file.match(/(\d+)(?=\.webp$)/i);
  const pageNumber = pageMatch ? Number(pageMatch[1]) : null;
  const fullPath = path.join(pagesDir, file);
  const dims = probeDimensions(fullPath);

  return {
    page: pageNumber,
    type: 'webp',
    path: `pages/${file}`,
    width: dims.width,
    height: dims.height,
    bytes: fs.statSync(fullPath).size,
  };
});

const manifest = {
  version: 1,
  docId,
  format: 'webp-single-page',
  generatedAt: new Date().toISOString(),
  pageCount: pages.length,
  pages,
};

fs.mkdirSync(path.dirname(outFile), { recursive: true });
fs.writeFileSync(outFile, JSON.stringify(manifest, null, 2));

console.log(`Manifest written: ${outFile}`);
