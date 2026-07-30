#!/usr/bin/env python3
"""Remove the full-page loading spinner from every static page."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SPINNER_PATTERN = re.compile(
    r"\s*(?:<!-- Spinner -->\s*)?"
    r'<div id="spinner".*?</div>\s*</div>\s*',
    re.DOTALL,
)


def main() -> None:
    updated = 0
    for page in ROOT.glob("*.html"):
        source = page.read_bytes().decode("utf-8")
        newline = "\r\n" if "\r\n" in source else "\n"
        result, count = SPINNER_PATTERN.subn(newline * 2 + "  ", source, count=1)
        if count:
            page.write_bytes(result.encode("utf-8"))
            updated += 1

    remaining = [page.name for page in ROOT.glob("*.html") if 'id="spinner"' in page.read_text(encoding="utf-8")]
    if remaining:
        raise RuntimeError(f"Spinner remains in: {', '.join(remaining)}")
    print(f"Removed loading spinner from {updated} pages")


if __name__ == "__main__":
    main()
