#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const [,, svgDir, outFile, docId = 'sport-rec-private-akts'] = process.argv;

if (!svgDir || !outFile) {
  console.error('Usage: node build-manifest.mjs <svg-dir> <out-manifest.json> [docId]');
  process.exit(1);
}

if (!fs.existsSync(svgDir)) {
  console.error(`SVG directory not found: ${svgDir}`);
  process.exit(1);
}

const files = fs.readdirSync(svgDir)
  .filter((name) => name.endsWith('.svg'))
  .sort((a, b) => a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' }));

const pages = files.map((file) => {
  const pageMatch = file.match(/(\d+)(?=\.svg$)/i);
  const pageNumber = pageMatch ? Number(pageMatch[1]) : null;
  const full = path.join(svgDir, file);
  const svg = fs.readFileSync(full, 'utf8');
  const vb = svg.match(/viewBox\s*=\s*"([^"]+)"/i);
  const wh = {
    width: null,
    height: null,
  };

  if (vb) {
    const parts = vb[1].trim().split(/\s+/).map(Number);
    if (parts.length === 4 && Number.isFinite(parts[2]) && Number.isFinite(parts[3])) {
      wh.width = parts[2];
      wh.height = parts[3];
    }
  }

  return {
    page: pageNumber,
    type: 'svg',
    path: `pages/${file}`,
    width: wh.width,
    height: wh.height,
    bytes: fs.statSync(full).size,
  };
});

const manifest = {
  version: 1,
  docId,
  generatedAt: new Date().toISOString(),
  pageCount: pages.length,
  pages,
};

fs.mkdirSync(path.dirname(outFile), { recursive: true });
fs.writeFileSync(outFile, JSON.stringify(manifest, null, 2));

console.log(`Manifest written: ${outFile}`);
