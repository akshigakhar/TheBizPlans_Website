# Prompt 57 CSBFP recovery report

Checked October 26, 2026 (America/Toronto). Implementation prepared for a pull request; deployment is outside this change. Three existing HTML files changed: the CSBFP guide, homepage and target-market post. This report and an inbound-link inventory are review artifacts.

## Recovery diagnosis

Search Console: BLOCKED / NOT CHECKED. No Search Console connector, configured identity, secret or supplied export is available. URL Inspection indexed status, Google-selected canonical, coverage changes around October 14–21 and page-query losses remain unknown. Requested Akshi's URL Inspection and 28-day comparison export while proceeding with independently authorized work. No penalty, algorithm update or index/canonical problem is claimed. An HTML canonical is not evidence of Google's canonical selection.

The supplied Position Tracking update establishes loss from tracked top positions. Position Tracking and Organic Research disagree on the baseline: Organic Research had the head term at #31 on October 18, while Tracking reports changes from different positions. No single exact drop is treated as settled. No new volume estimates are introduced.

Live web fetches returned complete CSBFP and BDC representations with older titles and content than this checkout, including July/September review notes. This may reflect deployment lag or the retrieval service's representation; it does not establish a cause of ranking loss. A fresh direct HTTP comparison could not be completed because the configured shell proxy was unreachable. The web tool could not retrieve the pillar or sitemap; per the user's October 26 note, treat the pillar as live and preserve the active intent boundary. Do not infer a current 404 from retrieval failure.

## Title / H1 / opening comparison with Prompt 35

Read repair commit d284696 and /workspace/CSBFP-BDC-repair-report.md, plus the current pillar. Repo title stays “Canada Small Business Financing Program (CSBFP) Guide” (53 characters). H1 stays “Canada Small Business Financing Program (CSBFP): Loan & Business Plan Guide”. The live retrieval showed “Canada Small Business Financing Program Guide”; its H1 matched in intent and wording. Its opening and the repo opening already contained the head term but lacked both close variants. The revised opening contains Canada Small Business Financing loan and Canadian small business financing program naturally within its first 100 words; an eligibility subhead also uses the loan variant. Title and H1 intent remain intact.

The current repo's numeric eligibility/fee content postdates the qualitative fallback described in the repair report. All retained figures were rechecked now rather than inherited as verified. The live representation's exclusion of nonprofit and charitable businesses conflicts with ISED's current FAQ. The repo already corrects it; that correction is preserved.

## Intent boundary and conflicts

CSBFP eligibility, uses and application detail stay on this page. Loan shopping stays on business-loans-canada.html, and BDC-bank intent stays on its own page. Existing Prompt 35 definition heading, comparison table, default guidance, author schema and related-resource links remain. No new landscape comparison or BDC targeting was added.

Explicit specification conflict: Prompt 57 asks for 6–7 FAQs, but Prompt 35's repaired page already has 12 and Prompt 57 says not to undo its repairs. Preserved 12, including all seven requested topics. Retargeted the existing business-plan-content FAQ to “What documents does a CSBFP lender need?” with a matching answer and schema. No extra duplicate FAQPage node was introduced. All other existing FAQ subjects remain.

## Sections and counts

Counts use whitespace-delimited article text excluding tables, scripts and styles; include headings, TOC, FAQs and the article sidebar. They exclude shared navigation/footer and the opening summary. Baseline: 3028 words; after: 4267 words. A new illustrative example, deeper eligibility, costs, application sequence and document guidance account for the expansion. These are counts of final sections, not net additions:

| Section | Words excluding tables |
|---|---:|
| What is the CSBFP? | 78 |
| Who qualifies for a Canada Small Business Financing loan? | 289 |
| How Much Can You Borrow Through CSBFP? | 422 |
| Illustrative example: financing a defined equipment purchase | 301 |
| What a CSBFP loan can and cannot fund | 250 |
| CSBFP vs. a regular bank loan | 6 |
| How to apply for CSBFP through a lender | 413 |
| Do You Need a Business Plan for a CSBFP Loan? | 124 |
| What Should a CSBFP Business Plan Include? | 296 |
| What Makes a CSBFP Business Plan Different From a Regular Business Plan? | 252 |
| Financial Projections for a CSBFP Loan | 218 |
| Documents to Prepare Before Applying | 336 |
| Common Problems That Can Weaken a Financing Application | 140 |
| How The Biz Plans Can Help With a CSBFP Financing Application | 154 |
| Frequently Asked Questions | 568 |
| Related Financing Resources | 130 |
| Build a plan that matches the financing request | 35 |
| Speak with a business plan expert | 47 |

## Official sources and every program figure

All sources below were retrieved through the web tool during this run and checked October 26, 2026. Source pages may show their own older modification dates. They are not approval offers.

