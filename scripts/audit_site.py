#!/usr/bin/env python3
"""Audit the site's crawlability and on-page SEO; optionally write a full report."""
from __future__ import annotations

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
HOST = "https://thebizplans.com"
MAX_IMAGE_BYTES = 4_000_000
RETIRED_EXTERNAL_URL_PREFIXES = {
    "https://dallascityhall.com/departments/sbc/",
    "https://www.canada.ca/en/immigration-refugees-citizenship/services/work-canada/permit",
    "https://www.edc.ca/en/export-help.html",
    "https://www.edc.ca/en/insights-and-resources.html",
    "https://www.gov.nl.ca/immigration/",
    "https://www.gov.nl.ca/industry/",
    "https://www.toronto.ca/business-economy/new-businesses-startups/financing-your-business/",
    "https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/start-visa",
    "https://www.gov.nl.ca/iet/business/",
    "https://futurpreneur.ca/en/offering/",
}


class AuditParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str]] = []
        self.canonicals: list[str] = []
        self.styles: list[str] = []
        self.titles: list[str] = []
        self.h1s: list[str] = []
        self.images: list[dict[str, str]] = []
        self.schemas: list[str] = []
        self.descriptions: list[str] = []
        self.og_urls: list[str] = []
        self.robots: list[str] = []
        self._capture: str | None = None

    def handle_data(self, data: str) -> None:
        if self._capture == "title":
            self.titles.append(data)
        elif self._capture == "h1":
            self.h1s.append(data)
        elif self._capture == "schema":
            self.schemas.append(data)

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = {key: value or "" for key, value in attrs_list}
        if tag == "title":
            self._capture = "title"
        elif tag == "h1":
            self._capture = "h1"
        elif tag == "script" and attrs.get("type", "").lower() == "application/ld+json":
            self._capture = "schema"
        if tag == "meta" and attrs.get("name", "").lower() == "description":
            self.descriptions.append(attrs.get("content", "").strip())
        if tag == "meta" and attrs.get("name", "").lower() == "robots":
            self.robots.extend(value.strip().lower() for value in attrs.get("content", "").split(","))
        if tag == "meta" and attrs.get("name", "").lower() == "keywords":
            errors.append(f"{current_page}: obsolete meta keywords tag")
        if tag == "meta" and attrs.get("property", "").lower() == "og:url":
            self.og_urls.append(attrs.get("content", "").strip())
        if tag == "img":
            self.images.append(attrs)
        if tag in {"a", "img", "script", "link"}:
            key = "href" if tag in {"a", "link"} else "src"
            if attrs.get(key):
                self.refs.append((tag, attrs[key]))
        rel = attrs.get("rel", "").lower().split()
        if tag == "link" and "canonical" in rel:
            self.canonicals.append(attrs.get("href", ""))
        if tag == "link" and "stylesheet" in rel:
            self.styles.append(attrs.get("href", ""))

    def handle_endtag(self, tag: str) -> None:
        if tag in {"title", "h1", "script"}:
            self._capture = None


def local_target(raw: str) -> Path | None:
    """Return a repository-relative target for an internal URL or None for external URLs."""
    url = raw.strip()
    if not url or url.startswith(("#", "mailto:", "tel:", "javascript:", "data:", "//")):
        return None
    parsed = urlsplit(url)
    if parsed.scheme in {"http", "https"} and parsed.netloc not in {"thebizplans.com", "www.thebizplans.com"}:
        return None
    path = unquote(parsed.path)
    if not path or path == "/":
        path = "index.html"
    return Path(path.lstrip("/"))


def schema_nodes(value: object):
    """Yield every JSON-LD object so property/type mistakes cannot hide in a graph."""
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from schema_nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from schema_nodes(child)


