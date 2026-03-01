#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const [,, inputDir, outputDir] = process.argv;

if (!inputDir || !outputDir) {
  console.error('Usage: node package-svg.mjs <input-svg-dir> <output-pages-dir>');
  process.exit(1);
}

if (!fs.existsSync(inputDir)) {
  console.error(`Input directory not found: ${inputDir}`);
  process.exit(1);
}

fs.mkdirSync(outputDir, { recursive: true });

const files = fs.readdirSync(inputDir)
  .filter((f) => f.endsWith('.svg'));

const entries = files
  .map((file) => {
    const match = file.match(/(\d+)(?=\.svg$)/i);
    if (!match) return null;
    return { file, page: Number(match[1]) };
  })
  .filter(Boolean)
  .sort((a, b) => a.page - b.page);

const padWidth = String(entries[entries.length - 1]?.page ?? 0).length || 3;

entries.forEach(({ file, page }) => {
  const from = path.join(inputDir, file);
  const to = path.join(outputDir, `${String(page).padStart(padWidth, '0')}.svg`);
  fs.copyFileSync(from, to);
});

console.log(`Packaged ${entries.length} SVG pages to ${outputDir}`);
