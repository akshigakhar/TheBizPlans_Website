# Internal-link audit — October 29, 2026

Baseline: `main` at `1647dc857d6309f893eb09b592d634dd2dd426a0`. All 336 repository HTML files were inspected, including redirect stubs and generator entry points. This is a static source audit, not a new Semrush crawl.

Counts are **distinct other source pages**, not repeated anchors on the same page. Body, navigation and footer counts are independent; total is their union (so do not sum the columns). `occurrences` additionally counts every anchor. Same-page links are excluded. Relative URLs, root URLs, absolute apex/www URLs, queries, fragments and directory index paths are normalized; `/` and `/index.html` are one target. Only HTTP(S) HTML destinations inside this repository are counted. Canonical tags, schema URLs, JavaScript-generated links and offsite links are not incoming anchors. Redirect stub fallback anchors count as source anchors, but redirects themselves are not link edges. Destination aliases are reported separately rather than silently consolidated.

Navigation includes `<nav>`, `<header>`, role=navigation and navbar/global-header/breadcrumb containers; footer anchors are reported separately; other body anchors are body content. Local table-of-contents navigation is classified as navigation. This source-based method may differ from Semrush's crawl scope, cached pages and redirect handling.

The baseline has **55 files with total inlinks ≤1: 25 content pages and 30 redirect stubs**. Each of the 25 content pages gains two links from two previously unlinked source pages. The three additional named Semrush examples (cleaning, dental and ecommerce) already have multiple source pages on current main and also gain two links each. The homepage has 42 body sources and 304 navigation sources before the change; it gains three new body sources (45 after). Its union total stays 306 because those sources already link through navigation.

**Redirect treatment:** all 30 stubs are listed below and remain unchanged. Adding links to legacy redirects would direct readers and crawlers through an unnecessary hop. New links point at content URLs; this is the intentional exception to adding links to every HTML file with ≤1 inlink. No URL, title, H1, canonical, global navigation or footer was changed.

59 new body anchors across 42 edited HTML pages. No content page remains at total ≤1. See `all-pages.csv` for all 336 before/after rows and `added-links.csv` for every added source, target, anchor and sentence.

## Full list of files with at most one incoming source

| Page | Body | Navigation | Footer | Total | Treatment |
|---|---:|---:|---:|---:|---|
| ainp-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/aaip-entrepreneur-business-plan.html |
| bc-pnp-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/bcpnp-business-plan.html |
| blog-business-plan-for-loan-application.html | 0 | 0 | 0 | 0 | Two new contextual source pages |
| blog-federal-funding-programs-ontario-small-business.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-how-much-does-a-business-plan-cost-canada.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-how-to-validate-a-business-idea.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-how-to-write-csbfp-business-plan.html | 0 | 0 | 0 | 0 | Two new contextual source pages |
| blog-ict-work-permit-business-plan.html | 0 | 0 | 0 | 0 | Two new contextual source pages |
| blog-key-elements-effective-executive-summary.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/blog-executive-summary-key-elements.html |
| blog-sample-auto-repair-shop-business-plan.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-sample-brewery-business-plan.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-sample-construction-company-business-plan.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-sample-event-venue-business-plan.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-sample-gym-business-plan.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-sample-hair-salon-business-plan.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-sample-landscaping-business-plan.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-sample-laundromat-business-plan.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-sample-liquor-store-business-plan.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-sample-pet-grooming-business-plan.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-small-business-grants-ontario-how-to-apply.html | 0 | 0 | 0 | 0 | Two new contextual source pages |
| blog-startup-visa-paused-alternatives.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-tam-sam-som-mistakes.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| blog-what-lenders-look-for-in-a-business-plan.html | 0 | 0 | 0 | 0 | Two new contextual source pages |
| cleaning-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/blog-sample-cleaning-company-business-plan.html |
| coffee-shop-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/blog-sample-coffee-shop-business-plan.html |
| cogs-meaning.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| convenience-store-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/sample-business-plans.html |
| dental-clinic-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/blog-sample-dental-clinic-business-plan.html |
| e-commerce-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/blog-sample-ecommerce-business-plan.html |
| es/index.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/ |
| fr/index.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/ |
| funding-solutions.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/business-loans-canada.html |
| gas-station-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/sample-business-plans.html |
| help.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/contact.html |
| industries/daycare-business-plan/index.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/blog-sample-daycare-business-plan.html |
| industries/index.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/sample-business-plans.html |
| industries/restaurant-business-plan/index.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/blog-sample-restaurant-business-plan.html |
| investor-plans.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/investor-business-plan.html |
| listings.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| lmia-imp-c10-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/immigration-business-plans.html |
| locations.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/contact.html |
| locations/index.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/contact.html |
| logistics-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/blog-sample-trucking-company-business-plan.html |
| manufacturing-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/sample-business-plans.html |
| pharmacy-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/blog-sample-pharmacy-business-plan.html |
| pnp-business-plans.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/immigration-business-plans.html |
| real-estate-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/blog-sample-real-estate-brokerage-business-plan.html |
| resources/index.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/canadian-business-plan-benchmarks-2026.html |
| restaurant-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/blog-sample-restaurant-business-plan.html |
| rfp-meaning.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| scarborough-business-plan-writers.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/toronto-business-plan-writers.html |
| service-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/services.html |
| spa-business-plan.html | 0 | 0 | 0 | 0 | Redirect: 0; url=/beauty-salon-business-plans.html |
| what-is-an-sme.html | 1 | 0 | 0 | 1 | Two new contextual source pages |
| what-is-bdc.html | 1 | 0 | 0 | 1 | Two new contextual source pages |

