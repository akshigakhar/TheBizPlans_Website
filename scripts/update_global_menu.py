#!/usr/bin/env python3
"""Keep the primary navigation identical across the static site."""

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

MENU = """<div class="container-fluid sticky-top global-header">
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-dark p-0" aria-label="Primary navigation">
      <a href="/" class="navbar-brand d-flex align-items-center">
        <img src="img/bizplanlogo.png" alt="The Biz Plans logo" width="90" height="90" class="me-2" loading="lazy">
      </a>
      <button class="navbar-toggler ms-auto me-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav list-unstyled ms-auto align-items-lg-center">
          <li class="nav-item dropdown">
            <a href="services.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Services</a>
            <ul class="dropdown-menu bg-light mt-2">
              <li><a href="services.html" class="dropdown-item">Business Plan Writing Services</a></li>
              <li><a href="bank-loan-business-plans.html" class="dropdown-item">Bank Loan Business Plans</a></li>
              <li><a href="investor-business-plan.html" class="dropdown-item">Investor Business Plans</a></li>
              <li><a href="strategic-business-plan.html" class="dropdown-item">Strategic Business Plans</a></li>
              <li><a href="financial-modeling.html" class="dropdown-item">Financial Modelling</a></li>
              <li><a href="business-plan-review.html" class="dropdown-item">Business Plan Review</a></li>
              <li><a href="services.html" class="dropdown-item fw-bold">View All Services</a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a href="small-business-financing-canada.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Financing</a>
            <ul class="dropdown-menu bg-light mt-2">
              <li><a href="small-business-financing-canada.html" class="dropdown-item">Financing Resource Centre</a></li>
              <li><a href="bank-loan-business-plans.html" class="dropdown-item">Bank Loan Business Plans</a></li>
              <li><a href="canada-small-business-financing-program.html" class="dropdown-item">Government Financing</a></li>
              <li><a href="canadian-bank-loan-business-plan-guide.html" class="dropdown-item">Bank Financing Guides</a></li>
              <li><a href="small-business-financing-canada.html" class="dropdown-item fw-bold">View All Financing</a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a href="industry-business-plans.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Industries</a>
            <ul class="dropdown-menu bg-light mt-2">
              <li><a href="industry-business-plans.html" class="dropdown-item">Industry Business Plans</a></li>
              <li><a href="construction-business-plans.html" class="dropdown-item">Construction</a></li>
              <li><a href="daycare-business-plans.html" class="dropdown-item">Daycare</a></li>
              <li><a href="food-franchise-business-plans.html" class="dropdown-item">Food Franchise</a></li>
              <li><a href="medical-services-business-plans.html" class="dropdown-item">Medical Services</a></li>
              <li><a href="trucking-business-plans.html" class="dropdown-item">Trucking</a></li>
              <li><a href="industry-business-plans.html" class="dropdown-item fw-bold">View All Industries</a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a href="business-plan-template.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Free Tools</a>
            <ul class="dropdown-menu bg-light mt-2"><li><a href="business-plan-template.html" class="dropdown-item">Free Business Plan Templates</a></li><li><a href="business-plan-generator.html" class="dropdown-item">Free Business Plan Generator</a></li></ul>
          </li>
          <li class="nav-item dropdown">
            <a href="blog-learning-hub.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Learn</a>
            <ul class="dropdown-menu bg-light mt-2 dropdown-menu-end">
              <li><a href="blog-learning-hub.html" class="dropdown-item">Learning Centre</a></li><li><a href="business-plan-essentials.html" class="dropdown-item">Business Plan Essentials</a></li><li><a href="chapter-3-market-research.html" class="dropdown-item">Market Research</a></li><li><a href="chapter-7-financial-forecasting.html" class="dropdown-item">Financial Projections</a></li><li><a href="business-plan-glossary.html" class="dropdown-item">Business Plan Glossary</a></li><li><a href="faqs.html" class="dropdown-item">FAQs</a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a href="about-business-plan.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">About</a>
            <ul class="dropdown-menu bg-light mt-2 dropdown-menu-end"><li><a href="about-business-plan.html" class="dropdown-item">About &amp; Credentials</a></li><li><a href="case-studies.html" class="dropdown-item">Case Studies</a></li><li><a href="testimonials.html" class="dropdown-item">Testimonials</a></li><li><a href="pricing.html" class="dropdown-item">Pricing</a></li><li><a href="contact.html" class="dropdown-item">Contact</a></li></ul>
          </li>
          <li class="nav-item"><a href="contact.html" class="btn btn-light rounded-pill ms-lg-2 nav-cta">Book a Consult</a></li>
        </ul>
      </div>
    </nav>
  </div>
</div>"""

NAV_PATTERN = re.compile(
    r'<div class="container-fluid sticky-top(?: global-header)?">\s*<div class="container">\s*'
    r'<nav class="navbar navbar-expand-lg navbar-dark p-0"(?: aria-label="Primary navigation")?>.*?</nav>\s*</div>\s*</div>',
    re.DOTALL,
)
CLUSTER_NAV_PATTERN = re.compile(
    r'<header class="cluster-header"><div class="container-fluid sticky-top">.*?</header>',
    re.DOTALL,
)


def menu_drift() -> list[str]:
    """Return pages that do not contain exactly the canonical menu once."""
    drift = []
    for page in ROOT.glob("*.html"):
        source = page.read_text(encoding="utf-8")
        if re.search(r'<meta[^>]+name=["\']robots["\'][^>]+noindex', source, re.I):
            continue
        matches = NAV_PATTERN.findall(source)
        if matches != [MENU]:
            drift.append(page.name)
    return drift


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify every HTML page uses the canonical menu without changing files",
    )
    args = parser.parse_args()

    if args.check:
        drift = menu_drift()
        if drift:
            raise RuntimeError(f"Non-canonical menu in: {', '.join(drift)}")
        print(f"Canonical menu verified in {len(list(ROOT.glob('*.html'))) - 1} public pages")
        return

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

    drift = menu_drift()
    if drift:
        raise RuntimeError(f"Non-canonical menu in: {', '.join(drift)}")
    print(f"Updated navigation in {updated} pages")


if __name__ == "__main__":
    main()
