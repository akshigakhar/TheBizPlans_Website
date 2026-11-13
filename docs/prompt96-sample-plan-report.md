# Prompt 96 — Semrush gap industries, batch 3

The library grows from **41 to 46 unique samples**.

## Coverage and substitutions

Digital marketing agency is already covered by `/blog-sample-marketing-agency-business-plan.html`, whose fictional agency offers SEO, paid advertising, social media and content marketing. Welding is already covered by `/blog-sample-welding-company-business-plan.html`. Neither is duplicated.

Reserves were checked in order: bakery, gym, trucking, landscaping, pet grooming/boarding and car wash already have samples (car wash was Prompt 95’s substitution). Clothing boutique is uncovered: the existing clothing-line sample covers designing/producing a line, while this new boutique purchases finished apparel for resale. It replaces digital marketing agency. Convenience store is conservatively skipped because the liquor-store sample explicitly includes a convenience-market food and household assortment. Pizza restaurant replaces welding: the existing restaurant is a 45-seat casual-dining Canadian comfort-food concept; this sample is a takeout pizza kitchen. No other reserve is needed.

Carpentry and custom home builder are distinct from the existing commercial tenant-improvement/general-contractor sample. This batch covers nonstructural interior finish carpentry and customer-lot custom homes respectively. Insurance agency is uncovered.

## Samples created

| Page URL | PDF path | Fictional business |
| --- | --- | --- |
| https://thebizplans.com/blog-sample-carpentry-business-plan.html | `/downloads/carpentry-business-plan-sample.pdf` | Elm Notch Woodworks Inc.; Guelph, Ontario |
| https://thebizplans.com/blog-sample-custom-home-builder-business-plan.html | `/downloads/custom-home-builder-business-plan-sample.pdf` | Willow Span Homes Inc.; London, Ontario |
| https://thebizplans.com/blog-sample-insurance-agency-business-plan.html | `/downloads/insurance-agency-business-plan-sample.pdf` | Cedar Arc Insurance Services Inc.; Hamilton, Ontario |
| https://thebizplans.com/blog-sample-clothing-boutique-business-plan.html | `/downloads/clothing-boutique-business-plan-sample.pdf` | Amber Hem Boutique Inc.; Kitchener, Ontario |
| https://thebizplans.com/blog-sample-pizza-restaurant-business-plan.html | `/downloads/pizza-restaurant-business-plan-sample.pdf` | Copper Peel Pizza Kitchen Inc.; Barrie, Ontario |

## Internal links added

Each new sample links to the library, `/services.html`, `/business-plan-generator.html`, `/contact.html` and a relevant planning page:

- `carpentry` → `/construction-business-plans.html`; contextual inbound link from `/blog-sample-construction-company-business-plan.html`.
- `custom-home-builder` → `/construction-business-plans.html`; contextual inbound link from `/construction-business-plans.html`.
- `insurance-agency` → `/business-plan-writing-services.html`; contextual inbound link from `/financial-modeling.html`.
- `clothing-boutique` → `/industry-business-plans.html`; contextual inbound link from `/blog-sample-clothing-line-business-plan.html`.
- `pizza-restaurant` → `/restaurant-business-plan.html`; contextual inbound link from `/blog-sample-restaurant-business-plan.html`.

All five index entries retain the existing sector/card format, with unique ItemList positions 42–46. The five canonical URLs are added to the sitemap without regenerating unrelated entries.

## Format and illustrative content

Studied Prompt 95’s report, the accounting-firm page and PDF, the index, and existing digital-marketing, welding, construction, clothing-line, restaurant and liquor-store coverage. New pages reuse the recent library shell, navigation, footer, print styles, annotations, ten-section order, financial table classes, author component, generator CTA, five FAQs and matching FAQ schema. Each has roughly 3,000–3,200 words and five financial tables: opening sources/uses, revenue drivers, income statement, cash flow and balance sheets. Break-even, disclosed repayment coverage and a combined sales/payroll downside accompany the statements.

All sample companies, founders, biographies and commercial assumptions are explicitly fictional and illustrative. No real brand is used as a sample company. No new The Biz Plans prices, client counts, testimonials or success claims are introduced. Existing site author copy is preserved. New JSON-LD contains no ratings.

The insurance model recognizes retained earned commissions, not premiums, excludes trust receipts and contingent bonuses, and conditions launch on applicable licences and carrier agreements. The custom-home model excludes customer land and speculative development; its simplified completed-handover accounting is explicitly distinguished from the monthly job, progress, deposit and holdback schedules a real plan needs. Carpentry excludes structural work; boutique resells purchased garments; pizza is takeout without alcohol.

## Validation

- Independently parsed displayed HTML tables with decimal arithmetic: all 15 modeled years reconcile unit/price revenue, contribution, EBITDA, tax/net income, working-capital movements, cash roll-forwards, net assets, debt, retained earnings and assets = liabilities + equity.
- Chromium checks at 1440 px and 390 px for each sample: one H1, ten numbered sections plus FAQs, five financial tables, working section targets and no document overflow. Reviewed desktop/mobile screenshots and a rendered PDF financial page; corrected unit-count formatting after visual review.
- All five PDFs use headless Chromium, existing print CSS, A4, background printing and 12 mm margins. Extracted text confirms company identity, financial statements and appendix. PDFs reproduce complete online plans.
- Checked internal article/sidebar targets, unique canonical metadata, FAQ text/schema parity, no rating data, one contextual inbound link per sample, 46 unique library cards and positions, and one sitemap inclusion per new sample.
- `node scripts/build-vercel-site.mjs work/site-dist` and `git diff --check` pass. This is a local static staging check, not deployment.
- Site-wide `python scripts/audit_site.py` and `python scripts/generate_seo.py --check` also fail on an extracted unchanged HEAD baseline. Existing failures include redirect/canonical disagreements, retired external links, sitemap drift and shared shell variants. The only additional page-specific audit findings are the template’s eager header-logo warning inherited by these five pages; the new canonicals are clean. Unrelated SEO findings are preserved.

No design/layout components, `/listings.html`, quote forms, generator source or bundles are changed. Existing related pages receive contextual text links only.
