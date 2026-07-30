#!/usr/bin/env python3
"""Keep the primary navigation identical across the static site."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

MENU = """<div class="container-fluid sticky-top">
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-dark p-0" aria-label="Primary navigation">
      <a href="/" class="navbar-brand d-flex align-items-center">
        <img src="img/bizplanlogo.png" alt="The Biz Plans logo" width="90" height="90" class="me-2" loading="lazy">
      </a>
      <button class="navbar-toggler ms-auto me-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav list-unstyled ms-auto align-items-lg-center d-none d-lg-flex">
          <li class="nav-item"><a href="/" class="nav-link">Home</a></li>
          <li class="nav-item dropdown">
            <a href="services.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Services</a>
            <ul class="dropdown-menu bg-light mt-2">
              <li><a href="services.html" class="dropdown-item">All Services</a></li>
              <li><a href="bank-loan-business-plans.html" class="dropdown-item">Bank Loan Business Plans</a></li>
              <li><a href="investor-business-plan.html" class="dropdown-item">Investor Business Plans</a></li>
              <li><a href="immigration-business-plans.html" class="dropdown-item">Immigration Business Plans</a></li>
              <li><a href="strategic-business-plan.html" class="dropdown-item">Strategic Business Plans</a></li>
              <li><a href="financial-modeling.html" class="dropdown-item">Financial Modelling</a></li>
              <li><a href="marketing-growth-strategy.html" class="dropdown-item">Marketing &amp; Growth Strategy</a></li>
              <li><a href="business-plan-review.html" class="dropdown-item">Business Plan Review</a></li>
              <li><a href="indigenous-business-plan.html" class="dropdown-item">Indigenous Business Plans</a></li>
              <li><a href="innovation-business-plan.html" class="dropdown-item">Innovation Business Plans</a></li>
              <li><a href="financial-due-diligence-essentials.html" class="dropdown-item">Financial Due Diligence</a></li>
            </ul>
          </li>
          <li class="nav-item dropdown mega-menu-parent">
            <a href="bank-loan-business-plans.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Financing</a>
            <div class="dropdown-menu mega-menu bg-light mt-2" role="menu">
              <a href="bank-loan-business-plans.html" class="dropdown-item fw-bold mb-2">Financing Resource Centre</a>
              <div class="mega-menu-grid">
                <div class="mega-menu-section"><span class="mega-menu-heading">Government Financing</span>
                  <a href="canada-small-business-financing-program.html" class="dropdown-item">Canada Small Business Financing Program (CSBFP)</a><a href="business-development-bank-of-canada.html" class="dropdown-item">Business Development Bank of Canada (BDC)</a><a href="farm-credit-canada.html" class="dropdown-item">Farm Credit Canada (FCC)</a><a href="canadian-agricultural-loans-act.html" class="dropdown-item">Canadian Agricultural Loans Act (CALA)</a><a href="futurpreneur.html" class="dropdown-item">Futurpreneur</a><a href="export-development-canada.html" class="dropdown-item">Export Development Canada (EDC)</a>
                </div>
                <div class="mega-menu-section"><span class="mega-menu-heading">Banks &amp; Credit Unions</span>
                  <a href="royal-bank-of-canada.html" class="dropdown-item">Royal Bank of Canada (RBC)</a><a href="td-canada-trust.html" class="dropdown-item">TD Canada Trust</a><a href="scotiabank.html" class="dropdown-item">Scotiabank</a><a href="cibc.html" class="dropdown-item">CIBC</a><a href="national-bank-of-canada.html" class="dropdown-item">National Bank of Canada</a><a href="desjardins.html" class="dropdown-item">Desjardins</a><a href="vancity-business-plan.html" class="dropdown-item">Vancity</a>
                </div>
                <div class="mega-menu-section"><span class="mega-menu-heading">Specialized Financing</span>
                  <a href="black-entrepreneurship.html" class="dropdown-item">Black Entrepreneurship Program</a><a href="indigenous-aboriginal-entrepreneurship.html" class="dropdown-item">Indigenous &amp; Aboriginal Entrepreneurship Financing</a><a href="women-entrepreneurship-loan-fund.html" class="dropdown-item">Women Entrepreneurship Loan Fund</a>
                  <span class="mega-menu-heading mt-2">Alternative Financing</span><a href="private-lender-alternative-financing.html" class="dropdown-item">Private Lenders &amp; Alternative Financing</a>
                  <span class="mega-menu-heading mt-2">Bank-Readiness Guides</span><a href="canadian-bank-loan-business-plan-guide.html" class="dropdown-item">Canadian Bank Loan Business Plan Guide</a><a href="how-banks-evaluate-business-plans.html" class="dropdown-item">How Banks Evaluate Business Plans</a>
                </div>
              </div>
            </div>
          </li>
          <li class="nav-item dropdown mega-menu-parent">
            <a href="immigration-business-plans.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Immigration</a>
            <div class="dropdown-menu mega-menu mega-menu--compact bg-light mt-2" role="menu">
              <a href="immigration-business-plans.html" class="dropdown-item fw-bold mb-2">All Immigration Business Plans</a>
              <div class="mega-menu-grid">
                <div class="mega-menu-section"><span class="mega-menu-heading">Federal Programs</span><a href="startup-visa-business-plan.html" class="dropdown-item">Start-Up Visa Program</a><a href="ict-business-plan.html" class="dropdown-item">Intra-Company Transfer</a><a href="lmia-owner-operator-business-plan.html" class="dropdown-item">LMIA Owner-Operator</a><a href="self-employed-business-plan.html" class="dropdown-item">Self-Employed Visa</a></div>
                <div class="mega-menu-section"><span class="mega-menu-heading">Provincial Programs</span><a href="aaip-entrepreneur-business-plan.html" class="dropdown-item">Alberta Advantage Immigration Program (AAIP)</a><a href="bcpnp-business-plan.html" class="dropdown-item">British Columbia Provincial Nominee Program (BC PNP)</a><a href="mpnp-business-plan.html" class="dropdown-item">Manitoba Provincial Nominee Program (MPNP)</a><a href="nbpnp-business-plan.html" class="dropdown-item">New Brunswick Provincial Nominee Program (NBPNP)</a><a href="nsnp-business-plan.html" class="dropdown-item">Nova Scotia Nominee Program (NSNP)</a><a href="oinp-business-plan.html" class="dropdown-item">Ontario Immigrant Nominee Program (OINP)</a><a href="sinp-business-plan.html" class="dropdown-item">Saskatchewan Immigrant Nominee Program (SINP)</a></div>
              </div>
            </div>
          </li>
          <li class="nav-item dropdown mega-menu-parent">
            <a href="industry-business-plans.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Industries</a>
            <div class="dropdown-menu mega-menu mega-menu--compact bg-light mt-2 mega-menu-end" role="menu">
              <a href="industry-business-plans.html" class="dropdown-item fw-bold mb-2">All Industries</a>
              <div class="mega-menu-grid">
                <div class="mega-menu-section"><a href="beauty-salon-business-plans.html" class="dropdown-item">Beauty Salon</a><a href="brewery-business-plans.html" class="dropdown-item">Brewery</a><a href="cannabis-business-plans.html" class="dropdown-item">Cannabis</a><a href="construction-business-plans.html" class="dropdown-item">Construction</a><a href="daycare-business-plans.html" class="dropdown-item">Daycare</a><a href="fintech-business-plans.html" class="dropdown-item">Fintech</a><a href="food-franchise-business-plans.html" class="dropdown-item">Food Franchise</a></div>
                <div class="mega-menu-section"><a href="grocery-business-plans.html" class="dropdown-item">Grocery</a><a href="hvac-business-plans.html" class="dropdown-item">HVAC</a><a href="logistics-business-plans.html" class="dropdown-item">Logistics</a><a href="manufacturing-business-plans.html" class="dropdown-item">Manufacturing</a><a href="marine-business-plans.html" class="dropdown-item">Marine</a><a href="medical-services-business-plans.html" class="dropdown-item">Medical Services</a><a href="mobile-app-business-plans.html" class="dropdown-item">Mobile Apps</a></div>
                <div class="mega-menu-section"><a href="nail-salon-business-plans.html" class="dropdown-item">Nail Salon</a><a href="pharmacy-business-plans.html" class="dropdown-item">Pharmacy</a><a href="plumbing-business-plans.html" class="dropdown-item">Plumbing</a><a href="recruiting-business-plans.html" class="dropdown-item">Recruiting</a><a href="telecom-business-plans.html" class="dropdown-item">Telecom</a><a href="trucking-business-plans.html" class="dropdown-item">Trucking</a></div>
              </div>
            </div>
          </li>
          <li class="nav-item dropdown">
            <a href="blog-learning-hub.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Learn</a>
            <ul class="dropdown-menu bg-light mt-2 dropdown-menu-end">
              <li><a href="blog-learning-hub.html" class="dropdown-item">Learning Centre</a></li><li><a href="books.html" class="dropdown-item">Books &amp; Chapters</a></li><li><a href="blog-learning-hub.html" class="dropdown-item">Blog</a></li><li><a href="business-plan-essentials.html" class="dropdown-item">Business Plan Essentials</a></li><li><a href="business-plan-cost-timeline-checklist.html" class="dropdown-item">Business Plan Cost, Timeline &amp; Checklist</a></li><li><a href="chapter-3-market-research.html" class="dropdown-item">Market Research</a></li><li><a href="business-plan-glossary.html" class="dropdown-item">Business Plan Glossary</a></li><li><a href="business-plan-comparisons.html" class="dropdown-item">Templates &amp; Comparisons</a></li><li><a href="sample-other-plan.html" class="dropdown-item">Sample Business Plan Template</a></li><li><a href="authoritative-resources.html" class="dropdown-item">Authoritative Resources</a></li><li><a href="faqs.html" class="dropdown-item">FAQs</a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a href="case-studies.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Results</a>
            <ul class="dropdown-menu bg-light mt-2 dropdown-menu-end"><li><a href="case-studies.html" class="dropdown-item">Case Studies</a></li><li><a href="testimonials.html" class="dropdown-item">Testimonials</a></li><li><a href="about-business-plan.html" class="dropdown-item">About &amp; Credentials</a></li></ul>
          </li>
          <li class="nav-item"><a href="pricing.html" class="nav-link">Pricing</a></li>
          <li class="nav-item"><a href="contact.html" class="btn btn-light rounded-pill ms-lg-2 nav-cta">Book a Consult</a></li>
        </ul>
        <ul class="navbar-nav list-unstyled d-lg-none mobile-nav" aria-label="Mobile navigation">
          <li class="nav-item"><a href="/" class="nav-link">Home</a></li>
          <li class="nav-item"><a href="services.html" class="nav-link">Services</a></li>
          <li class="nav-item"><a href="bank-loan-business-plans.html" class="nav-link">Financing</a></li>
          <li class="nav-item"><a href="immigration-business-plans.html" class="nav-link">Immigration</a></li>
          <li class="nav-item"><a href="industry-business-plans.html" class="nav-link">Industries</a></li>
          <li class="nav-item"><a href="blog-learning-hub.html" class="nav-link">Learn</a></li>
          <li class="nav-item"><a href="case-studies.html" class="nav-link">Results</a></li>
          <li class="nav-item"><a href="pricing.html" class="nav-link">Pricing</a></li>
          <li class="nav-item"><a href="contact.html" class="btn btn-light rounded-pill nav-cta my-3">Book a Consult</a></li>
        </ul>
      </div>
    </nav>
  </div>
</div>"""

NAV_PATTERN = re.compile(
    r'<div class="container-fluid sticky-top">\s*<div class="container">\s*'
    r'<nav class="navbar navbar-expand-lg navbar-dark p-0"(?: aria-label="Primary navigation")?>.*?</nav>\s*</div>\s*</div>',
    re.DOTALL,
)
CLUSTER_NAV_PATTERN = re.compile(
    r'<header class="cluster-header"><div class="container-fluid sticky-top">.*?</header>',
    re.DOTALL,
)


def main() -> None:
    updated = 0
    for page in ROOT.glob("*.html"):
        source = page.read_bytes().decode("utf-8")
        result, count = NAV_PATTERN.subn(MENU, source, count=1)
        if not count:
            result, count = CLUSTER_NAV_PATTERN.subn(MENU, source, count=1)
        if count and "bootstrap.bundle.min.js" not in result:
            result = result.replace(
                "</body>",
                '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/js/bootstrap.bundle.min.js" defer></script></body>',
                1,
            )
        if count and result != source:
            page.write_bytes(result.encode("utf-8"))
            updated += 1
    print(f"Updated navigation in {updated} pages")


if __name__ == "__main__":
    main()
