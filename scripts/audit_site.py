#!/usr/bin/env python3
"""Fail when local links/assets, canonical URLs, or sitemap entries drift."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json, re, sys, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
HOST='https://thebizplans.com'
class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]; self.canonicals=[]; self.styles=[]; self.titles=[]; self.descriptions=[]; self.h1_count=0; self.og_urls=[]
    def handle_data(self, data):
        if getattr(self, '_in_title', False): self.titles.append(data)
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag == 'title': self._in_title=True
        if tag == 'h1': self.h1_count += 1
        if tag == 'meta' and attrs.get('name','').lower() == 'description': self.descriptions.append(attrs.get('content','').strip())
        if tag == 'meta' and attrs.get('name','').lower() == 'keywords': errors.append(f'{page.name}: obsolete meta keywords tag')
        if tag == 'meta' and attrs.get('property','').lower() == 'og:url': self.og_urls.append(attrs.get('content','').strip())
        if tag in {'a','img','script','link'}:
            key='href' if tag in {'a','link'} else 'src'
            if attrs.get(key): self.refs.append((tag,attrs[key]))
        rel=attrs.get('rel','').split()
        if tag=='link' and 'canonical' in rel: self.canonicals.append(attrs.get('href',''))
        if tag=='link' and 'stylesheet' in rel: self.styles.append(attrs.get('href',''))
    def handle_endtag(self, tag):
        if tag == 'title': self._in_title=False
errors=[]; canonical_urls=set(); html_files=sorted(ROOT.glob('*.html')); seen_titles={}; seen_descriptions={}
shared_headers=set(); shared_footers=set()
commercial_landing_pages={
    'bank-loan-business-plans.html','black-entrepreneurship.html',
    'business-development-bank-of-canada.html','business-plan-review.html',
    'canada-small-business-financing-program.html','canadian-agricultural-loans-act.html',
    'cibc.html','desjardins.html',
    'export-development-canada.html','farm-credit-canada.html','financial-modeling.html',
    'futurpreneur.html','ict-business-plan.html','immigration-business-plans.html',
    'indigenous-aboriginal-entrepreneurship.html','innovation-business-plan.html',
    'investor-business-plan.html','lmia-owner-operator-business-plan.html',
    'marketing-growth-strategy.html',
    'national-bank-of-canada.html','private-lender-alternative-financing.html',
    'royal-bank-of-canada.html','scotiabank.html','strategic-business-plan.html',
    'self-employed-business-plan.html','startup-visa-business-plan.html',
    'td-canada-trust.html','vancity-business-plan.html',
    'women-entrepreneurship-loan-fund.html'
}
financing_pages={
    'bank-loan-business-plans.html','business-development-bank-of-canada.html',
    'canada-small-business-financing-program.html','canadian-agricultural-loans-act.html',
    'farm-credit-canada.html','futurpreneur.html','black-entrepreneurship.html',
    'indigenous-aboriginal-entrepreneurship.html','women-entrepreneurship-loan-fund.html',
    'private-lender-alternative-financing.html','export-development-canada.html',
    'royal-bank-of-canada.html','td-canada-trust.html','scotiabank.html','cibc.html',
    'national-bank-of-canada.html','desjardins.html','vancity-business-plan.html'
}
financing_pathways={}
for page in html_files:
    source=page.read_text(encoding='utf-8'); parser=AuditParser(); parser.feed(source)
    header=re.search(r'<div class="container-fluid sticky-top">.*?</nav>\s*</div>\s*</div>',source,re.S)
    footer=re.search(r'<footer\b.*?</footer>',source,re.S)
    if not header or not footer: errors.append(f'{page.name}: missing shared header or footer')
    else: shared_headers.add(header.group(0)); shared_footers.add(footer.group(0))
    for tag,raw in parser.refs:
        url=raw.strip()
        if not url or url.startswith(('#','mailto:','tel:','javascript:','data:','http://','https://','//')): continue
        path=unquote(urlsplit(url).path)
        if path and not (ROOT/path.lstrip('/')).exists(): errors.append(f'{page.name}: missing {tag} target {raw}')
    expected=HOST+('/' if page.name=='index.html' else '/'+page.name)
    if parser.canonicals != [expected]: errors.append(f'{page.name}: canonical must be {expected}')
    else: canonical_urls.add(expected)
    required={'css/bootstrap.min.css','css/style.css'}
    if not required.issubset(set(parser.styles)): errors.append(f'{page.name}: missing shared CSS: {sorted(required-set(parser.styles))}')
    if len(parser.styles) != len(set(parser.styles)): errors.append(f'{page.name}: duplicate stylesheet links')
    title=''.join(parser.titles).strip()
    if not title: errors.append(f'{page.name}: missing title')
    elif title in seen_titles: errors.append(f'{page.name}: duplicate title also used by {seen_titles[title]}')
    else: seen_titles[title]=page.name
    if len(parser.descriptions) != 1 or not parser.descriptions[0]: errors.append(f'{page.name}: must have one non-empty meta description')
    elif parser.descriptions[0] in seen_descriptions: errors.append(f'{page.name}: duplicate description also used by {seen_descriptions[parser.descriptions[0]]}')
    else: seen_descriptions[parser.descriptions[0]]=page.name
    if parser.h1_count != 1: errors.append(f'{page.name}: expected one h1, found {parser.h1_count}')
    if parser.og_urls and parser.og_urls != [expected]: errors.append(f'{page.name}: og:url must be {expected}')
    if page.name != 'faqs.html':
        faq=re.search(r'<!-- PAGE-FAQ:START -->(.*?)<!-- PAGE-FAQ:END -->',source,re.S)
        if not faq: errors.append(f'{page.name}: missing generated page FAQ')
        else:
            visible_count=faq.group(1).count('<details ')
            if not 5 <= visible_count <= 10: errors.append(f'{page.name}: expected 5-10 visible FAQs, found {visible_count}')
            schemas=re.findall(r'<script type="application/ld\+json" data-page-faq>(.*?)</script>',faq.group(1),re.S)
            try:
                schema_count=len(json.loads(schemas[0]).get('mainEntity',[])) if len(schemas) == 1 else -1
            except json.JSONDecodeError:
                schema_count=-1
            if schema_count != visible_count: errors.append(f'{page.name}: FAQPage schema does not match visible FAQs')
    needs_pathway = page.name in commercial_landing_pages or (page.name.startswith('blog-') and page.name != 'blog-learning-hub.html')
    if needs_pathway and source.count('<!-- COMMERCIAL-PATHWAY:START -->') != 1:
        errors.append(f'{page.name}: missing one commercial pathway')
    if source.count('<!-- COMMERCIAL-PATHWAY:START -->') != source.count('<!-- COMMERCIAL-PATHWAY:END -->'):
        errors.append(f'{page.name}: unbalanced commercial pathway markers')
    if page.name in financing_pages:
        pathway=re.search(r'<!-- COMMERCIAL-PATHWAY:START -->(.*?)<!-- COMMERCIAL-PATHWAY:END -->',source,re.S)
        if not pathway: errors.append(f'{page.name}: missing financing service content')
        else:
            financing_pathways[page.name]=pathway.group(1)
            if 'business plan FAQ' not in pathway.group(1) and 'business plan FAQs' not in pathway.group(1):
                errors.append(f'{page.name}: missing visible financing FAQ section')
            for target in {'financial-modeling.html','business-plan-review.html','sample-other-plan.html','https://calendly.com/atul_jagga/business-plan-free-consult'}:
                if f'href="{target}"' not in pathway.group(1): errors.append(f'{page.name}: financing pathway missing {target}')
            if page.name != 'bank-loan-business-plans.html' and 'href="bank-loan-business-plans.html"' not in pathway.group(1):
                errors.append(f'{page.name}: financing pathway missing bank-loan-business-plans.html')
            if pathway.group(1).count('class="btn ') < 3:
                errors.append(f'{page.name}: financing pathway needs at least three CTA buttons')
if len(financing_pathways) == len(financing_pages):
    # Exact duplicates are an editorial regression: structure may repeat, lender guidance may not.
    bodies={re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',body)).strip():name for name,body in financing_pathways.items()}
    if len(bodies) != len(financing_pathways): errors.append('financing pages contain duplicate commercial content')
if len(shared_headers) != 1: errors.append(f'header copies differ ({len(shared_headers)} variants)')
if len(shared_footers) != 1: errors.append(f'footer copies differ ({len(shared_footers)} variants)')
# CSS url() assets (skip embedded and external URLs).
for sheet in (ROOT/'css').glob('*.css'):
    for raw in re.findall(r'url\(["\']?([^"\')]+)',sheet.read_text(encoding='utf-8')):
        if raw.startswith(('data:','http:','https:','#')): continue
        if not (sheet.parent/unquote(urlsplit(raw).path)).resolve().exists(): errors.append(f'{sheet.relative_to(ROOT)}: missing background {raw}')
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
sitemap={node.text for node in ET.parse(ROOT/'sitemap.xml').findall('.//s:loc',ns)}
if sitemap != canonical_urls:
    errors.append(f'sitemap mismatch: missing={sorted(canonical_urls-sitemap)}, extra={sorted(sitemap-canonical_urls)}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'OK: {len(html_files)} pages, {len(canonical_urls)} canonical URLs, and all local assets validated.')
