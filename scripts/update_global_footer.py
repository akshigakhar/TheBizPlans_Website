#!/usr/bin/env python3
"""Install the shared, curated site footer on every static page."""

from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]


def links(items: list[tuple[str, str]]) -> str:
    return "\n".join(f'              <li><a href="{href}">{label}</a></li>' for label, href in items)


def group(title: str, items: list[tuple[str, str]], visible: int | None = None, disclosure_label: str | None = None) -> str:
    group_id = title.lower().replace(" ", "-")
    visible = visible or len(items)
    primary, additional = items[:visible], items[visible:]
    additional_markup = ""
    if additional:
        disclosure_label = disclosure_label or title
        additional_id = f"footer-{group_id}-additional"
        additional_markup = f'''\n            <li class="site-footer__additional" id="{additional_id}" hidden><ul>
{links(additional)}
            </ul></li>
            <li class="site-footer__more-item"><button class="site-footer__more" type="button" aria-expanded="false" aria-controls="{additional_id}" data-label-more="See All {disclosure_label}" data-label-less="Show Fewer {disclosure_label}">See All {disclosure_label}</button></li>'''
    return f'''        <nav class="site-footer__group" aria-label="{title}">
          <h2>{title}</h2>
          <button class="site-footer__category-toggle" type="button" aria-expanded="true" aria-controls="footer-{group_id}-links">{title}</button>
          <ul id="footer-{group_id}-links" class="site-footer__links">
{links(primary)}{additional_markup}
          </ul>
        </nav>'''


GROUPS = [
    ("Services", [("Business Plan Writing Services", "services.html"), ("Bank Loan Business Plans", "bank-loan-business-plans.html"), ("Investor Business Plans", "investor-business-plan.html"), ("Strategic Business Plans", "strategic-business-plan.html"), ("Financial Modelling", "financial-modeling.html"), ("Business Plan Review", "business-plan-review.html"), ("Feasibility Studies", "feasibility-study-services.html"), ("Confidential Information Memorandums", "cim-services.html"), ("Immigration Business Plans", "immigration-business-plans.html"), ("U.S. Business Plans", "us-business-plans.html")]),
    ("Financing", [("Financing Resource Centre", "small-business-financing-canada.html"), ("Business Loans in Canada", "business-loans-canada.html"), ("Bank Loan Business Plans", "bank-loan-business-plans.html"), ("CSBFP", "canada-small-business-financing-program.html"), ("BDC", "business-development-bank-of-canada.html"), ("RBC", "royal-bank-of-canada.html"), ("TD", "td-canada-trust.html"), ("Scotiabank", "scotiabank.html"), ("CIBC", "cibc.html"), ("FCC", "farm-credit-canada.html")], 6, "Financing Resources"),
    ("Industries", [("Industry Business Plans", "industry-business-plans.html"), ("Construction", "construction-business-plans.html"), ("Daycare", "daycare-business-plans.html"), ("Food Franchise", "food-franchise-business-plans.html"), ("Medical Services", "medical-services-business-plans.html"), ("Trucking", "trucking-business-plans.html"), ("Brewery", "brewery-business-plans.html"), ("Fintech", "fintech-business-plans.html"), ("Innovation", "innovation-business-plan.html"), ("Marine", "marine-business-plans.html"), ("Mobile App", "mobile-app-business-plans.html"), ("Recruiting", "recruiting-business-plans.html"), ("Telecom", "telecom-business-plans.html")], 6),
    ("Free Resources", [("Free Business Plan Templates", "business-plan-template.html"), ("Free Business Plan Generator", "business-plan-generator.html"), ("Business Plan Essentials", "business-plan-essentials.html"), ("Learning Centre", "blog-learning-hub.html"), ("Sample Business Plans", "sample-business-plans.html")]),
    # There is no city hub, so keep every city in the DOM behind an in-place
    # disclosure rather than pointing the control at an invented URL.
    ("Locations", [("Toronto", "toronto-business-plan-writers.html"), ("Vancouver", "vancouver-business-plan-writers.html"), ("Calgary", "calgary-business-plan-writers.html"), ("Ottawa", "ottawa-business-plan-writers.html"), ("Edmonton", "edmonton-business-plan-writers.html"), ("Montreal", "montreal-business-plan-writers.html"), ("Mississauga", "mississauga-business-plan-writers.html"), ("Brampton", "brampton-business-plan-writers.html"), ("Vaughan", "vaughan-business-plan-writers.html"), ("Markham", "markham-business-plan-writers.html"), ("Richmond Hill", "richmond-hill-business-plan-writers.html"), ("Oakville", "oakville-business-plan-writers.html"), ("Oshawa", "oshawa-business-plan-writers.html"), ("Burlington", "burlington-business-plan-writers.html"), ("Pickering", "pickering-business-plan-writers.html"), ("Ajax", "ajax-business-plan-writers.html"), ("Whitby", "whitby-business-plan-writers.html"), ("Winnipeg", "winnipeg-business-plan-writers.html"), ("Quebec City", "quebec-city-business-plan-writers.html"), ("Hamilton", "hamilton-business-plan-writers.html"), ("Kitchener-Waterloo", "kitchener-waterloo-business-plan-writers.html"), ("Halifax", "halifax-business-plan-writers.html"), ("Victoria", "victoria-business-plan-writers.html"), ("Saskatoon", "saskatoon-business-plan-writers.html"), ("Regina", "regina-business-plan-writers.html"), ("St. John's", "st-johns-business-plan-writers.html"), ("New York City", "new-york-city-business-plan-writers.html"), ("Los Angeles", "los-angeles-business-plan-writers.html"), ("Chicago", "chicago-business-plan-writers.html"), ("Houston", "houston-business-plan-writers.html"), ("Phoenix", "phoenix-business-plan-writers.html"), ("Philadelphia", "philadelphia-business-plan-writers.html"), ("San Antonio", "san-antonio-business-plan-writers.html"), ("San Diego", "san-diego-business-plan-writers.html"), ("Dallas", "dallas-business-plan-writers.html"), ("San Jose", "san-jose-business-plan-writers.html")], 4),
    ("Company", [("About", "/about.html"), ("About &amp; Credentials", "about-business-plan.html"), ("Case Studies", "case-studies.html"), ("Testimonials", "testimonials.html"), ("Pricing", "pricing.html"), ("Contact", "contact.html"), ("Book a Consult", "https://calendly.com/atul_jagga/business-plan-free-consult")]),
    ("Legal", [("Editorial Policy", "editorial-policy.html"), ("Privacy Policy", "privacy-policy.html"), ("Refund Policy", "refund-policy.html"), ("Terms and Conditions", "terms.html")]),
]

