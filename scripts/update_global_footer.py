#!/usr/bin/env python3
"""Install the shared, comprehensive site footer on every static page."""

from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]


def links(items: list[tuple[str, str]]) -> str:
    return "\n".join(f'              <li><a href="{href}">{label}</a></li>' for label, href in items)


def group(title: str, items: list[tuple[str, str]]) -> str:
    return f'''        <nav class="site-footer__group" aria-label="{title}">
          <h2>{title}</h2>
          <ul>
{links(items)}
          </ul>
        </nav>'''


GROUPS = [
    ("Canada", [("Toronto", "toronto-business-plan-writers.html"), ("Montreal", "montreal-business-plan-writers.html"), ("Vancouver", "vancouver-business-plan-writers.html"), ("Calgary", "calgary-business-plan-writers.html"), ("Edmonton", "edmonton-business-plan-writers.html"), ("Ottawa", "ottawa-business-plan-writers.html"), ("Winnipeg", "winnipeg-business-plan-writers.html"), ("Quebec City", "quebec-city-business-plan-writers.html"), ("Hamilton", "hamilton-business-plan-writers.html"), ("Kitchener-Waterloo", "kitchener-waterloo-business-plan-writers.html"), ("Halifax", "halifax-business-plan-writers.html"), ("Victoria", "victoria-business-plan-writers.html"), ("Saskatoon", "saskatoon-business-plan-writers.html"), ("Regina", "regina-business-plan-writers.html"), ("St. John's", "st-johns-business-plan-writers.html")]),
    ("United States", [("New York City", "new-york-city-business-plan-writers.html"), ("Los Angeles", "los-angeles-business-plan-writers.html"), ("Chicago", "chicago-business-plan-writers.html"), ("Houston", "houston-business-plan-writers.html"), ("Phoenix", "phoenix-business-plan-writers.html"), ("Philadelphia", "philadelphia-business-plan-writers.html"), ("San Antonio", "san-antonio-business-plan-writers.html"), ("San Diego", "san-diego-business-plan-writers.html"), ("Dallas", "dallas-business-plan-writers.html"), ("San Jose", "san-jose-business-plan-writers.html")]),
    ("Company", [("About &amp; Credentials", "about-business-plan.html"), ("Case Studies", "case-studies.html"), ("Testimonials", "testimonials.html"), ("Pricing", "pricing.html"), ("Contact", "contact.html"), ("Book a Consult", "contact.html")]),
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
        </ul>
        <div class="site-footer__social" aria-label="Social media">
          <a href="https://www.linkedin.com/company/thebizplans" target="_blank" rel="noopener noreferrer" aria-label="The Biz Plans on LinkedIn"><i class="fab fa-linkedin-in" aria-hidden="true"></i></a>
          <a href="https://www.facebook.com/people/The-biz-plans/61550125095965/" target="_blank" rel="noopener noreferrer" aria-label="The Biz Plans on Facebook"><i class="fab fa-facebook-f" aria-hidden="true"></i></a>
          <a href="https://www.instagram.com/thebizplans/" target="_blank" rel="noopener noreferrer" aria-label="The Biz Plans on Instagram"><i class="fab fa-instagram" aria-hidden="true"></i></a>
        </div>
      </section>
{chr(10).join(group(title, items) for title, items in GROUPS)}
    </div>
    <div class="site-footer__bottom">
      <p>© The Biz Plans</p>
    </div>
  </div>
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
    args = parser.parse_args()

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
