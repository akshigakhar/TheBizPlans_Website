#!/usr/bin/env python3
"""Fail when local links/assets, canonical URLs, or sitemap entries drift."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re, sys, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
HOST='https://thebizplans.com'
class AuditParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]; self.canonicals=[]; self.styles=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag in {'a','img','script','link'}:
            key='href' if tag in {'a','link'} else 'src'
            if attrs.get(key): self.refs.append((tag,attrs[key]))
        rel=attrs.get('rel','').split()
        if tag=='link' and 'canonical' in rel: self.canonicals.append(attrs.get('href',''))
        if tag=='link' and 'stylesheet' in rel: self.styles.append(attrs.get('href',''))
errors=[]; canonical_urls=set(); html_files=sorted(ROOT.glob('*.html'))
shared_headers=set(); shared_footers=set()
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