FOOTER = f'''<footer id="footer" class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <section class="site-footer__brand" aria-labelledby="footer-brand-heading">
        <img src="img/bizplanlogo.png" alt="The Biz Plans" width="96" height="96" loading="lazy" decoding="async">
        <h2 id="footer-brand-heading">The Biz Plans</h2>
        <ul class="site-footer__contact">
          <li>Toronto, Ontario, Canada</li>
          <li><a href="https://wa.me/16478968362">Chat with us on WhatsApp</a></li>
        </ul>
        <div class="site-footer__social" aria-label="Social media">
          <a href="https://www.linkedin.com/company/the-biz-plans/" target="_blank" rel="noopener noreferrer" aria-label="The Biz Plans on LinkedIn"><i class="fab fa-linkedin-in" aria-hidden="true"></i></a>
          <a href="https://www.facebook.com/people/The-biz-plans/61550125095965/" target="_blank" rel="noopener noreferrer" aria-label="The Biz Plans on Facebook"><i class="fab fa-facebook-f" aria-hidden="true"></i></a>
          <a href="https://www.instagram.com/thebizplans/" target="_blank" rel="noopener noreferrer" aria-label="The Biz Plans on Instagram"><i class="fab fa-instagram" aria-hidden="true"></i></a>
        </div>
      </section>
{chr(10).join(group(*group_data) for group_data in GROUPS)}
    </div>
    <div class="site-footer__bottom">
      <p>© The Biz Plans</p>
    </div>
  </div>
  <script src="js/footer-navigation.min.js" defer></script>
</footer>'''

FOOTER_PATTERN = re.compile(r'<footer\b[^>]*>.*?</footer>', re.DOTALL)


def footer_drift() -> list[str]:
    """Return pages that do not contain exactly the canonical footer once."""
    drift = []
    for page in ROOT.glob("*.html"):
        matches = FOOTER_PATTERN.findall(page.read_text(encoding="utf-8"))
        if matches != [FOOTER]:
            drift.append(page.name)
    return drift


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify every HTML page uses the canonical footer without changing files",
    )
    parser.add_argument('--contact-only', action='store_true',
                        help='add only WhatsApp to existing footers, preserving page-specific details')
    args = parser.parse_args()
    if args.contact_only:
        count = 0
        item = '<li><a href="https://wa.me/16478968362">Chat with us on WhatsApp</a></li>'
        for page in ROOT.glob("*.html"):
            source = page.read_bytes().decode("utf-8")
            match = FOOTER_PATTERN.search(source)
            if not match:
                continue  # Redirect pages do not have a shared footer.
            footer = match.group()
            if args.check:
                assert footer.count(item) == 1, f"WhatsApp footer drift: {page.name}"
            elif item not in footer:
                footer, added = re.subn(r'(<ul class="site-footer__contact">.*?)(\s*</ul>)',
                                       lambda m: m[1] + '\n          ' + item + m[2], footer, count=1, flags=re.S)
                assert added == 1, f"Missing contact list: {page.name}"
                page.write_bytes((source[:match.start()] + footer + source[match.end():]).encode("utf-8"))
            count += 1
        print(f"WhatsApp contact link verified in {count} existing footers")
        return


    if args.check:
        drift = footer_drift()
        if drift:
            raise RuntimeError(f"Non-canonical footer in: {', '.join(drift)}")
        print(f"Canonical footer verified in {len(list(ROOT.glob('*.html')))} pages")
        return

    updated = 0
    installed = 0
    for page in ROOT.glob("*.html"):
        source = page.read_bytes().decode("utf-8")
        result, count = FOOTER_PATTERN.subn(FOOTER, source, count=1)
        if not count and "</body>" in source:
            result = source.replace("</body>", f"{FOOTER}\n</body>", 1)
            count = 1
            installed += 1
        if count and result != source:
            page.write_bytes(result.encode("utf-8"))
            updated += 1

    drift = footer_drift()
    if drift:
        raise RuntimeError(f"Non-canonical footer in: {', '.join(drift)}")
    print(f"Updated footer in {updated} pages ({installed} newly installed)")


if __name__ == "__main__":
    main()
