# Commercial keyword SEO implementation report — August 2026

## Audit and inventory

The pre-edit audit covered the homepage, services hub, Toronto and Vancouver pages, all tracked HTML files, the sitemap, robots rules, Apache redirects, structured data and internal-link targets. The repository contains national service pages for bank loans, investors, immigration, strategic planning and financial modelling; lender and financing guides; immigration-program pages; industry clusters; educational articles and guides; and Canadian and US location pages.

Before this pass, the four target pages already had unique descriptions, self-referencing canonicals, one H1 each and useful intent-specific content. The homepage had `Organization` and visible-content-matched `FAQPage` data. The services page had visible-content-matched `FAQPage` data. Toronto and Vancouver had `Service` data with `areaServed` as a city, without invented branches or addresses. Those valid implementations were preserved.

## Target-page changes

| URL | Previous title | New title | Previous H1 | New H1 | Primary assignment |
| --- | --- | --- | --- | --- | --- |
| `/` | Professional Business Plan Writers in Canada \| The Biz Plans | Professional Business Plan Writer Canada \| The Biz Plans | Professional Business Plan Writers in Canada | Unchanged | business plan writer |
| `/services.html` | Business Plan Writing Services in Canada \| The Biz Plans | Business Plan Writing Services Canada \| The Biz Plans | Professional Business Plan Writing Services in Canada | Unchanged | business plan writing services |
| `/vancouver-business-plan-writers.html` | Vancouver Business Plan Writer \| Financing & BC Market Plans | Business Plan Writer Vancouver \| The Biz Plans | Business Plan Writing for Vancouver & the Lower Mainland | Vancouver Business Plan Writers | business plan writer Vancouver |
| `/toronto-business-plan-writers.html` | Toronto Business Plan Writer \| Financing & Investor Plans | Business Plan Writer Toronto \| The Biz Plans | Business Plan Writing for Toronto & the GTA | Toronto Business Plan Writers | business plan writer Toronto |

The homepage's first commercial H2 now focuses on writers for financing, investors and growth rather than trying to own the services phrase. Its proof section now directly answers why a client would work with a professional writer. The services-page opening now states concrete components and use cases, and its deliverables and audience headings make commercial service intent explicit. Vancouver and Toronto retain their distinct local-market evidence, funding resources, delivery disclosures and unique descriptions.

## Internal linking and cannibalization

The focused authority pass added 22 contextual body links from 21 closely related pages. It did not add footer, sidebar, boilerplate or site-wide links.

| Source URL | Existing context | Anchor text added | Target URL | Reason for link |
| --- | --- | --- | --- | --- |
| `/business-plan-essentials.html` | Founder biography in the core writing guide | The Biz Plans | `/` | Branded path from the primary writing resource. |
| `/chapter-1-structuring-your-business-plan.html` | Reader-first plan structure | professional business plan consultants | `/` | Connects the writing method to national consulting expertise. |
| `/business-plan-cost-timeline-checklist.html` | Comparing professional scope and cost | business plan writers in Canada | `/` | Helps readers identify the national provider behind the scoping guide. |
| `/industry-business-plans.html` | Research path across industry plan clusters | experienced business plan writers | `/` | Connects industry expertise to the national writer page. |
| `/financial-modeling.html` | Provider introduction on the modelling service | The Biz Plans | `/` | Adds a branded path from a core finance capability. |
| `/farm-credit-canada.html` | Agricultural plan preparation | professional planning team | `/` | Connects a specialist financing audience to national expertise. |
| `/chapter-3-market-research.html` | Evidence supporting strategy and forecasts | business plan writing services | `/services.html` | Links a core deliverable to the complete service scope. |
| `/chapter-7-financial-forecasting.html` | Integrating forecasts with narrative | planning and writing support | `/services.html` | Gives readers a natural next step after the forecasting guide. |
| `/how-banks-evaluate-business-plans.html` | Aligning the request, plan and forecast | help preparing a business plan | `/services.html` | Connects lender-readiness education to professional assistance. |
| `/canada-small-business-financing-program.html` | Connecting eligible costs and repayment | professional planning support | `/services.html` | Supports applicants who need an integrated financing case. |
| `/business-development-bank-of-canada.html` | Independent consulting and non-affiliation | business plan consulting services | `/services.html` | Clarifies the independent service while linking its scope. |
| `/royal-bank-of-canada.html` | Customized lender submission guidance | business plan preparation options | `/services.html` | Provides a service path without implying RBC affiliation. |
| `/td-canada-trust.html` | Broader bank-planning guidance | our business planning services | `/services.html` | Offers a customized engagement after informational guidance. |
| `/scotiabank.html` | Professional assistance for bank preparation | custom planning services | `/services.html` | Connects bank-focused preparation to the service hub. |
| `/investor-business-plan.html` | Investor-ready engagement scope | professional business plan services | `/services.html` | Consolidates overall service intent on the designated hub. |
| `/immigration-business-plans.html` | Separation of planning and representation | business plan writing support | `/services.html` | Helps readers choose the correct professional scope. |
| `/bcpnp-business-plan.html` | Non-immigration financing, acquisition or expansion | Vancouver business plan writer | `/vancouver-business-plan-writers.html` | Routes BC commercial intent outside the immigration stream. |
| `/immigration-business-plans.html` | BC program pathways | business plan services for Vancouver businesses | `/vancouver-business-plan-writers.html` | Separates Lower Mainland commercial work from immigration work. |
| `/victoria-business-plan-writers.html` | Choosing the correct BC market | Vancouver business planning support | `/vancouver-business-plan-writers.html` | Routes Lower Mainland users to the appropriate local page. |
| `/oinp-business-plan.html` | Non-immigration Ontario commercial planning | Toronto business plan writer | `/toronto-business-plan-writers.html` | Separates Toronto commercial intent from OINP intent. |
| `/mississauga-business-plan-writers.html` | Wider-GTA primary market | Toronto business planning support | `/toronto-business-plan-writers.html` | Routes Toronto-centred work to its preferred page. |
| `/brampton-business-plan-writers.html` | Projects centred elsewhere in the GTA | business plan guidance for Toronto businesses | `/toronto-business-plan-writers.html` | Clarifies local ownership without a generic city-site link. |