def parse_redirects() -> dict[str, str]:
    redirects: dict[str, str] = {}
    source = (ROOT / ".htaccess").read_text(encoding="utf-8")
    for old, new in re.findall(r"RewriteRule\s+\^([^$]+)\$\s+(\S+)\s+\[[^]]*R=30[12][^]]*]", source):
        if "(.*)" not in old:
            redirects[old.replace("\\.", ".")] = new.lstrip("/")
    for old, new in re.findall(r'Redirect\s+30[12]\s+"?([^"\s]+(?: [^"\s]+)*)"?\s+(\S+)', source):
        redirects[old.lstrip("/")] = new.lstrip("/")
    return redirects


def write_report(path: Path, pages: list[Path], links: list[tuple[str, str]], findings: dict[str, list[str]]) -> None:
    lines = ["# Site audit report", "", f"Audited **{len(pages)} HTML URLs** and **{len(links)} internal link occurrences**.", ""]
    lines += ["## All URLs", ""] + [f"- {HOST + ('/' if p.name == 'index.html' else '/' + p.name)}" for p in pages]
    lines += ["", "## Internal links", "", "| Source | Destination |", "| --- | --- |"]
    lines += [f"| `{source}` | `{target}` |" for source, target in sorted(set(links))]
    for heading, items in findings.items():
        lines += ["", f"## {heading}", ""]
        lines += [f"- {item}" for item in items] if items else ["- None."]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


args_parser = argparse.ArgumentParser()
args_parser.add_argument("--report", type=Path, help="write a Markdown inventory and findings report")
args = args_parser.parse_args()
errors: list[str] = []
current_page = ""
redirects = parse_redirects()
# The index.html rule redirects only the explicit duplicate filename. The same
# file still backs `/`, so repository targets normalized to index.html (such as
# `/` and the sitemap homepage URL) remain canonical rather than redirecting.
redirect_sources = set(redirects) - {"index.html"}
htaccess = (ROOT / ".htaccess").read_text(encoding="utf-8")
llms_text = (ROOT / "llms.txt").read_text(encoding="utf-8")
if "www.thebizplans.com" in llms_text:
    errors.append(
        "llms.txt: www hostname conflicts with the canonical apex hostname"
    )
if not re.search(
    r'<FilesMatch "\\\.\(\?:css\|js\)\$">\s*'
    r'Header always set X-Robots-Tag "noindex"\s*</FilesMatch>',
    htaccess,
    re.S,
):
    errors.append(
        ".htaccess: CSS and JavaScript responses must send X-Robots-Tag noindex"
    )
# A redirect source is not a deployable HTML page: Apache serves the redirect
# before its on-disk document. Exclude such files from every indexability check
# so an obsolete file cannot be encouraged to self-canonicalize or enter the
# sitemap merely because it still exists in the repository.
pages = sorted(page for page in ROOT.glob("*.html") if page.name not in redirect_sources)
page_names = {page.name for page in pages}
canonical_urls: set[str] = set()
seen_titles: dict[str, str] = {}
seen_h1s: dict[str, str] = {}
seen_descriptions: dict[str, str] = {}
internal_links: list[tuple[str, str]] = []
inbound: Counter[str] = Counter()
missing_alt: list[str] = []
unoptimized_images: list[str] = []
missing_schema: list[str] = []
shared_markup: dict[str, dict[str, list[str]]] = {
    "header": {},
    "footer": {},
}

