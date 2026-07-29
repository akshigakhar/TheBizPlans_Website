#!/usr/bin/env python3
"""Build a six-link, topic-aware discovery trail on every public HTML page.

The lists below are deliberately curated rather than inferred from page copy. This
keeps link destinations predictable, prevents self-links, and makes the generated
block safe to rebuild whenever pages are edited.
"""
from __future__ import annotations

from html import unescape
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
START = "<!-- RELATED-PAGES:START -->"
END = "<!-- RELATED-PAGES:END -->"
LINK_COUNT = 6

INDUSTRIES = (
    "beauty-salon", "cannabis", "construction", "daycare", "grocery", "hvac",
    "logistics", "manufacturing", "nail-salon", "pharmacy", "plumbing", "trucking",
)
INDUSTRY_SUFFIXES = (
    "business-plans", "financial-projections", "pitch-decks", "loans",
    "investors", "cost-calculator", "franchises",
)

LEARNING = [
    "business-plan-essentials.html", "chapter-1-structuring-your-business-plan.html",
    "chapter-2-executive-summary.html", "chapter-3-market-research.html",
    "chapter-4-business-model.html", "chapter-5-marketing-sales.html",
    "chapter-6-operations.html", "chapter-7-financial-forecasting.html",
    "chapter-8-writing-for-audiences.html", "chapter-9-common-mistakes.html",
    "chapter-10-presenting-your-plan.html", "blog-learning-hub.html",
]
FINANCING = [
    "bank-loan-business-plans.html", "how-banks-evaluate-business-plans.html",
    "financial-modeling.html", "business-plan-cost-timeline-checklist.html",
    "canada-small-business-financing-program.html",
    "private-lender-alternative-financing.html", "project-brief.html", "contact.html",
]
IMMIGRATION = [
    "immigration-business-plans.html", "startup-visa-business-plan.html",
    "ict-business-plan.html", "lmia-owner-operator-business-plan.html",
    "self-employed-business-plan.html", "oinp-business-plan.html",
    "bcpnp-business-plan.html", "sinp-business-plan.html", "project-brief.html",
]
SERVICES = [
    "services.html", "bank-loan-business-plans.html", "investor-business-plan.html",
    "financial-modeling.html", "strategic-business-plan.html",
    "marketing-growth-strategy.html", "business-plan-review.html", "project-brief.html",
]
COMPANY = [
    "about-business-plan.html", "services.html", "pricing.html", "case-studies.html",
    "testimonials.html", "faqs.html", "editorial-policy.html", "contact.html",
]

SERVICE_NAMES = {
    "services.html", "investor-business-plan.html", "strategic-business-plan.html",
    "innovation-business-plan.html", "business-plan-review.html",
    "marketing-growth-strategy.html", "financial-due-diligence-essentials.html",
    "industry-business-plans.html", "sample-other-plan.html",
}
COMPANY_NAMES = {
    "index.html", "about-business-plan.html", "pricing.html", "case-studies.html",
    "testimonials.html", "faqs.html", "contact.html", "project-brief.html",
    "editorial-policy.html", "authoritative-resources.html", "privacy-policy.html",
    "terms.html", "refund-policy.html", "books.html",
}


def title(path: Path) -> str:
    """Use the visible H1 as concise, descriptive anchor text."""
    match = re.search(r"<h1(?:\s[^>]*)?>(.*?)</h1>", read(path), re.I | re.S)
    if not match:
        raise ValueError(f"{path.name} has no H1")
    return unescape(re.sub(r"<[^>]+>", "", match.group(1))).strip()


def read(path: Path) -> str:
    with path.open(encoding="utf-8", newline="") as handle:
        return handle.read()


def write(path: Path, source: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(source)


def candidates(name: str) -> list[str]:
    """Return the most specific curated cluster available for a page."""
    for industry in INDUSTRIES:
        if name.startswith(industry + "-"):
            siblings = [f"{industry}-{suffix}.html" for suffix in INDUSTRY_SUFFIXES]
            return siblings + ["industry-business-plans.html", "contact.html"]

    if name in LEARNING or name.startswith("blog-"):
        if "executive-summary" in name:
            return ["chapter-2-executive-summary.html", "blog-executive-summary-key-elements.html",
                    "blog-executive-summary-dos-donts.html", "blog-executive-summary-tips.html",
                    "investor-business-plan.html", "financial-modeling.html", "blog-learning-hub.html"]
        if any(term in name for term in ("market", "competitor", "industry-analysis", "swot")):
            return ["chapter-3-market-research.html", "blog-why-market-research-matters.html",
                    "blog-identifying-target-market.html", "blog-analyzing-competitors.html",
                    "marketing-growth-strategy.html", "strategic-business-plan.html", "blog-learning-hub.html"]
        return LEARNING + ["business-plan-review.html", "contact.html"]

    if name in IMMIGRATION or name.endswith("pnp-business-plan.html") or name == "aaip-entrepreneur-business-plan.html":
        return IMMIGRATION

    if (name in FINANCING or any(token in name for token in
            ("bank", "credit", "lender", "loan-fund", "entrepreneurship", "vancity", "cibc", "scotiabank", "desjardins"))):
        return FINANCING

    if name in SERVICE_NAMES or name.endswith("-business-plans.html"):
        return SERVICES

    if name in COMPANY_NAMES:
        return COMPANY

    return SERVICES + COMPANY


def related(name: str, existing: set[str]) -> list[str]:
    choices: list[str] = []
    # Candidate lists may intentionally overlap; preserve editorial order.
    for destination in candidates(name) + SERVICES + COMPANY:
        if destination != name and destination in existing and destination not in choices:
            choices.append(destination)
        if len(choices) == LINK_COUNT:
            return choices
    raise ValueError(f"Could not find {LINK_COUNT} related destinations for {name}")


def block(destinations: list[str], labels: dict[str, str]) -> str:
    links = "\n".join(
        f'        <li><a href="{destination}">{labels[destination]}</a></li>'
        for destination in destinations
    )
    return f'''{START}
<aside class="related-pages" aria-labelledby="related-pages-heading">
  <div class="container">
    <p class="section-kicker">Keep exploring</p>
    <h2 id="related-pages-heading">Related business planning resources</h2>
    <p>Continue with the next practical step, from research and projections to funding and review.</p>
    <ul>
{links}
    </ul>
  </div>
</aside>
{END}'''


def main() -> None:
    pages = sorted(ROOT.glob("*.html"))
    existing = {page.name for page in pages}
    labels = {page.name: title(page) for page in pages}
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)

    for page in pages:
        source = read(page)
        # Generated fragments use LF even when a legacy page contains isolated
        # CRLF lines; rewriting the surrounding source would create noisy diffs.
        newline = "\n"
        generated = block(related(page.name, existing), labels)
        if pattern.search(source):
            source = pattern.sub(generated, source)
        else:
            footer = re.search(r"<footer\b", source, re.I)
            if not footer:
                raise ValueError(f"{page.name} has no footer")
            source = source[:footer.start()] + generated + newline + source[footer.start():]
        # A few legacy templates start the footer with a lone CRLF line. Once
        # that line becomes part of the diff, Git treats its carriage return as
        # trailing whitespace, so normalize only this generated-block boundary.
        source = re.sub(r"(<footer\b[^>]*>)\r\n", r"\1\n", source, count=1, flags=re.I)
        write(page, source)

    print(f"Added {LINK_COUNT} curated related-page links to {len(pages)} pages.")


if __name__ == "__main__":
    main()
