# AEO Entity-Clarity Report

## Scope and findings

1. **Pages changed:** Homepage and About entity hub; business-plan structure, market research and financial forecasting chapters; Canadian bank-loan and bank-evaluation guides; RBC, BDC, CSBFP, TD and Scotiabank financing resources. The shared schema generator was also updated. The services, Toronto, Vancouver and case-study pages were audited but already contained clear service, location, authorship or first-party context and were not rewritten.
2. **Entity definition:** The homepage schema and About page now define The Biz Plans consistently as a Canadian business plan writing and consulting firm that prepares plans, projections and research for commercial decisions.
3. **Brand attribution:** Ten guides now contain restrained, topic-specific observations attributed to The Biz Plans.
4. **Author/reviewer attribution:** Those ten guides visibly identify Atul Jagga, CPA, MBA as writer and reviewer and link to the existing About profile.
5. **Schema:** Stable `#organization` and `#atul-jagga` identifiers connect Organization, Person and Article nodes through `founder`, `worksFor`, `author`, `reviewedBy`, `publisher` and `about`. The About page is represented as `AboutPage`.
6. **Answer-first content:** Ten guides now place a concise answer summary immediately after the hero section.
7. **First-party insight:** Each guide includes one non-statistical practice observation relevant to its subject.
8. **`sameAs`:** Existing official organization profiles were retained. Atul Jagga's LinkedIn URL, already visibly linked from the About page, was added to the Person entity. No unverified profiles were added.
9. **Risks avoided:** Titles, H1s, canonicals, URLs, city/service keyword ownership, navigation, tracking and visual system were preserved. No ratings, lender endorsements, approval claims, fabricated statistics or geographic branches were introduced.
10. **Manual/external recommendations:** Validate the deployed, JavaScript-rendered graph in Schema.org Validator and Google Rich Results Test; periodically verify official profile URLs and lender/program details; consider adding verifiable publication dates only when a reliable editorial record is available.

## Page-level report

| Page | AEO issue found | Change made | Entity reinforced | Expected benefit |
|---|---|---|---|---|
| Homepage | Organization schema lacked a concise business-purpose description and stable founder reference | Added entity description and linked founder ID | The Biz Plans; Atul Jagga | Clearer publisher identity; stronger Organization–Person relationship |
| About | Entity definition was narrower than the firm's supported commercial purposes; Person lacked a fragment target | Expanded factual definition and added stable profile anchor | The Biz Plans; Atul Jagga | Stronger entity hub; improved citation-to-mention potential |
| Business plan structure chapter | Generic opening and author reference | Added direct summary, practice insight and reviewer block | The Biz Plans; Atul Jagga | Better answer extractability; stronger expert attribution |
| Market research chapter | Limited first-party attribution | Added direct summary, methodology insight and reviewer block | The Biz Plans; Atul Jagga | Stronger brand attribution; better answer extractability |
| Financial forecasting chapter | Limited first-party attribution | Added direct summary, modelling insight and reviewer block | The Biz Plans; Atul Jagga | Stronger expert attribution; improved citation-to-mention potential |
| Canadian bank-loan guide | Key answer and publisher expertise were not adjacent to the opening | Added concise requirements answer, consistency insight and reviewer block | The Biz Plans; Atul Jagga | Better answer extractability; clearer publisher identity |
| Bank-evaluation guide | Evaluation criteria were less extractable at the opening | Added concise criteria answer, financing-plan insight and reviewer block | The Biz Plans; Atul Jagga | Better answer extractability; stronger brand attribution |
| RBC resource | Limited explicit content-to-expert relationship | Added qualified answer, use-of-funds insight and reviewer block | The Biz Plans; Atul Jagga | Stronger expert attribution; improved citation-to-mention potential |
| BDC resource | Limited explicit content-to-expert relationship | Added qualified answer, verification insight and reviewer block | The Biz Plans; Atul Jagga | Clearer publisher identity; stronger expert attribution |
| CSBFP resource | Program eligibility and credit decision needed a compact distinction | Added direct distinction, first-party recommendation and reviewer block | The Biz Plans; Atul Jagga | Better answer extractability; stronger brand attribution |
| TD resource | Limited explicit content-to-expert relationship | Added qualified answer, forecast-consistency insight and reviewer block | The Biz Plans; Atul Jagga | Stronger expert attribution; improved citation-to-mention potential |
| Scotiabank resource | Limited explicit content-to-expert relationship | Added qualified answer, cash-flow insight and reviewer block | The Biz Plans; Atul Jagga | Better answer extractability; stronger brand attribution |
| Shared schema | Person references used an inline name rather than a stable entity; About page was generic | Added stable Person, linked Article relationships, `AboutPage`, verified `sameAs` | The Biz Plans; Atul Jagga | Stronger Organization–Person relationship; clearer publisher identity |