## Before/after for every edited source and linked target

| Page (edited source or linked target) | Body before → after | Navigation before → after | Footer before → after | Total before → after |
|---|---:|---:|---:|---:|
| about.html | 29 → 29 | 0 → 0 | 295 → 295 | 295 → 295 |
| bank-loan-business-plans.html | 71 → 71 | 304 → 304 | 304 → 304 | 305 → 305 |
| beauty-salon-business-plans.html | 11 → 11 | 7 → 7 | 0 → 0 | 12 → 12 |
| blog-business-plan-for-loan-application.html | 0 → 2 | 0 → 0 | 0 → 0 | 0 → 2 |
| blog-federal-funding-programs-ontario-small-business.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-how-much-does-a-business-plan-cost-canada.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-how-to-validate-a-business-idea.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-how-to-write-csbfp-business-plan.html | 0 → 2 | 0 → 0 | 0 → 0 | 0 → 2 |
| blog-ict-work-permit-business-plan.html | 0 → 2 | 0 → 0 | 0 → 0 | 0 → 2 |
| blog-industry-analysis.html | 7 → 7 | 0 → 0 | 0 → 0 | 7 → 7 |
| blog-sample-auto-repair-shop-business-plan.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-sample-brewery-business-plan.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-sample-car-dealership-business-plan.html | 2 → 2 | 0 → 0 | 0 → 0 | 2 → 2 |
| blog-sample-cleaning-company-business-plan.html | 2 → 4 | 0 → 0 | 0 → 0 | 2 → 4 |
| blog-sample-clothing-line-business-plan.html | 4 → 4 | 0 → 0 | 0 → 0 | 4 → 4 |
| blog-sample-construction-business-plan.html | 2 → 2 | 0 → 0 | 0 → 0 | 2 → 2 |
| blog-sample-construction-company-business-plan.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-sample-dental-clinic-business-plan.html | 2 → 4 | 0 → 0 | 0 → 0 | 2 → 4 |
| blog-sample-ecommerce-business-plan.html | 2 → 4 | 0 → 0 | 0 → 0 | 2 → 4 |
| blog-sample-esthetician-business-plan.html | 4 → 4 | 0 → 0 | 0 → 0 | 4 → 4 |
| blog-sample-event-venue-business-plan.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-sample-gym-business-plan.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-sample-hair-salon-business-plan.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-sample-landscaping-business-plan.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-sample-laundromat-business-plan.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-sample-liquor-store-business-plan.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-sample-painting-company-business-plan.html | 8 → 8 | 0 → 0 | 0 → 0 | 8 → 8 |
| blog-sample-pet-grooming-business-plan.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-sample-pet-store-business-plan.html | 8 → 8 | 0 → 0 | 0 → 0 | 8 → 8 |
| blog-sample-pharmacy-business-plan.html | 2 → 2 | 0 → 0 | 0 → 0 | 2 → 2 |
| blog-sample-restaurant-business-plan.html | 13 → 13 | 0 → 0 | 0 → 0 | 13 → 13 |
| blog-sample-welding-company-business-plan.html | 4 → 4 | 0 → 0 | 0 → 0 | 4 → 4 |
| blog-small-business-grants-ontario-how-to-apply.html | 0 → 2 | 0 → 0 | 0 → 0 | 0 → 2 |
| blog-startup-visa-paused-alternatives.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-tam-sam-som-mistakes.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| blog-what-lenders-look-for-in-a-business-plan.html | 0 → 2 | 0 → 0 | 0 → 0 | 0 → 2 |
| brewery-business-plans.html | 2 → 2 | 1 → 1 | 304 → 304 | 305 → 305 |
| business-loans-canada.html | 15 → 15 | 0 → 0 | 304 → 304 | 305 → 305 |
| business-plan-cost-timeline-checklist.html | 18 → 18 | 1 → 1 | 0 → 0 | 19 → 19 |
| business-plan-template.html | 12 → 12 | 303 → 303 | 304 → 304 | 304 → 304 |
| canada-small-business-financing-program.html | 68 → 68 | 304 → 304 | 304 → 304 | 305 → 305 |
| canadian-bank-loan-business-plan-guide.html | 13 → 13 | 304 → 304 | 0 → 0 | 304 → 304 |
| cogs-meaning.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| construction-business-plans.html | 12 → 12 | 304 → 304 | 304 → 304 | 305 → 305 |
| contact.html | 119 → 119 | 303 → 303 | 305 → 305 | 308 → 308 |
| financial-modeling.html | 82 → 82 | 304 → 304 | 304 → 304 | 305 → 305 |
| grocery-business-plans.html | 12 → 12 | 7 → 7 | 0 → 0 | 13 → 13 |
| how-banks-evaluate-business-plans.html | 29 → 29 | 1 → 1 | 0 → 0 | 30 → 30 |
| how-to-start-a-business-in-ontario.html | 2 → 2 | 0 → 0 | 0 → 0 | 2 → 2 |
| how-to-write-business-plan-for-bdc-loan.html | 3 → 3 | 0 → 0 | 0 → 0 | 3 → 3 |
| ict-business-plan.html | 11 → 11 | 1 → 1 | 0 → 0 | 12 → 12 |
| immigration-business-plans.html | 29 → 29 | 1 → 1 | 304 → 304 | 307 → 307 |
|  /  | 42 → 45 | 304 → 304 | 0 → 0 | 306 → 306 |
| industry-business-plans.html | 15 → 15 | 304 → 304 | 304 → 304 | 305 → 305 |
| listings.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| medical-services-business-plans.html | 1 → 1 | 304 → 304 | 304 → 304 | 305 → 305 |
| pricing.html | 24 → 24 | 304 → 304 | 305 → 305 | 305 → 305 |
| rfp-meaning.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| sample-business-plans.html | 43 → 43 | 15 → 15 | 304 → 304 | 308 → 308 |
| small-business-financing-canada.html | 12 → 12 | 303 → 303 | 304 → 304 | 304 → 304 |
| small-business-grants-ontario.html | 10 → 10 | 0 → 0 | 0 → 0 | 10 → 10 |
| small-business-ideas.html | 4 → 4 | 0 → 0 | 0 → 0 | 4 → 4 |
| startup-visa-business-plan.html | 12 → 12 | 1 → 1 | 0 → 0 | 13 → 13 |
| tam-sam-som.html | 26 → 26 | 0 → 0 | 0 → 0 | 26 → 26 |
| what-is-an-sme.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |
| what-is-bdc.html | 1 → 3 | 0 → 0 | 0 → 0 | 1 → 3 |

