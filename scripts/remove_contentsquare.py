#!/usr/bin/env python3
"""Remove the third-party Contentsquare tag from every published HTML page.

The tag is hosted with cache headers outside our control. Keeping the cleanup
as a repeatable script prevents generated and hand-authored pages from drifting.
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
TAG = re.compile(
    rb"^[ \t]*<script src=[\"']https://t\.contentsquare\.net/uxa/ffe9231bf84b1\.js[\"']></script>[ \t]*\r?\n?",
    re.MULTILINE,
)
LOADER = re.compile(
    rb"^[ \t]*loadScript\([\"']https://t\.contentsquare\.net/uxa/ffe9231bf84b1\.js[\"']\);[ \t]*\n?",
    re.MULTILINE,
)


def main() -> None:
    changed = 0
    for path in ROOT.glob("*.html"):
        original = path.read_bytes()
        updated = TAG.sub(b"", original)
        updated = LOADER.sub(b"", updated)
        if updated != original:
            path.write_bytes(updated)
            changed += 1

    print(f"Removed Contentsquare from {changed} HTML files")


if __name__ == "__main__":
    main()
