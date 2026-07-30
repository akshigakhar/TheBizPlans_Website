#!/usr/bin/env python3
"""Install the shared, comprehensive site footer on every static page."""

from pathlib import Path
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
    ("Company", [("About &amp; Credentials", "about-business-plan.html"), ("Case Studies", "case-studies.html"), ("Testimonials", "testimonials.html"), ("Pricing", "pricing.html"), ("Toronto Business Plan Writers", "toronto-business-plan-writers.html"), ("Vancouver Business Plan Writers", "vancouver-business-plan-writers.html"), ("Contact", "contact.html"), ("Book a Consult", "contact.html")]),
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


def main() -> None:
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

    missing = [page.name for page in ROOT.glob("*.html") if not FOOTER_PATTERN.search(page.read_text(encoding="utf-8"))]
    if missing:
        raise RuntimeError(f"Footer is missing from: {', '.join(missing)}")
    print(f"Updated footer in {updated} pages ({installed} newly installed)")


if __name__ == "__main__":
    main()
