#!/usr/bin/env python3
"""Convert site images to descriptively named WebP assets and update references.

Install Pillow before running this script::

    python -m pip install Pillow
    python scripts/convert_images_to_webp.py

Original assets are retained by default so the generated changes can be reviewed
before removal. Pass ``--delete-originals`` after verifying the converted site.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
IMAGE_DIR = ROOT / "img"
MAX_PHOTO_SIZE = (1920, 1920)
WEBP_QUALITY = 80

IMAGE_MAP = {
    "atul-jagga-profile.jpg": "atul-jagga-business-plan-consultant-profile.webp",
    "bizplanlogo.png": "the-biz-plans-business-plan-consulting-logo.webp",
    "blog-learning-hub.jpg": "business-planning-learning-hub.webp",
    "book-business-plan-essentials.jpg": "business-plan-essentials-book-cover.webp",
    "book-financial-due-diligence.jpg": "financial-due-diligence-essentials-book-cover.webp",
    "favicon.ico": "the-biz-plans-website-favicon.webp",
    "hero-bizplans.png": "business-plan-consulting-strategy-session.webp",
    "industry-brewery.jpg": "brewery-business-plan-consulting.webp",
    "industry-fintech.jpg": "fintech-business-plan-consulting.webp",
    "industry-food-franchise.jpg": "food-franchise-business-plan-consulting.webp",
    "industry-marine.jpg": "marine-business-plan-consulting.webp",
    "industry-medical.jpg": "medical-services-business-plan-consulting.webp",
    "industry-mobile-app.jpg": "mobile-app-business-plan-consulting.webp",
    "industry-recruiting.jpg": "recruiting-business-plan-consulting.webp",
    "industry-telecom.jpg": "telecom-business-plan-consulting.webp",
    "pricing.jpg": "business-plan-service-pricing.webp",
    "service-financial-modeling.jpg": "financial-modeling-business-plan-service.webp",
    "service-immigration.jpg": "immigration-business-plan-service.webp",
    "service-investor-lender.jpg": "investor-lender-business-plan-service.webp",
    "service-marketing-strategy.jpg": "marketing-growth-strategy-service.webp",
    "services-overview.jpg": "business-plan-consulting-services-overview.webp",
    "testimonials.jpg": "business-plan-client-testimonials.webp",
    "what-sets-us-apart.jpg": "business-plan-consulting-difference.webp",
    "why-bizplans.jpg": "why-choose-the-biz-plans-consultants.webp",
}

# Preserve the original resolution of assets where automatic photo resizing is
# undesirable. The favicon is resized separately to a browser-appropriate size.
NO_PHOTO_RESIZE = {
    "bizplanlogo.png",
    "book-business-plan-essentials.jpg",
    "book-financial-due-diligence.jpg",
    "favicon.ico",
}


def convert_image(old_name: str, new_name: str) -> None:
    """Convert one source image while preserving transparency when applicable."""
    source = IMAGE_DIR / old_name
    destination = IMAGE_DIR / new_name
    if not source.exists():
        raise FileNotFoundError(f"Missing source image: {source.relative_to(ROOT)}")

    with Image.open(source) as opened:
        image = ImageOps.exif_transpose(opened)
        if old_name == "favicon.ico":
            image.thumbnail((256, 256), Image.Resampling.LANCZOS)
        elif old_name not in NO_PHOTO_RESIZE:
            image.thumbnail(MAX_PHOTO_SIZE, Image.Resampling.LANCZOS)

        has_transparency = image.mode in {"RGBA", "LA"} or "transparency" in image.info
        image = image.convert("RGBA" if has_transparency else "RGB")
        image.save(destination, "WEBP", quality=WEBP_QUALITY, method=6)
        print(f"Converted img/{old_name} -> img/{new_name} ({image.width}x{image.height})")


def update_references() -> None:
    """Replace image paths in HTML, CSS, metadata, and structured data."""
    authored_files = [*ROOT.glob("*.html"), ROOT / "css" / "style.css"]
    for path in authored_files:
        with path.open("r", encoding="utf-8", newline="") as file:
            original = file.read()
        updated = original
        for old_name, new_name in IMAGE_MAP.items():
            updated = updated.replace(f"img/{old_name}", f"img/{new_name}")
        if updated != original:
            with path.open("w", encoding="utf-8", newline="") as file:
                file.write(updated)
            print(f"Updated {path.relative_to(ROOT)}")


def verify_conversion() -> None:
    """Ensure every output exists and no authored old-format reference remains."""
    authored_files = [*ROOT.glob("*.html"), ROOT / "css" / "style.css"]
    failures: list[str] = []
    for old_name, new_name in IMAGE_MAP.items():
        output = IMAGE_DIR / new_name
        if not output.exists() or output.read_bytes()[:4] != b"RIFF":
            failures.append(f"Invalid or missing WebP output: img/{new_name}")
        for path in authored_files:
            with path.open("r", encoding="utf-8", newline="") as file:
                if f"img/{old_name}" in file.read():
                    failures.append(f"{path.relative_to(ROOT)} still references img/{old_name}")
    if failures:
        raise RuntimeError("Conversion verification failed:\n- " + "\n- ".join(failures))
    print(f"Verified {len(IMAGE_MAP)} WebP assets and all authored references.")


def delete_originals() -> None:
    """Delete source assets only after conversion verification succeeds."""
    for old_name in IMAGE_MAP:
        source = IMAGE_DIR / old_name
        if source.exists():
            source.unlink()
            print(f"Deleted img/{old_name}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--delete-originals",
        action="store_true",
        help="remove original JPG, PNG, and ICO assets after successful verification",
    )
    args = parser.parse_args()

    for old_name, new_name in IMAGE_MAP.items():
        convert_image(old_name, new_name)
    update_references()
    verify_conversion()
    if args.delete_originals:
        delete_originals()
    else:
        print("Original assets retained. Re-run with --delete-originals after review.")


if __name__ == "__main__":
    main()
