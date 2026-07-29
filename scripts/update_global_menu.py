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
        <div class="navbar-nav ms-auto align-items-lg-center">
          <a href="/" class="nav-item nav-link">Home</a>

          <div class="nav-item dropdown">
            <a href="services.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Services</a>
            <div class="dropdown-menu bg-light mt-2">
              <a href="services.html" class="dropdown-item">All Services</a>
              <a href="bank-loan-business-plans.html" class="dropdown-item">Bank Loan Plans</a>
              <a href="investor-business-plan.html" class="dropdown-item">Investor Plans</a>
              <a href="immigration-business-plans.html" class="dropdown-item">Immigration Plans</a>
              <a href="financial-modeling.html" class="dropdown-item">Financial Modelling</a>
              <a href="strategic-business-plan.html" class="dropdown-item">Strategic &amp; Growth Planning</a>
              <a href="business-plan-review.html" class="dropdown-item">Business Plan Review</a>
            </div>
          </div>

          <div class="nav-item dropdown">
            <a href="bank-loan-business-plans.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Financing</a>
            <div class="dropdown-menu bg-light mt-2">
              <a href="bank-loan-business-plans.html" class="dropdown-item">Financing Resource Centre</a>
              <a href="canada-small-business-financing-program.html" class="dropdown-item">Government Programs</a>
              <a href="royal-bank-of-canada.html" class="dropdown-item">Banks &amp; Credit Unions</a>
              <a href="black-entrepreneurship.html" class="dropdown-item">Specialized Programs</a>
              <a href="private-lender-alternative-financing.html" class="dropdown-item">Alternative Financing</a>
              <a href="canadian-bank-loan-business-plan-guide.html" class="dropdown-item">Bank-Readiness Guides</a>
            </div>
          </div>

          <div class="nav-item dropdown">
            <a href="immigration-business-plans.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Immigration</a>
            <div class="dropdown-menu bg-light mt-2">
              <a href="immigration-business-plans.html" class="dropdown-item">Immigration Business Plans</a>
              <a href="startup-visa-business-plan.html" class="dropdown-item">Federal Programs</a>
              <a href="bcpnp-business-plan.html" class="dropdown-item">Provincial Programs</a>
              <a href="immigration-business-plans.html" class="dropdown-item">How the Process Works</a>
            </div>
          </div>

          <div class="nav-item dropdown">
            <a href="industry-business-plans.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Industries</a>
            <div class="dropdown-menu bg-light mt-2">
              <a href="industry-business-plans.html" class="dropdown-item">All Industries</a>
              <a href="industry-business-plans.html" class="dropdown-item">Featured Industries</a>
              <a href="industry-business-plans.html" class="dropdown-item">Industry A&ndash;Z</a>
            </div>
          </div>

          <div class="nav-item dropdown">
            <a href="blog-learning-hub.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Learn</a>
            <div class="dropdown-menu bg-light mt-2">
              <a href="blog-learning-hub.html" class="dropdown-item">Learning Centre</a>
              <a href="business-plan-essentials.html" class="dropdown-item">Business Plan Foundations</a>
              <a href="chapter-3-market-research.html" class="dropdown-item">Market Research</a>
              <a href="books.html" class="dropdown-item">Books &amp; Chapters</a>
              <a href="business-plan-glossary.html" class="dropdown-item">Glossary</a>
              <a href="business-plan-comparisons.html" class="dropdown-item">Templates &amp; Comparisons</a>
            </div>
          </div>

          <div class="nav-item dropdown">
            <a href="case-studies.html" class="nav-link dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Results</a>
            <div class="dropdown-menu bg-light mt-2 dropdown-menu-end">
              <a href="case-studies.html" class="dropdown-item">Case Studies</a>
              <a href="testimonials.html" class="dropdown-item">Testimonials</a>
              <a href="about-business-plan.html" class="dropdown-item">About &amp; Credentials</a>
            </div>
          </div>

          <a href="pricing.html" class="nav-item nav-link">Pricing</a>
          <a href="project-brief.html" class="btn btn-light rounded-pill ms-lg-2 nav-cta">Start a Project</a>
        </div>
      </div>
    </nav>
  </div>
</div>"""

NAV_PATTERN = re.compile(
    r'<div class="container-fluid sticky-top">\s*<div class="container">\s*'
    r'<nav class="navbar navbar-expand-lg navbar-dark p-0">.*?</nav>\s*</div>\s*</div>',
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
