const fs = require('node:fs');
const path = require('node:path');
const { test, expect } = require('@playwright/test');

const calendlyUrl = 'https://calendly.com/atul_jagga/business-plan-free-consult';

test('all consultation links direct visitors to Calendly', () => {
  const root = path.resolve(__dirname, '..');
  const pages = fs.readdirSync(root).filter(file => file.endsWith('.html'));
  const invalidLinks = [];

  for (const page of pages) {
    const html = fs.readFileSync(path.join(root, page), 'utf8');
    const anchors = html.matchAll(/<a\b(?<attributes>[^>]*)>(?<content>[\s\S]*?)<\/a>/gi);

    for (const anchor of anchors) {
      const label = anchor.groups.content.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
      if (!/^book a consult(?:ation)?$/i.test(label)) continue;

      const href = anchor.groups.attributes.match(/href\s*=\s*["']([^"']+)["']/i)?.[1];
      if (href !== calendlyUrl) invalidLinks.push(`${page}: ${label} -> ${href ?? 'missing href'}`);
    }
  }

  expect(invalidLinks).toEqual([]);
});
