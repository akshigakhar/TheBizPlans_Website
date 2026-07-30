#!/usr/bin/env python3
"""Fail CI when deployed images regress accessibility or byte budgets."""
from __future__ import annotations
import argparse
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RASTER_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".avif"}
SOURCE_SUFFIXES = {".jpg", ".jpeg", ".png"}

class ImageParser(HTMLParser):
    def __init__(self, path: Path) -> None:
        super().__init__(); self.path=path; self.errors=[]
    def handle_starttag(self, tag, attrs):
        if tag != "img": return
        values=dict(attrs); src=values.get("src", "")
        for name in ("width", "height", "decoding"):
            if name not in values: self.errors.append(f"{self.path.relative_to(ROOT)}: <img src=\"{src}\"> lacks {name}")
        if values.get("loading") not in {"lazy", "eager"}: self.errors.append(f"{self.path.relative_to(ROOT)}: <img src=\"{src}\"> lacks loading policy")

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max-image-kb",type=int,default=500)
    ap.add_argument("--max-hero-kb",type=int,default=250)
    args=ap.parse_args(); errors=[]
    for path in ROOT.glob("*.html"):
        parser=ImageParser(path); parser.feed(path.read_text(encoding="utf-8")); errors.extend(parser.errors)
    for path in (ROOT/"img").iterdir():
        if path.suffix.lower() not in RASTER_SUFFIXES: continue
        limit=args.max_hero_kb if "hero" in path.name or "strategy-session" in path.name else args.max_image_kb
        if path.stat().st_size > limit*1024: errors.append(f"{path.relative_to(ROOT)}: {path.stat().st_size/1024:.0f} KB exceeds {limit} KB")
    if errors:
        print("Image budget failed:\n- " + "\n- ".join(errors)); return 1
    print("Image budget passed: intrinsic dimensions, loading policy, decoding, and file sizes verified."); return 0
if __name__ == "__main__": raise SystemExit(main())
