# SEO implementation report — August 2026

## Audit scope and method

The repository was audited before implementation. The audit covered all **222 tracked HTML files** (221 indexable URLs because `/index.html` redirects to `/`), page metadata and headings, JSON-LD, local links and assets, the XML sitemap, robots directives, redirects, shared navigation, content clusters and conversion paths. The automated crawler currently reports **33,998 internal-link occurrences**, no broken local targets, no orphan indexable pages, no duplicate titles or H1s, one non-empty H1 and description per indexable page, complete canonical coverage, valid schema on every indexable page, and no missing image alt attributes.

The site is static HTML. Public URLs use root-level `.html` filenames, except the canonical homepage `/`. Apache redirects `index.html`, normalizes HTTPS/apex-host requests and consolidates listed legacy URLs. `robots.txt` allows the public site, blocks query-string and repository/support paths, and declares the canonical sitemap. `sitemap.xml` lists 221 canonical URLs. Google Tag Manager and existing presentation assets are retained.

## Existing inventory and navigation

The complete URL and link-occurrence inventory remains in `docs/site-audit-report.md`. The primary navigation is **Home, Services, Financing, Immigration, Industries, Learn, Results, Pricing**, plus a consultation CTA. Important existing clusters include:

- **Business plans:** homepage, services, bank-loan, investor, immigration and strategic service pages; template/outline; book and ten educational chapters; review, cost/timeline and comparison guides; 20 industry hubs plus supporting loan, projections, investor, franchise, pitch-deck and cost-calculator pages.
- **Financing:** a national financing guide; CSBFP and BDC guides; bank-loan service and bank-evaluation guides; Canadian bank, credit-union, agricultural, EDC, Futurpreneur, private-lender, women, Black and Indigenous financing pages.
- **Consulting/finance:** financial modelling, marketing/growth strategy, strategic business plans, financial due diligence and feasibility study content.
- **Tools:** industry-specific startup-cost calculators exist. The repository does **not** contain a general interactive free business-plan builder, so the template page must not claim one exists.
- **Educational:** learning hub, business-plan glossary, executive-summary series, market research/SWOT articles and book chapters. EBITDA receives glossary coverage, but SME and RFP do not yet have authoritative standalone guides.
- **Gaps:** no dedicated national/provincial grant hub, CanExport SME/Innovation, Strategic Innovation Fund, Canada–Ontario Job Grant, Rapid Innovation Fund, fractional CFO service, SME guide or RFP guide was found.

## Existing pages that should remain unchanged

| Current URL | Reason |
| --- | --- |
| `/` | Strong national commercial homepage with unique title/H1, Organization/WebSite schema and links into core services. |
| `/services.html` | Clear commercial business-plan-services hub and differentiated conversion intent. |
| `/bank-loan-business-plans.html` | Strong commercial page for lender-ready plan preparation; should support, not compete with, the informational financing hub. |
| `/canada-small-business-financing-program.html` | Already consolidates CSBFP variants into one authoritative page and covers eligibility, costs, lender role, process, failure points, planning and projections. |
| `/business-development-bank-of-canada.html` | Existing independent informational BDC guide includes a clear non-affiliation position and application-planning content. |
| `/financial-modeling.html` | Appropriate commercial target for financial projections/modelling. |
| `/industry-business-plans.html` and industry clusters | Genuine industry-specific intent with supporting calculators and financing/projection pages; retain while monitoring quality and performance. |

## Existing pages optimized in Priority 1

| Current URL | Target cluster | Primary keyword | Secondary keywords | Issue found | Improvement implemented |
| --- | --- | --- | --- | --- | --- |
| `/sample-other-plan.html` | Canadian templates and examples | business plan template Canada | business plan examples; sample format of business plan; small business plan; executive summary | Existing relevant page had a generic title/H1, thin usage guidance and skipped from H2 to H4. Creating `/business-plan-template-canada/` would duplicate its intent. | Repositioned existing URL, improved title/description/social metadata/H1, added Canadian application guidance, fixed section hierarchy and linked to financing, CSBFP, projections, industries and services. |
| `/small-business-financing-canada.html` | Canadian loans and financing | small business loans Canada | business loans Canada; business loan Canada; how to get a business loan; business funding; small business financing | Comprehensive hub existed, but the title/H1 emphasized only the broader “financing” term and its document checklist did not link to the template. | Assigned all loan variants to this one informational hub, updated metadata/H1 naturally and added the template link. |

## Existing pages recommended for later optimization

| Current URL | Cluster / primary keyword | Secondary keywords | Current issue | Recommended improvement | Priority |
| --- | --- | --- | --- | --- | --- |
| `/business-plan-glossary.html` | business finance glossary | EBITDA; COGS; margins; feasibility | Broad glossary cannot fully satisfy every high-volume definition query. | Keep concise definitions here and link to selective deep guides; do not create a page for every term. | 2 |
| `/strategic-business-plan.html` | strategic planning | strategic planification; strategic business solutions | Commercial planning intent overlaps somewhat with educational strategy language. | Clarify service deliverables and create a separate guide only if Search Console confirms informational demand. | 2 |
| `/blog-executive-summary*.html` (five pages) | executive summary | ex summary; executive summary examples/tips | Multiple pages address closely related intent and may cannibalize. | Choose one pillar, substantially differentiate supporting articles, and redirect/merge any page with no unique value after performance review. | 1 |
| `/canadian-bank-loan-business-plan-guide.html` and `/how-banks-evaluate-business-plans.html` | loan application education | lender requirements; evaluation; rejection reasons | Adjacent intent risks overlap with the financing hub and commercial bank-loan service. | Preserve distinct roles in headings/internal anchors; inspect Search Console query/page pairs before merging. | 1 |
| `/financial-feasibility-study-guide.html` | feasibility assessment | bankable feasibility study | Relevant guide exists but is not yet represented in the keyword map. | Add it to the educational hub and map; expand only from verified reader questions. | 2 |