- A: ISED, [Helping small businesses get loans](https://ised-isde.canada.ca/site/canada-small-business-financing-program/en/canada-small-business-financing-program/find-loan-your-small-business/helping-small-businesses-get-loans).
- B: ISED, [Frequently asked questions—For small businesses](https://ised-isde.canada.ca/site/canada-small-business-financing-program/en/frequently-asked-questions-small-businesses).
- C: ISED, [Canada Small Business Financing Program Guidelines](https://ised-isde.canada.ca/site/canada-small-business-financing-program/en/canada-small-business-financing-program/find-loan-your-small-business/canada-small-business-financing-program-guidelines).

| Program figure / rule | Verification |
|---|---|
| Gross annual revenue ceiling CAD $10 million | A eligibility; B question 1 |
| Combined financing ceiling CAD $1.15 million | A available financing; B question 5 |
| Term loans up to CAD $1 million, including real property | A available financing / uses; C section 3.1 |
| Nested CAD $500,000 equipment/leasehold ceiling | A available financing; C section 3.1 |
| Within that ceiling, CAD $150,000 intangible-assets/working-capital sub-limit | A available financing; C section 3.1 |
| Line of credit up to CAD $150,000 | A available financing; B question 5 |
| 2% registration fee, borrower pays lender; may be financed | A registration fee; B question 6; C sections 4.1.5 and 10.1 |
| Term-loan fee based on amount loaned; LOC fee based on authorized amount | A registration fee; C section 10.1 |
| Floating term-loan interest ceiling: lender prime + 3 percentage points | A interest rates; B question 6 |
| Fixed term-loan ceiling: lender single-family residential mortgage rate for that term + 3 percentage points | A interest rates |
| LOC interest ceiling: lender prime + 5 percentage points | A interest rates; B question 6 |
| No asserted universal minimum borrower contribution | B question 5; C section 5.1: negotiated lender financing percentage |
| Financed registration fees count within category ceilings | C section 4.1.5 |
| Refundable taxes excluded in eligible-cost calculation | C section 5.4 |
| Eligible Canadian startups/operating businesses, entity types, nonprofits/charities; farming excluded | A eligibility; B question 1 |
| Eligible cost categories, share-purchase/holding-company exclusions | A uses; B questions 2–4 |
| Goodwill permitted as an intangible in a going-concern purchase | C section 4.1.4; not blanket goodwill eligibility |
| Lender decides; lender disburses and registers | A application; B questions 7–8 |
| Due diligence and repayment assessment remain necessary | C section 1 |
| Borrower remains liable; realization/security/guarantees may apply | C sections 21–22; no borrower debt forgiveness implied |

No unverifiable existing numeric figure was deleted because the figures present in the repo were confirmed. No universal contribution percentage, loss-sharing percentage, processing deadline or approval timeline was inserted. The earlier incorrect source path for the Guidelines was not used; the official FAQ's link resolved the current path. Personal financial statements and other document suggestions are clearly labelled lender-dependent preparation guidance, not mandatory program rules.

The fictional bakery's CAD $100,000 eligible equipment purchase, 80% negotiated financing assumption, CAD $80,000 asset advance, CAD $20,000 asset contribution, CAD $1,600 fee, CAD $21,600 total borrower cash and CAD $101,600 total uses are all illustrative. Only the 2% fee is a verified rule. Borrower pays the example's fee separately, avoiding circular fee-financing arithmetic. The example excludes refundable-tax cash timing and other costs from its simplified contribution, and flags their separate funding needs.

## Internal links in both directions

New outbound link: small-business-grants-ontario.html, anchor “small business grants in Ontario guide”, explicitly Ontario-scoped. Existing outbound links retained to the live-concern pillar, BDC, writing services, generator and Benchmarks; the services and Benchmarks links also appear in the new lender-document explanation. All required six destinations exist in the repo. The example receives a TOC anchor.

New contextual inbound links:

| Source | Anchor |
|---|---|
| index.html | Canada Small Business Financing Program guide |
| blog-identifying-target-market.html | Canada Small Business Financing Program application guide |

The pillar already has contextual “CSBFP loan” and “CSBFP financing” links; BDC already has a contextual “CSBFP” link. Neither file changed, respecting the instruction to add links only if absent. Homepage retains its old CSBFP chip and gains a descriptive paragraph. The target-market post previously had only shared navigation/footer links.

The accompanying CSV lists every matching link found across repo HTML, with page, destination, exact anchor and a contextual/shared flag. Contextual source pages after changes: 48; all source pages including shared links: 270. This is a repo inventory, not a completed live-site census. Live sitemap retrieval and shell crawling were unavailable; the web tool confirmed the BDC contextual guide link and the target-market post's shared-only representation, but cannot establish all live anchors or all deployed pages. No current traffic ranking was independently measured; priority pages were selected from the addendum.

## Validation and delivery limits

Passed: 2,800+ words excluding tables; one unchanged H1; 53-character title; valid static JSON-LD; one FAQPage with all 12 visible questions/answers matching exactly; existing Person schema retained; every article-local file and fragment target exists; unique IDs; sitemap byte content unchanged; git diff --check. This is a static content change: generator build/test execution is unrelated and was not repeated.

Visual browser validation could not run: Playwright's bundled browser is absent and the installed system Chromium exits at startup with a crashpad socket permission error. No desktop/mobile rendering or live HTTP-200 claim is made for this run.

The content and report are submitted together for pull-request review; no deployment was performed during content preparation. GSC diagnosis and a full live-link inventory remain open. The environment's advertised /codex/.../output directory does not exist and its parent filesystem is read-only, so artifacts are saved in the repo reports directory and /workspace/work/p57/output instead. No permission escalation or approval rejection occurred.

## Contextual inbound pages and exact anchors (repo)

| Source | Anchor(s) |
|---|---|
| bank-loan-business-plans.html | CSBFPProgram guide; Canada Small Business Financing Program; Canada Small Business Financing Program (CSBFP) Business Plan |
| black-entrepreneurship.html | Canada Small Business Financing Program (CSBFP) Business Plan |
| blog-bank-asked-one-question.html | Canada Small Business Financing Program; small business financing in Canada |
| blog-ideal-business-plan.html | CSBFP financing guide |
| blog-identifying-target-market.html | CSBFP planning guide; Canada Small Business Financing Program application guide |
| blog-sample-bakery-business-plan.html | CSBFP |
| blog-sample-clothing-line-business-plan.html | CSBFP |
| blog-sample-coffee-shop-business-plan.html | CSBFP planning guide |
| blog-sample-daycare-business-plan.html | Canada Small Business Financing Program hub |
| blog-sample-esthetician-business-plan.html | Canada Small Business Financing Program |
| blog-sample-food-truck-business-plan.html | CSBFP guide |
| blog-sample-painting-company-business-plan.html | Canada Small Business Financing Program |
| blog-sample-restaurant-business-plan.html | Canada Small Business Financing Program guide |
| blog-sample-trucking-company-business-plan.html | Canada Small Business Financing Program (CSBFP) |
| blog-sample-welding-company-business-plan.html | Canada Small Business Financing Program |
| blog-small-business-ideas-canada.html | Canada Small Business Financing Program (CSBFP) |
| business-development-bank-of-canada.html | CSBFP |
| business-loans-canada.html | CSBFP loan; CSBFP financing; CSBFP guide |
| business-plan-components.html | Canada Small Business Financing Program (CSBFP) Business Plan |
| business-plan-cost-timeline-checklist.html | Canada Small Business Financing Program (CSBFP) Business Plan |
| business-plan-generator.html | CSBFP hub |
| canadian-bank-loan-business-plan-guide.html | Canada Small Business Financing Program (CSBFP) Business Plan |
| canadian-business-plan-benchmarks-2026.html | CSBFP resource |
| case-studies.html | Canada Small Business Financing Program (CSBFP) |
| cibc.html | Program page; CIBC; CSBFP planningLearn more; Canada Small Business Financing Program (CSBFP) Business Plan |
| contact.html | Canada Small Business Financing Program (CSBFP) Business Plan |
| desjardins.html | Canada Small Business Financing Program (CSBFP) Business Plan |
| executive-summary-example.html | Canada Small Business Financing Program (CSBFP) Business Plan |
| farm-credit-canada.html | Canada Small Business Financing Program (CSBFP) Business Plan |
| fractional-cfo-services.html | CSBFP guide |
| franchise-business-plans.html | Canada Small Business Financing Program (CSBFP); Canada Small Business Financing Program |
| how-banks-evaluate-business-plans.html | Canada Small Business Financing Program (CSBFP) Business Plan |
| how-to-start-a-business-in-ontario.html | Canada Small Business Financing Program hub |
| index.html | Canada Small Business Financing Program guide; CSBFP |
| indigenous-aboriginal-entrepreneurship.html | Canada Small Business Financing Program (CSBFP) Business Plan |
| national-bank-of-canada.html | Canada Small Business Financing Program (CSBFP) Business Plan |
| private-lender-alternative-financing.html | Canada Small Business Financing Program (CSBFP) Business Plan |
| royal-bank-of-canada.html | Canada Small Business Financing Program (CSBFP); Canada Small Business Financing Program (CSBFP) Business Plan |
| sample-other-plan.html | CSBFP guide |
| sba-business-plan.html | Canada Small Business Financing Program guide; CSBFP: Canadian counterpart |
| scotiabank.html | Canada Small Business Financing Program (CSBFP) guide |
| services.html | Canada Small Business Financing Program (CSBFP) |
| small-business-financing-canada.html | Read our CSBFP guide; CSBFP |
| small-business-grants-ontario.html | CSBFP hub; CSBFP guide; CSBFP financing route; CSBFP hub |
| small-business-ideas.html | CSBFP |
| td-canada-trust.html | Canada Small Business Financing Program (CSBFP) |
| us-business-plans.html | CSBFP: Canadian financing comparison |
| women-entrepreneurship-loan-fund.html | Canada Small Business Financing Program (CSBFP) Business Plan |
