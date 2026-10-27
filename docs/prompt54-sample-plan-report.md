# Prompt 54 — 15 Canadian sample business plans

Created in `/workspace/TheBizPlans_Website` on October 26, 2026 (America/Toronto). These are repository deliverables, not a production deployment. The URLs below are the pages’ configured canonical URLs; availability on the live domain was not claimed or tested.

All 15 plans were created in queue order. Each has its own HTML page, downloadable full-sample PDF and separate entry below. The established `blog-sample-…-business-plan.html` convention replaces the requested `sample-…-business-plan.html` paths. No duplicate short-path pages or redirects were created.

## Template and shared implementation

No standalone master-template file was found. The existing daycare sample and documented painting-series structure supplied the template: shared navigation, hero, breadcrumb, two-column article/sidebar, numbered ten-section plan, annotation blocks, responsive financial tables, funding CTA, source appendix, five FAQs, existing author card, footer and print styling. Sections are executive summary; company overview; services and revenue model; market analysis; operations; marketing; management; financial projections; funding request; appendix. Each fictional business is explicitly labelled SAMPLE. Financial figures and commercial assumptions are explicitly illustrative.

Every plan links to the existing sample hub, generator, services, CSBFP hub and TAM/SAM/SOM glossary. All internal link targets and fragments in the new pages were checked against the checkout, including the generated PDFs. The hub now contains 31 cards, up from 16, preserving all existing entries. The 15 new cards follow the queue order in a new industry-library section, and all ItemList positions were renumbered consecutively. The sitemap retains all existing URLs and adds each canonical once in alphabetical order with commit-derived 2026-10-27 dates (Git metadata; research and page publication remain October 26 in America/Toronto).

## Official-source verification

Official-source research was performed at build time. Ontario pages returned 403 on direct retrieval; current indexed excerpts on the named official pages supplied the limited claims used. The report and pages do not imply full-page legal review. Current canonical Ontario legislation URLs are linked rather than historical version URLs. Unverified fees, thresholds, timelines and sector details are omitted or treated qualitatively, as itemized per plan. A direct AGCO overview URL did not resolve; Ontario’s current retail overview and consolidated licensing regulation supplied the liquor framework, with AGCO’s published retail licence list identifying regulator categories. No failed overview URL was published.

The liquor sample is a proposed licensed convenience-market format, with actual non-alcohol merchandise and no spirits revenue or assumed right to an LCBO arrangement. It does not present Ontario as permitting a generic new private spirits store. The brewery uses qualitative provincial/federal licence framing, with no obsolete retail permission or excise rate asserted. The pet business uses Vaughan’s published licensing framework rather than applying another municipality’s requirements.

## Validation

- All 15 pages: one H1, ten numbered sections, five visible FAQs with matching FAQPage content, parseable Article + FAQPage + Person JSON-LD, unique IDs and valid table-of-contents targets.
- Every title is at most 60 characters; every meta description is 140–160 characters. All article word counts exceed 2,500. Counts below exclude financial tables, table of contents, print-only title, author card, sidebar, navigation and footer; FAQs and substantive annotations are included.
- All 45 financial years independently reconciled from rendered tables: revenue, direct costs, EBITDA, net income, working-capital cash movement, principal, closing cash, assets, liabilities and retained earnings. The selected cases have nonnegative closing annual cash; no monthly liquidity or operating-result guarantee is implied. The brewery equity assumption was increased after a cash shortfall was detected.
- All 15 pages and the hub checked in local Chromium at desktop 1440px and mobile 390px, with no horizontal page overflow or JavaScript page errors. External CDNs were blocked for deterministic local checks. Shared navbar behaviour requiring external Bootstrap JavaScript was not tested. Existing local site styles and schema scripts loaded.
- All 15 PDFs exported from final page content, with selectable text, ten sections, five financial tables, appendix and FAQs. Each is ten pages, with SAMPLE/illustrative page footers and portable production-domain document links. Representative first and financial-table pages were visually inspected.
- `git diff --check` passed. New pages have no broken local links, missing fragments, placeholder tokens or invented keyword-volume claims.
- The repository-wide audit is not clean: existing findings include a missing financial workbook on the free-template page, retired external links on the startup-visa page, and shared header/footer variants. The new pages inherit the template’s eager header logo, which the audit flags as not lazy-loaded. No new broken-link or JSON-LD finding remains.
- After committing the new pages, the sitemap was regenerated from Git modification dates. `generate_seo.py --check` passes. Sitemap URL membership, uniqueness and ordering were also checked independently. Deployment was not performed.

