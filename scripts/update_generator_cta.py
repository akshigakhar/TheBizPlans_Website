#!/usr/bin/env python3
"""Install one reusable generator callout in static blog articles.

There is no shared article template. Run after any article regeneration.
Uses the site's existing Bootstrap card and primary pill-button patterns.
"""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
CTA = '''<!-- TheBizPlanAI CTA start -->
<section class="border rounded-3 p-4 bg-light my-5" data-generator-cta aria-label="Try TheBizPlanAI">
  <h2 class="h4">Try TheBizPlanAI — the free AI business plan generator</h2>
  <p>Create a structured draft plan with an executive summary, market analysis and financial projections.</p>
  <a class="btn btn-primary rounded-pill" href="/business-plan-generator.html">Try TheBizPlanAI</a>
</section>
<!-- TheBizPlanAI CTA end -->'''
BLOCK = re.compile(r'<!-- TheBizPlanAI CTA start -->.*?<!-- TheBizPlanAI CTA end -->\r?\n?', re.S)
AUTHOR = re.compile(r'<h[2-6]\b[^>]*\bid="author"[^>]*>|<(?:section|div)\b[^>]*class="[^"]*\bauthor-card\b[^"]*"[^>]*>')


def render(source):
    source = BLOCK.sub('', source)
    start = re.search(r'<article\b[^>]*>', source)
    if not start:
        return source
    end = source.index('</article>', start.end())
    author = AUTHOR.search(source, start.end(), end)
    at = author.start() if author else end
    newline = '\r\n' if '\r\n' in source else '\n'
    return source[:at] + CTA.replace('\n', newline) + newline + source[at:]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    count = samples = 0
    for page in sorted(ROOT.glob('blog-*.html')):
        if page.name == 'blog-learning-hub.html':
            continue
        source = page.read_bytes().decode('utf-8')
        if '<article' not in source:
            continue  # Legacy redirect, not an article.
        result = render(source)
        if args.check:
            assert result == source, f'CTA drift: {page.name}'
        elif result != source:
            page.write_bytes(result.encode('utf-8'))
        count += 1
        samples += page.name.startswith('blog-sample-')
    print(f'Generator CTA {"verified" if args.check else "installed"} in {count} articles ({samples} sample plans)')


if __name__ == '__main__':
    main()
