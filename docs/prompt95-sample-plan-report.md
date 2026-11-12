# Prompt 95 — Sample library expansion, batch 2

The library starts with **36 unique entries** and ends with **41**.

## Coverage and substitution

Accounting firm, security guard company, private school / after-school program and bookstore are uncovered. Esthetician is already covered by `/blog-sample-esthetician-business-plan.html`, so it is skipped. The reserve list is applied in order: bakery, gym, trucking, landscaping and pet grooming / boarding already have samples. **Car wash** is the first uncovered reserve and replaces esthetician. No existing sample is duplicated or counted as new.

## Created samples

| Page URL | Matching PDF path | Fictional business | Library placement / position |
| --- | --- | --- | --- |
| https://thebizplans.com/blog-sample-accounting-firm-business-plan.html | `/downloads/accounting-firm-business-plan-sample.pdf` | Alder Ledger Advisory Inc.; Hamilton, Ontario | Professional & Care / 37 |
| https://thebizplans.com/blog-sample-security-guard-company-business-plan.html | `/downloads/security-guard-company-business-plan-sample.pdf` | North Lantern Security Services Inc.; London, Ontario | Trades & Services / 38 |
| https://thebizplans.com/blog-sample-private-school-business-plan.html | `/downloads/private-school-business-plan-sample.pdf` | Cedar Kite Learning Academy Inc.; Kitchener, Ontario | Professional & Care / 39 |
| https://thebizplans.com/blog-sample-bookstore-business-plan.html | `/downloads/bookstore-business-plan-sample.pdf` | Maple Quill Books Inc.; Guelph, Ontario | Retail / 40 |
| https://thebizplans.com/blog-sample-car-wash-business-plan.html | `/downloads/car-wash-business-plan-sample.pdf` | Silver Brook Washworks Inc.; Barrie, Ontario | Trades & Services / 41 |

The sample index keeps its existing sector/card format and unique ItemList positions. All five canonical page URLs are included in `sitemap.xml`, preserving unrelated entries.

## Internal links

Existing contextual inbound links added:

- `/financial-modeling.html` → accounting firm, after the financial-model explanation.
- `/blog-sample-cleaning-company-business-plan.html` → security guard company, comparing contract staffing and payroll timing before the financial section.
- `/daycare-business-plans.html` → private school / after-school program, distinguishing education and child-care classification.
- `/blog-sample-clothing-line-business-plan.html` → bookstore, comparing inventory and supplier terms in the startup-budget discussion.
- `/blog-sample-auto-repair-shop-business-plan.html` → car wash, comparing a separate vehicle-service model before the financial section.

Each new sample links to `/sample-business-plans.html`, `/services.html`, `/business-plan-generator.html` and `/contact.html`. The appendix also links to `/financial-modeling.html` for accounting, `/business-plan-writing-services.html` for security, `/daycare-business-plans.html` for school / after-school, and `/industry-business-plans.html` for bookstore and car wash.

## Format and content

Studied the home-care services, pet grooming / boarding and real estate brokerage pages and their PDFs, plus the sample index and Prompt 94 report. The home-care page supplies the unchanged page shell, print CSS, annotations, section order, table classes, author card, shared navigation/footer and generator CTA. Each new sample has approximately 4,300 words, ten numbered plan sections, five FAQs, opening sources and uses, revenue drivers, three-year income/cash-flow/balance-sheet tables, break-even, debt-service and combined downside analysis, funding request and appendix.

All sample companies, founders, biographies, commercial figures and demand assumptions are explicitly fictional and illustrative. Official links are research starting points; no verification date, fee, approval timeline, statutory rate, licence or eligibility finding is invented. The school model separates elementary tuition and optional after-school enrichment; it assumes no diploma authority or automatic child-care exemption. Accounting excludes assurance work; security excludes armed services; car wash assumes leased serviced premises, not land or tunnel construction. Existing site author components are reused without new business claims.

PDFs use headless Chromium and each page's existing print styles, A4, background printing and 12 mm margins. Each PDF reproduces the full sample in **11 pages**, matching the recent library PDFs.

## Validation

- Independently parsed displayed HTML tables with decimal arithmetic: all **15 modeled years** reconcile unit/price revenue, income calculations, working-capital movements, cash roll-forwards, debt, net assets, retained earnings and assets = liabilities + equity.
- Chromium checks on every sample at 1440 px and 390 px: one H1, ten numbered sections plus FAQs, five financial tables, working section anchors, no document overflow and matching visible FAQ/schema text. Reviewed desktop/mobile screenshots and a rendered PDF financial page.
- Checked live JSON-LD after shared schema execution: no rating or review data. New page titles, descriptions and canonical URLs are unique.
- Library has 41 cards with 41 unique positions; all new cards, downloads and sitemap entries resolve locally. Extracted all PDFs to confirm company identity, numbered sections, financial statements and FAQs.
- `node scripts/build-vercel-site.mjs work/site-dist` passes; all five pages and PDFs are staged byte-for-byte. This is a static staging check, not a deployment; generator source and logic are unchanged.
- `git diff --check` passes.
- `python scripts/audit_site.py` and `python scripts/generate_seo.py --check` fail on the unchanged starting commit as well. Existing findings include redirect/canonical disagreements, sitemap drift, retired external links and shared header/footer variants. The new pages inherit the template's eager header-logo warning; there are no additional non-template findings. Unrelated legacy SEO data is preserved for this scoped batch.

No design/layout components, `/listings.html`, quote forms, generator source or generator bundles are changed. Existing sample pages receive contextual text links only.