Totals: 6 new links to `/`, 10 to `/services.html`, 3 to Vancouver and 3 to Toronto. Of 22 anchors, 6 are exact or near-exact commercial phrases (27.3%), 11 are descriptive or partial-match phrases (50.0%), 3 are local descriptive phrases (13.6%), and 2 are branded anchors (9.1%).

The main cannibalization issue was semantic overlap between the homepage's early “Professional Business Plan Writing Services” H2 and the services page. The revised homepage keeps national provider intent while `/services.html` owns service/package intent. City titles and H1s now lead with their geographic writer topic. No synonym page or “near me” doorway was created; local discovery remains consolidated into legitimate city pages.

## Canonical, redirect and schema decisions

No canonical needed changing: `/` points to `https://thebizplans.com/`, and each internal target self-references its canonical `.html` URL. The sitemap already lists the root homepage and excludes `/index.html`. Apache's `.htaccess` already permanently redirects `index.html` to `/` and normalizes HTTPS/apex-host requests.

No schema changes were necessary. Existing schema matches visible services and does not claim Vancouver or Toronto branches. Adding more schema would not clarify the page ownership enough to justify duplicate entities.

The repository contains no CloudFront/S3 configuration. If production is served through CloudFront or S3 rather than Apache, the `/index.html` redirect and `www`-to-apex redirect must be implemented and tested at the viewer-request layer. That infrastructure change was not guessed in this static-site repository.

## Keyword map

| Keyword | Target URL | Optimization performed |
| --- | --- | --- |
| business plan writer | `/` | Singular phrase moved into the title; national writer H1 and commercial proof retained. |
| business plan services | `/services.html` | Concrete scope and audience language strengthened. |
| business plan writing services | `/services.html` | Exact service intent retained in title/H1 and strengthened in opening copy. |
| business plan consultants | `/` | National writer/consultant scope retained without a duplicate consultant page. |
| business plan writers near me | Toronto or Vancouver page, according to location | Supported by legitimate city relevance; no doorway page or artificial “near me” repetition. |
| business plan writer Vancouver | `/vancouver-business-plan-writers.html` | Exact title order and location-specific H1; BC/Lower Mainland content retained. |
| business plan experts | `/` | Consolidated into national professional-provider intent rather than a synonym page. |
| business plan writing service | `/services.html` | Singular phrase used naturally in the deliverables heading. |
| business plan consulting services | `/services.html` | Consulting section and service scope retained under the commercial hub. |

## Conservative recommendations not implemented

- No location pages were removed or mass-edited without Search Console query-to-page and conversion evidence.
- No fake office, reviews, ratings, lender relationships or LocalBusiness branches were added.
- No mass exact-match links, FAQ schema solely for keywords, hidden copy or synonym pages were added.
- No risky hosting redirect was added outside the existing Apache configuration; CloudFront behavior requires production-infrastructure access and validation.
