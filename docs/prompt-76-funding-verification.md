# Prompt 76 — Federal funding verification report

Verified October 29, 2026 using the web tool to open the official program pages (not directory summaries). Article: `blog-federal-funding-programs-ontario-small-business.html`.

- Article body: 1,776 words, including section headings, decision table and FAQ; excluding shared navigation, hero, sidebar and footer.
- Title: Federal Funding Programs for Ontario Small Businesses (53 characters).
- Meta description: 155 characters after decoding HTML entities.
- Blog index: `blog-learning-hub.html`; sitemap URL added in alphabetical order and index lastmod updated.
- Three contextual internal links: `/small-business-grants-ontario.html` (primary), `/canada-small-business-financing-program.html`, `/business-loans-canada.html`.
- `what-is-bdc.html` does not exist, so that optional link was omitted.
- Based directly on main commit `65b737fa730db3d30beedc68225fbeeb9d3cd43d`; no dependency on an unmerged glossary PR.

## Included: seven verified options

### 1. Canada Small Business Financing Program

Official URL checked: https://www.ised-isde.canada.ca/site/canada-small-business-financing-program/en/canada-small-business-financing-program/find-loan-your-small-business/helping-small-businesses-get-loans

Current lender application instructions; no intake deadline stated. Verified lender risk sharing, startup/small-business eligibility, $10 million revenue ceiling, farming exclusion, asset and working-capital uses, and lender credit decision. Article quotes the published revenue ceiling, not loan maximums or rates.

### 2. BDC financing

Official URL checked: https://www.bdc.ca/en/financing

Current online assessment/application route; no general intake deadline stated. Verified Canadian registration, recorded sales, general 12-month revenue history guidance, financing catalogue and assessment limitations. Article treats BDC as financing with product-specific criteria, not as a grant.

### 3. Futurpreneur Startup Program

Official URLs checked:

- https://futurpreneur.ca/en/offering/core-startup/
- https://futurpreneur.ca/en/eligibility/

Current contact form and application route; no intake deadline stated on offering page. Verified age 18–39, citizenship/permanent residence, Canadian residence, startup stage, market readiness, business plan and 24-month cash flow, mentorship and BDC participation. Eligibility page excludes refinancing existing debt. Distinguished national nonprofit delivery from a direct federal grant.

### 4. FedDev Ontario funding for businesses

Official URLs checked:

- https://feddev-ontario.canada.ca/en/funding-southern-ontario/funding-businesses-southern-ontario-what-we-support
- https://feddev-ontario.canada.ca/en/funding-southern-ontario/funding-businesses-southern-ontario-who-can-apply
- https://feddev-ontario.canada.ca/en/funding-southern-ontario/funding-businesses-southern-ontario-how-funding-works
- https://feddev-ontario.canada.ca/en/funding-southern-ontario/funding-businesses-southern-ontario-how-apply
- https://feddev-ontario.canada.ca/en/funding-southern-ontario/funding-businesses-southern-ontario-application-guide

What-we-support and how-to-apply pages explicitly say applications are being accepted. Verified southern Ontario scope, incorporation history, minimum workforce, innovation/productivity/expansion uses and projections/work-plan requirements. How-funding-works timed out on direct open; its official indexed page text was retrieved through web search and confirms cost sharing and interest-free unconditional repayment. No funding amount or percentage quoted. Official eligibility page and application guide differ at the upper employee boundary (500 versus fewer than 500); article avoids this boundary and directs borderline applicants to the agency.

### 5. Canada Summer Jobs

Official URLs checked:

- https://www.canada.ca/en/employment-social-development/services/funding/canada-summer-jobs.html
- https://www.canada.ca/en/employment-social-development/services/funding/canada-summer-jobs/applicant-guide.html
- https://www.canada.ca/en/employment-social-development/services/funding/canada-summer-jobs/applicant-guide/who-can-apply.html

Applicant guide explicitly labels intake open from October 27, 2026 to December 3, 2026 at 11:59 pm Pacific Time, for 2027 summer jobs. Deadline and time zone transcribed from the official applicant guide. Verified youth age range, private-sector employer size, new two-year operating-history rule and exemption. No subsidy percentage quoted.

### 6. SR&ED tax incentives

Official URLs checked:

- https://www.canada.ca/en/revenue-agency/services/scientific-research-experimental-development-tax-incentive-program/what-are-sred-tax-incentives.html (overview URL redirects here)
- https://www.canada.ca/en/revenue-agency/services/scientific-research-experimental-development-tax-incentive-program/sred-eligibility.html
- https://www.canada.ca/en/revenue-agency/services/scientific-research-experimental-development-tax-incentive-program/sred-claim.html

Current claim instructions, eligibility rules and forms path verified. This is a tax-year-based claim route, not a periodic grant intake. Verified advancement/systematic investigation requirements, allowable cost categories, claimant types, deduction/ITC distinction and assistance interaction. No rates or universal filing deadline quoted.

### 7. NRC IRAP

Official URL checked: https://nrc.canada.ca/en/support-technology-innovation/financial-support-technology-innovation

Current executive contact/advisor engagement route; no general intake deadline stated. Verified incorporation, for-profit Canadian operations, up to 500 FTEs, technology innovation/commercialization purpose, required business plan and financial statements, excluded activities and non-guaranteed project funding. The article does not imply an advisor engagement is an approved award.

## Dropped candidate

**CanExport SMEs** — https://www.tradecommissioner.gc.ca/en/our-solutions/funding-financing-international-business/canexport-smes.html

Official page says the program is currently closed, all 2026–27 applications have been processed, and information about future intakes will be posted when available. No announced future intake to support inclusion. Dropped entirely from the article and decision table. No other candidate was dropped.

## Validation and limits

- Passed static content checks for article length, seven program entries and official links, three contextual internal links, existing local link targets, four FAQs, one H1, JSON-LD parsing, index entry and single sitemap entry.
- `git diff --check` passed.
- Ran required `python scripts/generate_seo.py --check` and `python scripts/audit_site.py`. Repo-wide checks fail on existing canonical drift, broken download references, retired links, shared-template variants and image warnings. Compared full audit with a clean archive of the unchanged main commit; no new error category was introduced. New post inherits the existing header logo loading warning from the blog template.
- Kept sitemap edits confined to the new URL and updated blog index timestamp. Did not regenerate unrelated canonical changes or change historical sitemap metadata.
- Chromium preview attempted but blocked at launch by environment restriction (`setsockopt: Operation not permitted`). No visual verification claimed.
- No application outcomes promised. No direct main update, merge or deployment authorized or performed.
