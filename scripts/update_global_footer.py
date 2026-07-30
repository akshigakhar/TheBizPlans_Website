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
    ("Services", [("All Services", "services.html"), ("Bank Loan Business Plans", "bank-loan-business-plans.html"), ("Investor Business Plans", "investor-business-plan.html"), ("Immigration Business Plans", "immigration-business-plans.html"), ("Strategic Business Plans", "strategic-business-plan.html"), ("Financial Modelling", "financial-modeling.html"), ("Marketing &amp; Growth Strategy", "marketing-growth-strategy.html"), ("Business Plan Review", "business-plan-review.html"), ("Indigenous Business Plans", "indigenous-business-plan.html"), ("Innovation Business Plans", "innovation-business-plan.html"), ("Financial Due Diligence", "financial-due-diligence-essentials.html")]),
    ("Financing", [("Financing Resource Centre", "bank-loan-business-plans.html"), ("Government Financing Programs", "canada-small-business-financing-program.html"), ("Banks &amp; Credit Unions", "royal-bank-of-canada.html"), ("Specialized Financing Programs", "black-entrepreneurship.html"), ("Alternative Financing", "private-lender-alternative-financing.html"), ("Bank-Readiness Guides", "canadian-bank-loan-business-plan-guide.html"), ("How Banks Evaluate Business Plans", "how-banks-evaluate-business-plans.html")]),
    ("Immigration", [("All Immigration Business Plans", "immigration-business-plans.html"), ("Federal Immigration Programs", "startup-visa-business-plan.html"), ("Provincial Immigration Programs", "oinp-business-plan.html"), ("Start-Up Visa Program", "startup-visa-business-plan.html"), ("Intra-Company Transfer", "ict-business-plan.html"), ("LMIA Owner-Operator", "lmia-owner-operator-business-plan.html"), ("Self-Employed Visa", "self-employed-business-plan.html")]),
    ("Industries", [("All Industries", "industry-business-plans.html"), ("Featured Industries", "industry-business-plans.html"), ("Industry A–Z", "industry-business-plans.html")]),
    ("Industry Resources", [("Business Plans", "industry-business-plans.html"), ("Business Loans", "bank-loan-business-plans.html"), ("Investor Plans", "investor-business-plan.html"), ("Franchise Plans", "food-franchise-business-plans.html"), ("Financial Projections", "financial-modeling.html"), ("Startup Cost Calculators", "nail-salon-cost-calculator.html"), ("Pitch Decks", "nail-salon-pitch-decks.html")]),
    ("Learn", [("Learning Centre", "blog-learning-hub.html"), ("Books &amp; Chapters", "books.html"), ("Blog", "blog-learning-hub.html"), ("Business Plan Essentials", "business-plan-essentials.html"), ("Business Plan Cost, Timeline &amp; Checklist", "business-plan-cost-timeline-checklist.html"), ("Business Plan Glossary", "business-plan-glossary.html"), ("Templates &amp; Comparisons", "business-plan-comparisons.html"), ("Sample Business Plan Template", "sample-other-plan.html"), ("Authoritative Resources", "authoritative-resources.html"), ("FAQs", "faqs.html")]),
    ("Company", [("About &amp; Credentials", "about-business-plan.html"), ("Case Studies", "case-studies.html"), ("Testimonials", "testimonials.html"), ("Pricing", "pricing.html"), ("Toronto Business Plan Writers", "toronto-business-plan-writers.html"), ("Vancouver Business Plan Writers", "vancouver-business-plan-writers.html"), ("Contact", "contact.html"), ("Book a Consult", "contact.html")]),
    ("Legal", [("Editorial Policy", "editorial-policy.html"), ("Privacy Policy", "privacy-policy.html"), ("Refund Policy", "refund-policy.html"), ("Terms and Conditions", "terms.html")]),
]

FOOTER = f'''<footer id="footer" class="site-footer">
  <div class="container">
    <div class="site-footer__grid">
      <section class="site-footer__brand" aria-labelledby="footer-brand-heading">
        <img src="img/bizplanlogo.png" alt="The Biz Plans" width="96" height="96" loading="lazy" decoding="async">
        <h2 id="footer-brand-heading">The Biz Plans</h2>
        <p>CPA-led business plans, financial models and growth strategies built for lenders, investors and immigration pathways.</p>
        <ul class="site-footer__contact">
          <li><a href="tel:+16478968362">+1 647-896-8362</a></li>
          <li><a href="mailto:info@thebizplans.com">info@thebizplans.com</a></li>
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
      <nav aria-label="Footer legal links">
        <a href="privacy-policy.html">Privacy</a>
        <a href="terms.html">Terms</a>
      </nav>
      <a href="contact.html" class="btn btn-light rounded-pill">Book a Consult</a>
    </div>
  </div>
</footer>'''

FOOTER_PATTERN = re.compile(r'<footer\b[^>]*>.*?</footer>', re.DOTALL)


def main() -> None:
    updated = 0
    for page in ROOT.glob("*.html"):
        source = page.read_bytes().decode("utf-8")
        result, count = FOOTER_PATTERN.subn(FOOTER, source, count=1)
        if count and result != source:
            page.write_bytes(result.encode("utf-8"))
            updated += 1
    print(f"Updated footer in {updated} pages")


if __name__ == "__main__":
    main()