## New pages recommended (not blindly implemented)

| Proposed URL | Primary keyword | Secondary cluster | Intent and purpose | Internal links | Conversion goal | Priority |
| --- | --- | --- | --- | --- | --- | --- |
| `/small-business-grants-canada.html` | small business grants Canada | government grants for small business; grants for small business | Informational national hub explaining grant fit, matching, eligibility, timing and evidence without promising funding. | Financing hub, Benefits Finder, business-plan services, projections | Qualified planning/grant-support enquiry | 1 |
| `/small-business-grants-ontario.html` | small business grants Ontario | Ontario business grants/funding | Provincial informational page only because programs and delivery bodies differ. | National grants hub, COJG guide if created, Toronto/Ontario services | Qualified Ontario enquiry | 2 |
| `/small-business-grants-bc.html` | small business grants BC | BC small business funding | Provincial guide after verifying sufficient distinct current programs. | National hub, Vancouver services, projections | Qualified BC enquiry | 3 |
| `/small-business-grants-alberta.html` | small business grants Alberta | Alberta small business funding | Provincial guide after verifying sufficient distinct current programs. | National hub, Calgary/Edmonton services | Qualified Alberta enquiry | 3 |
| `/what-is-ebitda.html` | what is EBITDA | EBITDA definition; what EBITDA stands for | Authoritative educational guide with formula, worked example, limitations and lender context. | Glossary, projections, due diligence, feasibility | Financial-modelling enquiry | 2 |
| `/what-is-an-sme.html` | SME meaning | what is an SME; SMEs | Canadian definition guide explaining context-dependent thresholds. | Glossary, financing, services | Continue to relevant planning resource | 2 |
| `/request-for-proposal-guide.html` | what is an RFP | request for proposal; RFP process | Educational procurement guide; create only if commercially relevant services can credibly support it. | Learning hub, consulting/service page | Consulting enquiry | 3 |
| `/fractional-cfo-services.html` | fractional CFO services | fractional chief financial officer | Commercial page only if this is an actively delivered service with evidence, scope and ownership. | Financial modelling, strategic planning, due diligence | Consultation | 2 |

CanExport, Strategic Innovation Fund and job-grant pages should wait for editorial capacity and a current-program verification workflow. A “Rapid Innovation Fund” page is not recommended until the exact Canadian program and durable search intent are validated.

## Cannibalization and intent boundaries

1. The five executive-summary articles are the clearest consolidation/differentiation candidate.
2. `/small-business-financing-canada.html` is the informational loan-selection hub; `/bank-loan-business-plans.html` is the commercial service page; program/lender guides answer program-specific preparation questions. Maintain those roles in titles and links.
3. `/sample-other-plan.html` now owns Canadian template/example intent. `/business-plan-essentials.html` remains the book/how-to page and `/business-plan-comparisons.html` remains comparison intent. Do not add a duplicate `/business-plan-template-canada/` page.
4. City pages share a service pattern and industry clusters share a taxonomy. They do not currently duplicate titles/H1s, but should be monitored for low impressions, doorway-like similarity and weak unique value.

## Technical SEO findings

### Healthy

- Canonical, title, description, single-H1 and structured-data coverage is complete across indexable pages.
- No duplicate titles/H1s, broken local links, orphan pages, missing alt text, redirect chains or oversized images were found by the repository audit.
- Open Graph URLs are consistent where present; schema JSON parses; sitemap and robots configuration agree with canonical URLs.
- Public pages are crawlable/indexable in source. Utility/repository paths and query variants are intentionally blocked or excluded.

### Opportunities and risks

- Open Graph is not enforced as mandatory by the audit, so coverage should be measured and completed page by page; `og:type` should match informational versus commercial content.
- The sitemap mixes bare URL entries and richer `lastmod/changefreq/priority` entries. Prefer trustworthy `lastmod` generated from meaningful content changes; omit decorative signals if they cannot be maintained.
- The very large global navigation/footer link footprint creates tens of thousands of repeated links. Keep user-critical navigation, but review whether every city must be linked sitewide.
- Static pages repeat shared header/footer markup. Generator scripts reduce drift, but every global change must be regenerated and audited.
- Claims about programs, loan terms, statistics and eligibility are time-sensitive. Continue visible review dates and primary-source verification.

## Priority roadmap

### Priority 1 — highest SEO and business value

1. Completed: assign Canadian template intent to the existing sample page rather than create a duplicate.
2. Completed: assign national loan variants to the existing financing hub and strengthen its cross-link to the template.
3. Create one current, evidence-led Canadian grants hub.
4. Resolve the executive-summary cluster using Search Console data and unique-intent review.
5. Validate the financing/service/loan-guide intent split with query-to-page performance data.

### Priority 2 — supporting authority

1. Publish selective EBITDA and SME guides; connect them to glossary and commercial finance pages.
2. Add Ontario grants only after the national hub and a maintainable program-review process exist.
3. Improve feasibility-study discovery and consider fractional CFO only if it is a real, staffed service.
4. Audit OG completeness and reduce excessive sitewide link repetition without harming navigation.

### Priority 3 — lower priority

1. Consider BC and Alberta grants after distinct provincial intent/content is demonstrated.
2. Consider RFP and additional government-program explainers only where expertise and conversion relevance are clear.
3. Do not prioritize navigational lender pages, US SBA content or one page per keyword variant.