for page in pages:
    current_page = page.name
    source = page.read_text(encoding="utf-8")
    parser = AuditParser()
    parser.feed(source)
    expected = HOST + ("/" if page.name == "index.html" else "/" + page.name)
    if parser.canonicals != [expected]:
        errors.append(f"{page.name}: canonical must be {expected}")
    # Utility pages intentionally excluded from search results are outside the
    # indexable-page on-page SEO contract. They still require a canonical so
    # hostname and protocol variants do not create duplicate URL signals.
    if "noindex" in parser.robots:
        continue
    header = re.search(r'<div class="container-fluid sticky-top(?: global-header)?">.*?</nav>\s*</div>\s*</div>', source, re.S)
    footer = re.search(r"<footer\b.*?</footer>", source, re.S)
    if not header or not footer:
        errors.append(f"{page.name}: missing shared header or footer")
    for component, match in (("header", header), ("footer", footer)):
        if match:
            shared_markup[component].setdefault(match.group(), []).append(page.name)
    for tag, raw in parser.refs:
        if tag == "a" and any(
            raw == retired or raw.startswith(f"{retired}/")
            for retired in RETIRED_EXTERNAL_URL_PREFIXES
        ):
            errors.append(f"{page.name}: link uses retired external URL {raw}")
        target = local_target(raw)
        if target is None:
            continue
        if tag == "a":
            internal_links.append((page.name, target.as_posix()))
            if target.name in page_names and target.name != page.name:
                inbound[target.name] += 1
        if not (ROOT / target).exists():
            errors.append(f"{page.name}: broken {tag} target {raw}")
    for image in parser.images:
        src = image.get("src", "(missing src)")
        if "alt" not in image or not image["alt"].strip():
            missing_alt.append(f"{page.name}: {src}")
        if image.get("loading", "").lower() != "lazy":
            unoptimized_images.append(f"{page.name}: {src} is not lazy-loaded")
        for dimension in ("width", "height"):
            value = image.get(dimension, "")
            if not value.isdigit() or int(value) < 1:
                unoptimized_images.append(f"{page.name}: {src} has no valid {dimension}")
    canonical_urls.add(expected)
    required_css = {"css/bootstrap.min.css", "css/style.min.css"}
    if not required_css.issubset(parser.styles):
        errors.append(f"{page.name}: missing shared CSS")
    title = " ".join("".join(parser.titles).split())
    if not title:
        errors.append(f"{page.name}: missing title")
    elif title in seen_titles:
        errors.append(f"{page.name}: duplicate title also used by {seen_titles[title]}")
    else:
        seen_titles[title] = page.name
    h1 = " ".join("".join(parser.h1s).split())
    if len(parser.h1s) != 1 or not h1:
        errors.append(f"{page.name}: expected one non-empty h1, found {len(parser.h1s)}")
    elif h1 in seen_h1s:
        errors.append(f"{page.name}: duplicate h1 also used by {seen_h1s[h1]}")
    else:
        seen_h1s[h1] = page.name
    if len(parser.descriptions) != 1 or not parser.descriptions[0]:
        errors.append(f"{page.name}: must have one non-empty meta description")
    elif parser.descriptions[0] in seen_descriptions:
        errors.append(f"{page.name}: duplicate description also used by {seen_descriptions[parser.descriptions[0]]}")
    else:
        seen_descriptions[parser.descriptions[0]] = page.name
    if parser.og_urls and parser.og_urls != [expected]:
        errors.append(f"{page.name}: og:url must be {expected}")
    valid_schema = False
    for raw_schema in parser.schemas:
        try:
            schema_data = json.loads(raw_schema.strip())
            valid_schema = bool(schema_data) or valid_schema
            for node in schema_nodes(schema_data):
                node_types = node.get("@type", [])
                if isinstance(node_types, str):
                    node_types = [node_types]
                if "serviceType" in node and "Service" not in node_types:
                    errors.append(
                        f"{page.name}: serviceType is only valid on a Service schema"
                    )
                if "HowTo" in node_types:
                    if not str(node.get("name", "")).strip():
                        errors.append(f"{page.name}: HowTo schema has no name")
                    if not node.get("step"):
                        errors.append(f"{page.name}: HowTo schema has no steps")
                if {"LocalBusiness", "ProfessionalService"}.intersection(node_types):
                    if not node.get("address"):
                        errors.append(
                            f"{page.name}: local business schema has no address"
                        )
        except json.JSONDecodeError:
            errors.append(f"{page.name}: invalid JSON-LD schema")
    if not valid_schema:
        missing_schema.append(page.name)