## 1. Gym

- **URL:** [https://thebizplans.com/blog-sample-gym-business-plan.html](https://thebizplans.com/blog-sample-gym-business-plan.html)
- **Requested-path remap:** `/sample-gym-business-plan.html` → `/blog-sample-gym-business-plan.html`.
- **Fictional SAMPLE:** Cedar Arc Fitness Inc., Whitby, Ontario.
- **Words excluding tables:** 3,618. Title: 33 characters. Meta: 143 characters.
- **Official sources used:** [Ontario — Joining a gym or fitness club](https://www.ontario.ca/page/joining-gym-or-fitness-club); [City of Toronto — Business Regulations, Licences & Permits](https://www.toronto.ca/business-economy/new-businesses-startups/business-regulations/).
- **Figures/requirements omitted or left qualitative:** Licence fees, presale trust mechanics and cancellation exceptions beyond the verified Ontario summary are omitted; counsel must determine the applicable details.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/gym-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 2. Hair salon

- **URL:** [https://thebizplans.com/blog-sample-hair-salon-business-plan.html](https://thebizplans.com/blog-sample-hair-salon-business-plan.html)
- **Requested-path remap:** `/sample-hair-salon-business-plan.html` → `/blog-sample-hair-salon-business-plan.html`.
- **Fictional SAMPLE:** Copper Finch Hair Studio Inc., Toronto, Ontario.
- **Words excluding tables:** 3,595. Title: 40 characters. Meta: 150 characters.
- **Official sources used:** [City of Toronto — Personal service settings licensing](https://www.toronto.ca/services-payments/permits-licences-bylaws/body-piercing-electrolysis-hair-salon-nail-shop-tattoo-and-waxing/); [Ontario — O. Reg. 136/18, Personal Service Settings](https://www.ontario.ca/laws/regulation/180136).
- **Figures/requirements omitted or left qualitative:** Municipal fees, notice-period numbers and trade-qualification details are not quoted; the actual licence and staffing arrangement require confirmation.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/hair-salon-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 3. Landscaping

- **URL:** [https://thebizplans.com/blog-sample-landscaping-business-plan.html](https://thebizplans.com/blog-sample-landscaping-business-plan.html)
- **Requested-path remap:** `/sample-landscaping-business-plan.html` → `/blog-sample-landscaping-business-plan.html`.
- **Fictional SAMPLE:** Juniper Route Grounds Inc., Oshawa, Ontario.
- **Words excluding tables:** 3,594. Title: 41 characters. Meta: 151 characters.
- **Official sources used:** [WSIB — Register with us](https://www.wsib.ca/en/businesses/registration-and-coverage/register-us); [WSIB — Questions and answers: Clearances](https://www.wsib.ca/en/clearancefaqs).
- **Figures/requirements omitted or left qualitative:** WSIB premium rates, snow-depth triggers described as law, pesticide entitlements and universal clearance exemptions are omitted; snow triggers are negotiated commercial terms.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/landscaping-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 4. Cleaning company

- **URL:** [https://thebizplans.com/blog-sample-cleaning-company-business-plan.html](https://thebizplans.com/blog-sample-cleaning-company-business-plan.html)
- **Requested-path remap:** `/sample-cleaning-company-business-plan.html` → `/blog-sample-cleaning-company-business-plan.html`.
- **Fictional SAMPLE:** Clear Alder Contract Cleaning Inc., Mississauga, Ontario.
- **Words excluding tables:** 3,599. Title: 46 characters. Meta: 156 characters.
- **Official sources used:** [WSIB — Register with us](https://www.wsib.ca/en/businesses/registration-and-coverage/register-us); [City of Toronto — Business Regulations, Licences & Permits](https://www.toronto.ca/business-economy/new-businesses-startups/business-regulations/).
- **Figures/requirements omitted or left qualitative:** No mandatory bond amount, insurance minimum or WSIB premium rate is asserted; bonded/insured wording is conditional on actual cover.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/cleaning-company-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 5. Auto repair shop

- **URL:** [https://thebizplans.com/blog-sample-auto-repair-shop-business-plan.html](https://thebizplans.com/blog-sample-auto-repair-shop-business-plan.html)
- **Requested-path remap:** `/sample-auto-repair-shop-business-plan.html` → `/blog-sample-auto-repair-shop-business-plan.html`.
- **Fictional SAMPLE:** Iron Maple Auto Service Inc., Toronto, Ontario.
- **Words excluding tables:** 3,592. Title: 46 characters. Meta: 156 characters.
- **Official sources used:** [Skilled Trades Ontario — Automotive Service Technician](https://www.skilledtradesontario.ca/trade-information/automotive-service-technician/); [City of Toronto — Business Regulations, Licences & Permits](https://www.toronto.ca/business-economy/new-businesses-startups/business-regulations/).
- **Figures/requirements omitted or left qualitative:** Trade-training hour counts, municipal repair-garage fees, environmental thresholds and certification claims for unrelated repair activities are omitted.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/auto-repair-shop-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 6. E-commerce

- **URL:** [https://thebizplans.com/blog-sample-ecommerce-business-plan.html](https://thebizplans.com/blog-sample-ecommerce-business-plan.html)
- **Requested-path remap:** `/sample-ecommerce-business-plan.html` → `/blog-sample-ecommerce-business-plan.html`.
- **Fictional SAMPLE:** Birch Parcel Home Goods Inc., Kitchener, Ontario.
- **Words excluding tables:** 3,520. Title: 40 characters. Meta: 150 characters.
- **Official sources used:** [Canada Revenue Agency — GST/HST on imports and exports](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-imports-exports.html).
- **Figures/requirements omitted or left qualitative:** GST/HST numeric registration thresholds, United States sales-tax thresholds, duty/de minimis figures and guaranteed export zero-rating are omitted.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/ecommerce-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 7. Construction company

- **URL:** [https://thebizplans.com/blog-sample-construction-company-business-plan.html](https://thebizplans.com/blog-sample-construction-company-business-plan.html)
- **Requested-path remap:** `/sample-construction-company-business-plan.html` → `/blog-sample-construction-company-business-plan.html`.
- **Fictional SAMPLE:** Stone Elm General Contracting Inc., Hamilton, Ontario.
- **Words excluding tables:** 3,623. Title: 50 characters. Meta: 160 characters.
- **Official sources used:** [Ontario — Construction Act, section 22](https://www.ontario.ca/laws/statute/90c30); [WSIB — Questions and answers: Clearances](https://www.wsib.ca/en/clearancefaqs).
- **Figures/requirements omitted or left qualitative:** Bond limits, surety premiums, universal lien deadlines and automatic holdback-release dates are omitted. The existing blog-sample-construction-business-plan.html is retained as a separate older example.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/construction-company-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 8. Dental clinic

- **URL:** [https://thebizplans.com/blog-sample-dental-clinic-business-plan.html](https://thebizplans.com/blog-sample-dental-clinic-business-plan.html)
- **Requested-path remap:** `/sample-dental-clinic-business-plan.html` → `/blog-sample-dental-clinic-business-plan.html`.
- **Fictional SAMPLE:** Willow Compass Dental Professional Corporation, Burlington, Ontario.
- **Words excluding tables:** 3,608. Title: 43 characters. Meta: 153 characters.
- **Official sources used:** [RCDSO — Become a dentist](https://www.rcdso.org/en-ca/become-a-dentist); [RCDSO — Health Profession Corporations](https://www.rcdso.org/en-ca/permits-and-renewals/health-profession-corporations); [RCDSO — Infection Prevention and Control](https://www.rcdso.org/standards-guidelines-resources/standards-guidelines-advisories/infection-prevention-and-control).
- **Figures/requirements omitted or left qualitative:** Professional fees, imaging approval details, clinical staffing ratios and dental reimbursement rates are omitted.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/dental-clinic-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 9. Pharmacy

- **URL:** [https://thebizplans.com/blog-sample-pharmacy-business-plan.html](https://thebizplans.com/blog-sample-pharmacy-business-plan.html)
- **Requested-path remap:** `/sample-pharmacy-business-plan.html` → `/blog-sample-pharmacy-business-plan.html`.
- **Fictional SAMPLE:** North Lantern Community Pharmacy Inc., London, Ontario.
- **Words excluding tables:** 3,556. Title: 38 characters. Meta: 148 characters.
- **Official sources used:** [Ontario College of Pharmacists — Opening a Community Pharmacy](https://ocpinfo.com/pharmacies/opening-a-community-pharmacy/); [Ontario College of Pharmacists — Community Pharmacy Assessments](https://ocpinfo.com/pharmacies/operating-a-community-pharmacy/community-pharmacy-assessments/).
- **Figures/requirements omitted or left qualitative:** Dispensing fees, reimbursement rates, accreditation fees and promised assessment durations are omitted.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/pharmacy-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 10. Liquor store

- **URL:** [https://thebizplans.com/blog-sample-liquor-store-business-plan.html](https://thebizplans.com/blog-sample-liquor-store-business-plan.html)
- **Requested-path remap:** `/sample-liquor-store-business-plan.html` → `/blog-sample-liquor-store-business-plan.html`.
- **Fictional SAMPLE:** Harbour Cedar Convenience Market Inc., Kingston, Ontario.
- **Words excluding tables:** 3,686. Title: 42 characters. Meta: 152 characters.
- **Official sources used:** [Ontario — Where to buy alcoholic beverages](https://www.ontario.ca/page/where-buy-alcoholic-beverages); [Ontario — O. Reg. 746/21, Licensing](https://www.ontario.ca/laws/regulation/210746); [AGCO — List of Convenience and Grocery Store Retail Licences](https://www.agco.ca/en/alcohol/list-convenience-and-grocery-store-retail-licences).
- **Figures/requirements omitted or left qualitative:** Licence fees, store-size and assortment thresholds, alcohol-strength limits, permitted hours, rollout dates, delivery entitlements and any right to sell spirits are omitted.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/liquor-store-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 11. Pet grooming

- **URL:** [https://thebizplans.com/blog-sample-pet-grooming-business-plan.html](https://thebizplans.com/blog-sample-pet-grooming-business-plan.html)
- **Requested-path remap:** `/sample-pet-grooming-business-plan.html` → `/blog-sample-pet-grooming-business-plan.html`.
- **Fictional SAMPLE:** Pine Paw Grooming and Boarding Inc., Vaughan, Ontario.
- **Words excluding tables:** 3,558. Title: 42 characters. Meta: 152 characters.
- **Official sources used:** [City of Vaughan — Pet Shop, Pet Grooming, Kennel and Boarding Facility permit](https://www.vaughan.ca/business/business-licensing-and-permits/pet-shop-pet-grooming-kennel-and-boarding-facility-permit).
- **Figures/requirements omitted or left qualitative:** Kennel fees, statutory animal capacity, staffing ratios, vaccination mandates and Ontario-wide licence claims are omitted; operator intake policies need veterinary and municipal review.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/pet-grooming-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 12. Laundromat

- **URL:** [https://thebizplans.com/blog-sample-laundromat-business-plan.html](https://thebizplans.com/blog-sample-laundromat-business-plan.html)
- **Requested-path remap:** `/sample-laundromat-business-plan.html` → `/blog-sample-laundromat-business-plan.html`.
- **Fictional SAMPLE:** Blue Elm Laundry Inc., Toronto, Ontario.
- **Words excluding tables:** 3,524. Title: 40 characters. Meta: 150 characters.
- **Official sources used:** [City of Toronto — Business Regulations, Licences & Permits](https://www.toronto.ca/business-economy/new-businesses-startups/business-regulations/).
- **Figures/requirements omitted or left qualitative:** Water, sewer, gas and electricity tariffs, mandatory staffing claims and municipal machine-capacity limits are omitted pending site-specific confirmation.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/laundromat-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 13. Brewery

- **URL:** [https://thebizplans.com/blog-sample-brewery-business-plan.html](https://thebizplans.com/blog-sample-brewery-business-plan.html)
- **Requested-path remap:** `/sample-brewery-business-plan.html` → `/blog-sample-brewery-business-plan.html`.
- **Fictional SAMPLE:** Granite Finch Brewing Inc., Guelph, Ontario.
- **Words excluding tables:** 3,611. Title: 37 characters. Meta: 147 characters.
- **Official sources used:** [Ontario — O. Reg. 746/21, Licensing](https://www.ontario.ca/laws/regulation/210746); [Canada Revenue Agency — ED200-1, Licensing requirements for manufacturers of beer](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/excise-duty/excise-duty-circulars/ed200-1-licensing-requirements-manufacturers-beer-malt-liquor-wort-yeast-malt-products.html).
- **Figures/requirements omitted or left qualitative:** Excise duty rates, small-brewer thresholds, provincial beer-tax rates, mandatory production volumes and obsolete by-the-glass licence descriptions are omitted.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/brewery-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 14. Event venue

- **URL:** [https://thebizplans.com/blog-sample-event-venue-business-plan.html](https://thebizplans.com/blog-sample-event-venue-business-plan.html)
- **Requested-path remap:** `/sample-event-venue-business-plan.html` → `/blog-sample-event-venue-business-plan.html`.
- **Fictional SAMPLE:** Meadow Lantern Events Inc., Toronto, Ontario.
- **Words excluding tables:** 3,637. Title: 41 characters. Meta: 151 characters.
- **Official sources used:** [Ontario — O. Reg. 746/21, Licensing](https://www.ontario.ca/laws/regulation/210746); [City of Toronto — Business Regulations, Licences & Permits](https://www.toronto.ca/business-economy/new-businesses-startups/business-regulations/).
- **Figures/requirements omitted or left qualitative:** Occupancy limits, liquor-service hours, caterer notice-period figures and statutory cancellation percentages are omitted; deposit dates and percentages are explicitly fictional operator proposals.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/event-venue-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## 15. Real estate brokerage

- **URL:** [https://thebizplans.com/blog-sample-real-estate-brokerage-business-plan.html](https://thebizplans.com/blog-sample-real-estate-brokerage-business-plan.html)
- **Requested-path remap:** `/sample-real-estate-brokerage-business-plan.html` → `/blog-sample-real-estate-brokerage-business-plan.html`.
- **Fictional SAMPLE:** Cedar Meridian Realty Inc., Toronto, Ontario.
- **Words excluding tables:** 3,599. Title: 51 characters. Meta: 154 characters.
- **Official sources used:** [RECO — Opening a brokerage or branch office](https://www.reco.on.ca/agents-and-brokerages/info-for-brokerages/opening-a-brokerage-or-branch-office/); [Ontario — Trust in Real Estate Services Act, 2002](https://www.ontario.ca/laws/statute/02r30).
- **Figures/requirements omitted or left qualitative:** Registration fees, statutory trust-deposit deadlines, standard commission rates, agent earnings and compulsory split percentages are omitted.
- **Hub/sitemap edits:** one new card in `sample-business-plans.html`, an upward hub link on this plan, one canonical sitemap entry dated 2026-10-27 from Git metadata.
- **PDF:** `downloads/real-estate-brokerage-business-plan-sample.pdf` (10 pages).
- **Checklist:** template structure followed; Canada angle addressed with sourced or qualitative regulatory treatment; financials labelled illustrative; Article/FAQPage/Person schema checked; hub card and upward link present; sitemap entry present; no placeholders; no invented keyword volume.

## Construction overlap

Queue item 7 was built as `blog-sample-construction-company-business-plan.html`, focused on general contracting, tenant improvements, project recognition, subcontracting, holdbacks and collections. The existing `blog-sample-construction-business-plan.html` and its hub card were preserved without modification. Both now remain in the inventory. No redirect, canonical consolidation or replacement was introduced; this follows Prompt 54’s explicit instruction to build item 7 despite the overlap.

## Queue summary

Plans created: **15 HTML pages and 15 complete PDFs**. Plans deferred: **0**. Hub cards added: **15**. Sitemap URLs added: **15**. No already-covered industry listed in Section A was rebuilt. All pre-existing sample pages remain unchanged. No individual keyword search volumes were invented or published, and the supplied competitor traffic figures were not repurposed as industry demand claims.

Changes are committed on `seo/prompt54-sample-plan-queue` for pull-request review. They have not been merged or deployed. A change archive was also assembled in the working directory for packaging. The configured chat output directory was unavailable in this cloud filesystem; the final chat report therefore supplies the requested inventory inline. The repository files rely on the existing site’s shared assets.
