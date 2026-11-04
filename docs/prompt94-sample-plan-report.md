# Prompt 94 — Sample library expansion, batch 1

The starting library contains **31 entries**, not 21. Existing coverage: restaurant; coffee shop; food truck; bakery; painting company; welding company; construction; trucking company; car dealership; clothing line; pet store; consulting firm; interior design; esthetician; marketing agency; daycare; gym; hair salon; landscaping; cleaning company; auto repair shop; e-commerce; construction company; dental clinic; pharmacy; liquor store; pet grooming; laundromat; brewery; event venue; real estate brokerage.

All four requested industry samples already exist. Apply the first four uncovered reserves in order:

| Requested | Created instead | Reason |
| --- | --- | --- |
| Restaurant | Logistics franchise | Existing restaurant sample; parcel-dispatch franchise differs from trucking |
| Food truck | Food manufacturing | Existing food-truck sample; packaged sauce production differs from bakery/brewery |
| Hair salon / barbershop | Home-care services | Existing hair-salon sample; non-clinical private-pay support differs from cleaning |
| Cleaning services | Import/export trading | Existing cleaning-company sample; B2B tableware trading differs from e-commerce |

The priority SBA sample uses a fictional Austin bicycle retailer and repair workshop, avoiding the existing coffee-shop industry. The fifth reserve, brewery/taproom, is already covered and was not needed.

## Created pages and wiring

| Page URL | Library placement | Existing inbound linking pages |
| --- | --- | --- |
| `/blog-sample-us-sba-loan-business-plan.html` | Ungrouped card before Food & Hospitality; position 32 | `/sba-business-plan.html`; `/us-business-plans.html` (intro, explanatory copy and resource card) |
| `/blog-sample-logistics-franchise-business-plan.html` | End of Trades & Services; position 33 | `/logistics-franchises.html`, after unit economics |
| `/blog-sample-food-manufacturing-business-plan.html` | End of Food & Hospitality; position 34 | `/manufacturing-business-plans.html`, after opening operating-model discussion |
| `/blog-sample-home-care-services-business-plan.html` | End of Professional & Care; position 35 | `/medical-services-business-plans.html`, near the existing related-operation example |
| `/blog-sample-import-export-trading-business-plan.html` | End of Retail; position 36 | `/export-development-canada.html`, following the official-site link |

Each page links back to the library and its related planning guide and includes a matching PDF under `/downloads/`. The US hub now identifies the SBA sample as US-context/USD while preserving the Canadian context of the other linked samples. Its resource ItemList has 12 entries matching the visible cards. Five new sitemap entries use the generator's output; unrelated legacy entries are preserved.

## Template and content

Studied the brewery and cleaning-company factory samples and the food-truck sample. Copied the brewery factory page shell, section order, styles, disclaimers, annotation, CTA, author and sidebar conventions. Each new page has approximately 4,500–4,800 words, ten numbered sections, five FAQs, sources-and-uses, revenue drivers, three-year income/cash-flow/balance-sheet tables, downside and repayment calculations, an appendix and an 11-page PDF.

The SBA sample covers the guide's nine traditional components within the library's ten-section order, which adds a separate operations section. It explains the three-year teaching scope versus the longer outlook and first-year detail the lender may request. All business details, owner biographies, franchise terms and commercial figures are fictional. Official links are research starting points; no regulatory checking date, current fee, statutory rate, eligibility finding or approval is invented. Existing site author/service components are reused without new claims about The Biz Plans.

## Validation

- Independently parsed the displayed HTML tables with decimal arithmetic: unit/price revenue, direct-cost channel formulas, income, cash roll-forwards, assets = liabilities + equity, retained earnings and inter-year cash reconcile for all 15 modeled years.
- Confirmed 36 unique library positions, all five library cards and sitemap entries, working section anchors, a unique title/meta description and one H1 per page.
- Local Chromium checks at 1440px and 390px: no document overflow; financial tables scroll within their wrappers. Reviewed desktop and mobile screenshots.
- Parsed live JSON-LD after shared schema execution: no ratings or review fields. FAQ schema matches visible questions and answers.
- Generated five PDFs using the existing print styles. Text extraction confirms all ten sections, company identity and FAQs; all PDFs have 11 pages.
- `git diff --check` passes. Existing sample pages, design components, listings, pricing/quote forms and generator files are unchanged.
- `python scripts/audit_site.py` and `python scripts/generate_seo.py --check` fail on the unchanged starting commit too. Baseline includes legacy redirect canonical/SEO disagreements, retired external links, eager-logo findings and shared header/footer variant findings. New samples inherit the exact template's eager header-logo finding; no new broken link, missing heading, duplicate metadata, schema or orphan issue is introduced. The generator also rewrites unrelated legacy canonicals and sitemap dates, so only the five new generated sitemap entries are retained for this scoped PR.
