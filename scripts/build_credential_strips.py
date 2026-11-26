#!/usr/bin/env python3
"""Refresh the shared under-H1 credential strip in commercial HTML pages."""
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

IMMIGRATION_PAGES = set("""
aaip-entrepreneur-business-plan.html bcpnp-business-plan.html
e2-visa-business-plan.html e2-visa-business-plan-cost.html
eb2-niw-business-plan.html eb5-business-plan-service.html ict-business-plan.html
immigration-business-plans.html l1-visa-business-plan.html
lmia-owner-operator-business-plan.html mpnp-business-plan.html nbpnp-business-plan.html
nsnp-business-plan.html oinp-business-plan.html self-employed-business-plan.html
sinp-business-plan.html startup-visa-business-plan.html
""".split())

FINANCING_PAGES = set("""
business-development-bank-of-canada.html canada-small-business-financing-program.html canadian-agricultural-loans-act.html
farm-credit-canada.html futurpreneur.html black-entrepreneurship.html
indigenous-aboriginal-entrepreneurship.html women-entrepreneurship-loan-fund.html export-development-canada.html
royal-bank-of-canada.html td-canada-trust.html scotiabank.html
cibc.html national-bank-of-canada.html desjardins.html
vancity-business-plan.html private-lender-alternative-financing.html
""".split())

SERVICE_PAGES = set("""
about-business-plan.html bank-loan-business-plans.html best-business-plan-writers-canada.html
brewery-business-plans.html business-plan-review.html business-plan-writing-services.html
cim-services.html dealership-business-plans.html feasibility-study-services.html
financial-modeling.html fintech-business-plans.html food-franchise-business-plans.html
fractional-cfo-services.html franchise-business-plans.html index.html
indigenous-business-plan.html innovation-business-plan.html investor-business-plan.html
marine-business-plans.html marketing-growth-strategy.html medical-services-business-plans.html
mobile-app-business-plans.html partner-buyout-business-plan.html pricing.html
recruiting-business-plans.html sba-business-plan.html services.html strategic-business-plan.html
telecom-business-plans.html us-business-plans.html
""".split())

AFTER_HEADING = re.compile(
    r"(</h1>)(?:\s*<p class=\"credential-strip\"[^>]*>[^<]*</p>)?",
    re.IGNORECASE,
)


def credential_strip(*, immigration=False):
    credentials = (
        "Led by Atul Jagga — CPA (Ontario) · RCIC-IRB · "
        "MBA Finance &amp; Strategy (UBC) · 20+ years in corporate finance"
    )
    if immigration:
        credentials += " · CICC licence R711106"
    return f'<p class="credential-strip" style="font-size: .875em">{credentials}</p>'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing HTML")
    args = parser.parse_args()
    city_pages = {path.name for path in ROOT.glob("*-business-plan-writers.html")}
    city_pages.add("business-plan-writers-near-me.html")
    city_pages.discard("scarborough-business-plan-writers.html")  # Legacy redirect.
    pages = SERVICE_PAGES | IMMIGRATION_PAGES | FINANCING_PAGES | city_pages
    stale = []
    for name in sorted(pages):
        path = ROOT / name
        with path.open(encoding="utf-8", newline="") as source:
            original = source.read()
        strip = credential_strip(immigration=name in IMMIGRATION_PAGES)
        updated, count = AFTER_HEADING.subn(lambda match: match[1] + strip, original)
        if count != 1:
            raise ValueError(f"Expected one H1 in {name}, found {count}")
        if original != updated:
            stale.append(name)
            if not args.check:
                with path.open("w", encoding="utf-8", newline="") as target:
                    target.write(updated)
    if args.check and stale:
        parser.exit(1, "Refresh credential strips in " + ", ".join(stale) + "\n")


if __name__ == "__main__":
    main()