for item in missing_alt:
    errors.append(f"{item}: image has missing or empty alt text")
for item in unoptimized_images:
    errors.append(f"unoptimized image: {item}")
for item in missing_schema:
    errors.append(f"{item}: page has no valid JSON-LD schema")

# A static site can only keep copied global components maintainable when drift is
# caught immediately. Include the pages in each variant in the error so a
# developer can identify and repair the outliers without manually diffing every
# document.
for component, variants in shared_markup.items():
    if len(variants) > 1:
        distribution = "; ".join(
            f"{len(files)} page(s): {', '.join(sorted(files))}"
            for files in variants.values()
        )
        errors.append(
            f"shared {component} has {len(variants)} variants ({distribution})"
        )

oversized = [f"{p.relative_to(ROOT)} ({p.stat().st_size:,} bytes)" for p in (ROOT / "img").glob("*") if p.is_file() and p.stat().st_size > MAX_IMAGE_BYTES]
for item in oversized:
    errors.append(f"oversized image: {item}; limit is {MAX_IMAGE_BYTES:,} bytes")

orphans = sorted(page_names - {"index.html"} - set(inbound))
for item in orphans:
    errors.append(f"{item}: orphan page with no incoming internal link")

redirect_chains: list[str] = []
for source, target in redirects.items():
    visited = {source}
    route = [source, target]
    while target in redirects:
        if target in visited:
            route.append("CYCLE")
            break
        visited.add(target)
        target = redirects[target]
        route.append(target)
    if len(route) > 2:
        redirect_chains.append(" -> ".join(route))
for route in redirect_chains:
    errors.append(f"redirect chain: {route}")
for source, target in internal_links:
    if target in redirect_sources:
        errors.append(f"{source}: internal link points through redirect {target}")

namespace = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
sitemap_root = ET.parse(ROOT / "sitemap.xml")
sitemap = {node.text for node in sitemap_root.findall(".//s:loc", namespace)}
for entry in sitemap_root.findall(".//s:url", namespace):
    location = entry.findtext("s:loc", namespaces=namespace) or "(missing loc)"
    lastmod = entry.findtext("s:lastmod", namespaces=namespace) or ""
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", lastmod):
        errors.append(f"sitemap URL has missing or invalid lastmod: {location}")
sitemap_redirect_sources = {
    url
    for url in sitemap
    if (target := local_target(url)) is not None and target.as_posix() in redirect_sources
}
for url in sorted(sitemap_redirect_sources):
    errors.append(f"sitemap URL must not be a redirect source: {url}")
if sitemap != canonical_urls:
    errors.append(f"sitemap mismatch: missing={sorted(canonical_urls - sitemap)}, extra={sorted(sitemap - canonical_urls)}")

findings = {
    "Broken links": sorted(error for error in errors if "broken " in error),
    "Orphan pages / pages not linked anywhere": orphans,
    "Duplicate titles": [error for error in errors if "duplicate title" in error],
    "Duplicate H1s": [error for error in errors if "duplicate h1" in error],
    "Missing H1s": [error for error in errors if "expected one non-empty h1" in error],
    "Images without alt tags": missing_alt,
    "Images without complete optimization attributes": unoptimized_images,
    f"Oversized images (over {MAX_IMAGE_BYTES:,} bytes)": oversized,
    "Missing canonical URLs": [error for error in errors if "canonical must" in error],
    "Redirect chains": redirect_chains,
    "Pages without schema": missing_schema,
}
if args.report:
    report_path = args.report if args.report.is_absolute() else ROOT / args.report
    write_report(report_path, pages, internal_links, findings)
    print(f"Wrote {report_path.relative_to(ROOT)}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(canonical_urls)} indexable URLs, {len(internal_links)} internal links, no crawlability or on-page SEO issues.")
