#!/usr/bin/env python3
"""Build a CSV map of incoming links between the site's HTML pages."""

import argparse
import csv
import posixpath
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        values = dict(attrs)
        href = values.get("href")
        if href:
            self.links.append((href, " ".join(self.get_starttag_text().split())))


def aliases(page: str) -> set[str]:
    values = {page, f"/{page}"}
    if page == "index.html":
        values.update({"", "/"})
    elif page.endswith("/index.html"):
        directory = page[: -len("index.html")]
        values.update({directory, f"/{directory}", directory.rstrip("/"), f"/{directory.rstrip('/')}"})
    else:
        values.update({page[:-5], f"/{page[:-5]}"})
    return values


def build_map(root: Path) -> tuple[list[str], dict[str, set[str]]]:
    pages = sorted(
        path.relative_to(root).as_posix()
        for path in root.rglob("*.html")
        if "node_modules" not in path.parts and ".git" not in path.parts
    )
    lookup = {alias: page for page in pages for alias in aliases(page)}
    incoming: dict[str, set[str]] = defaultdict(set)

    for source in pages:
        parser = LinkParser()
        parser.feed((root / source).read_text(encoding="utf-8", errors="ignore"))
        for href, _ in parser.links:
            parsed = urlparse(href)
            host = parsed.netloc.lower().removeprefix("www.")
            if host and host != "thebizplans.com":
                continue
            if parsed.scheme and parsed.scheme not in {"http", "https"}:
                continue
            path = unquote(parsed.path)
            if not path:
                continue
            if not path.startswith("/"):
                path = posixpath.normpath(posixpath.join(posixpath.dirname(source), path))
            target = lookup.get(path) or lookup.get(path.lstrip("/"))
            if target and target != source:
                incoming[target].add(source)
    return pages, incoming


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="reports/internal-link-map.csv")
    parser.add_argument("--minimum", type=int, default=2)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    pages, incoming = build_map(root)
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(("page", "incoming_page_count", "incoming_pages"))
        for page in pages:
            sources = sorted(incoming[page])
            writer.writerow((page, len(sources), " | ".join(sources)))
    below = [(page, len(incoming[page])) for page in pages if len(incoming[page]) < args.minimum]
    try:
        display_output = output.relative_to(root)
    except ValueError:
        display_output = output
    print(f"Mapped {len(pages)} HTML pages to {display_output}.")
    if below:
        for page, count in below:
            print(f"{page}: {count} incoming links")
        return 1
    print(f"All pages have at least {args.minimum} incoming internal links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