## Added link inventory

| Source page | Destination | Added anchor text |
|---|---|---|
| bank-loan-business-plans.html | blog-business-plan-for-loan-application.html | business plan for a loan application |
| canadian-bank-loan-business-plan-guide.html | blog-business-plan-for-loan-application.html | business plan for a loan application |
| small-business-financing-canada.html | blog-federal-funding-programs-ontario-small-business.html | federal funding programs for Ontario small businesses |
| small-business-grants-ontario.html | blog-federal-funding-programs-ontario-small-business.html | federal funding programs for Ontario small businesses |
| pricing.html | blog-how-much-does-a-business-plan-cost-canada.html | what a business plan costs in Canada |
| business-plan-cost-timeline-checklist.html | blog-how-much-does-a-business-plan-cost-canada.html | what a business plan costs in Canada |
| business-plan-template.html | blog-how-to-validate-a-business-idea.html | validate a business idea before commissioning a plan |
| small-business-ideas.html | blog-how-to-validate-a-business-idea.html | validate a business idea before commissioning a plan |
| canada-small-business-financing-program.html | blog-how-to-write-csbfp-business-plan.html | step-by-step CSBFP business plan guide |
| canadian-bank-loan-business-plan-guide.html | blog-how-to-write-csbfp-business-plan.html | step-by-step CSBFP business plan guide |
| ict-business-plan.html | blog-ict-work-permit-business-plan.html | what officers assess in an ICT business plan |
| immigration-business-plans.html | blog-ict-work-permit-business-plan.html | what officers assess in an ICT business plan |
| small-business-grants-ontario.html | blog-small-business-grants-ontario-how-to-apply.html | how to apply for small business grants in Ontario |
| business-loans-canada.html | blog-small-business-grants-ontario-how-to-apply.html | how to apply for small business grants in Ontario |
| startup-visa-business-plan.html | blog-startup-visa-paused-alternatives.html | alternatives while Canada’s Startup Visa is paused |
| immigration-business-plans.html | blog-startup-visa-paused-alternatives.html | alternatives while Canada’s Startup Visa is paused |
| tam-sam-som.html | blog-tam-sam-som-mistakes.html | TAM, SAM and SOM mistakes lenders spot |
| blog-industry-analysis.html | blog-tam-sam-som-mistakes.html | TAM, SAM and SOM mistakes lenders spot |
| bank-loan-business-plans.html | blog-what-lenders-look-for-in-a-business-plan.html | what lenders look for in a business plan |
| how-banks-evaluate-business-plans.html | blog-what-lenders-look-for-in-a-business-plan.html | what lenders look for in a business plan |
| financial-modeling.html | cogs-meaning.html | cost of goods sold and gross margin |
| blog-sample-ecommerce-business-plan.html | cogs-meaning.html | cost of goods sold and gross margin |
| blog-sample-construction-business-plan.html | rfp-meaning.html | how to respond to a request for proposal |
| construction-business-plans.html | rfp-meaning.html | how to respond to a request for proposal |
| small-business-financing-canada.html | what-is-an-sme.html | Canadian SME definitions and employee bands |
| how-to-start-a-business-in-ontario.html | what-is-an-sme.html | Canadian SME definitions and employee bands |
| business-loans-canada.html | what-is-bdc.html | what the Business Development Bank of Canada does |
| how-to-write-business-plan-for-bdc-loan.html | what-is-bdc.html | what the Business Development Bank of Canada does |
| about.html | listings.html | The Biz Plans’ business listings and directories |
| contact.html | listings.html | The Biz Plans’ business listings and directories |
| industry-business-plans.html | blog-sample-auto-repair-shop-business-plan.html | auto repair shop business plan sample |
| blog-sample-car-dealership-business-plan.html | blog-sample-auto-repair-shop-business-plan.html | auto repair shop business plan sample |
| brewery-business-plans.html | blog-sample-brewery-business-plan.html | brewery business plan sample |
| blog-sample-liquor-store-business-plan.html | blog-sample-brewery-business-plan.html | brewery business plan sample |
| construction-business-plans.html | blog-sample-construction-company-business-plan.html | construction company business plan sample |
| blog-sample-welding-company-business-plan.html | blog-sample-construction-company-business-plan.html | construction company business plan sample |
| industry-business-plans.html | blog-sample-event-venue-business-plan.html | event venue business plan sample |
| blog-sample-restaurant-business-plan.html | blog-sample-event-venue-business-plan.html | event venue business plan sample |
| industry-business-plans.html | blog-sample-gym-business-plan.html | gym business plan sample |
| blog-sample-dental-clinic-business-plan.html | blog-sample-gym-business-plan.html | gym business plan sample |
| beauty-salon-business-plans.html | blog-sample-hair-salon-business-plan.html | hair salon business plan sample |
| blog-sample-esthetician-business-plan.html | blog-sample-hair-salon-business-plan.html | hair salon business plan sample |
| construction-business-plans.html | blog-sample-landscaping-business-plan.html | landscaping business plan sample |
| blog-sample-painting-company-business-plan.html | blog-sample-landscaping-business-plan.html | landscaping business plan sample |
| industry-business-plans.html | blog-sample-laundromat-business-plan.html | laundromat business plan sample |
| blog-sample-cleaning-company-business-plan.html | blog-sample-laundromat-business-plan.html | laundromat business plan sample |
| brewery-business-plans.html | blog-sample-liquor-store-business-plan.html | liquor store business plan sample |
| grocery-business-plans.html | blog-sample-liquor-store-business-plan.html | liquor store business plan sample |
| industry-business-plans.html | blog-sample-pet-grooming-business-plan.html | pet grooming business plan sample |
| blog-sample-pet-store-business-plan.html | blog-sample-pet-grooming-business-plan.html | pet grooming business plan sample |
| industry-business-plans.html | blog-sample-cleaning-company-business-plan.html | cleaning company business plan sample |
| blog-sample-landscaping-business-plan.html | blog-sample-cleaning-company-business-plan.html | cleaning company business plan sample |
| medical-services-business-plans.html | blog-sample-dental-clinic-business-plan.html | dental clinic business plan sample |
| blog-sample-pharmacy-business-plan.html | blog-sample-dental-clinic-business-plan.html | dental clinic business plan sample |
| industry-business-plans.html | blog-sample-ecommerce-business-plan.html | ecommerce business plan sample |
| blog-sample-clothing-line-business-plan.html | blog-sample-ecommerce-business-plan.html | ecommerce business plan sample |
| pricing.html | / | business plan writing services |
| sample-business-plans.html | / | business plan writing services |
| contact.html | / | business plan writing services |

## Validation

Validated: each added href resolves to an existing non-redirect HTML target; all 59 additions are body anchors; each low-inlink content page gains two distinct new sources; homepage gains three distinct body sources; titles/H1s/canonicals/navigation/footer subtrees remain identical; no original anchors were removed. Counts are static; deployed crawl results require a later Semrush recrawl after merge and deployment.
