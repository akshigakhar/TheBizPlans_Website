# Sample business plans hub — implementation report

Implemented in `/workspace/TheBizPlans_Website` on October 26, 2026.

**Hub source:** `sample-business-plans.html`  
**Canonical destination:** https://thebizplans.com/sample-business-plans.html  
**Status:** implemented and verified locally; not deployed. Production publishing runs through the existing GitHub Actions workflow on a push to `main`. No production credentials are configured in this environment; no commit, push or production deployment was performed. The destination URL above is not a claim that this new page is live.

## Complete sample inventory and cards

14 complete industry samples exist. All 14 are included as cards and each received a permanent related-section link back to the hub. No queued sample is represented as a card.

| Sample | Sector | Actual URL / page edited for backlink |
| --- | --- | --- |
| Restaurant | Food & Hospitality | [https://thebizplans.com/blog-sample-restaurant-business-plan.html](https://thebizplans.com/blog-sample-restaurant-business-plan.html) |
| Coffee shop | Food & Hospitality | [https://thebizplans.com/blog-sample-coffee-shop-business-plan.html](https://thebizplans.com/blog-sample-coffee-shop-business-plan.html) |
| Food truck | Food & Hospitality | [https://thebizplans.com/blog-sample-food-truck-business-plan.html](https://thebizplans.com/blog-sample-food-truck-business-plan.html) |
| Bakery | Food & Hospitality | [https://thebizplans.com/blog-sample-bakery-business-plan.html](https://thebizplans.com/blog-sample-bakery-business-plan.html) |
| Painting company | Trades & Services | [https://thebizplans.com/blog-sample-painting-company-business-plan.html](https://thebizplans.com/blog-sample-painting-company-business-plan.html) |
| Welding company | Trades & Services | [https://thebizplans.com/blog-sample-welding-company-business-plan.html](https://thebizplans.com/blog-sample-welding-company-business-plan.html) |
| Construction | Trades & Services | [https://thebizplans.com/blog-sample-construction-business-plan.html](https://thebizplans.com/blog-sample-construction-business-plan.html) |
| Car dealership | Retail | [https://thebizplans.com/blog-sample-car-dealership-business-plan.html](https://thebizplans.com/blog-sample-car-dealership-business-plan.html) |
| Clothing line | Retail | [https://thebizplans.com/blog-sample-clothing-line-business-plan.html](https://thebizplans.com/blog-sample-clothing-line-business-plan.html) |
| Pet store | Retail | [https://thebizplans.com/blog-sample-pet-store-business-plan.html](https://thebizplans.com/blog-sample-pet-store-business-plan.html) |
| Consulting firm | Professional & Care | [https://thebizplans.com/blog-sample-consulting-firm-business-plan.html](https://thebizplans.com/blog-sample-consulting-firm-business-plan.html) |
| Interior design | Professional & Care | [https://thebizplans.com/blog-sample-interior-design-business-plan.html](https://thebizplans.com/blog-sample-interior-design-business-plan.html) |
| Esthetician | Professional & Care | [https://thebizplans.com/blog-sample-esthetician-business-plan.html](https://thebizplans.com/blog-sample-esthetician-business-plan.html) |
| Marketing agency | Professional & Care | [https://thebizplans.com/blog-sample-marketing-agency-business-plan.html](https://thebizplans.com/blog-sample-marketing-agency-business-plan.html) |

An additional existing reference, https://thebizplans.com/sample-other-plan.html, contains an outline and illustrative excerpts rather than a complete industry plan. The hub links to it in the planning guidance, outside the industry cards and ItemList. It also received a link back to the new library. This produces an inventory of **14 industry samples plus one structural reference**.

The repo was inspected for sample filenames, sample content, industry pages, and the daycare/trucking story pages. `executive-summary-example.html` is a section example, not a complete sample plan. `blog-first-draft-daycare-plan.html` and `blog-buying-the-trucking-company.html` are educational stories, not completed industry samples.

## Named samples absent from the repository

The following are named or queued in the supplied prompt but have no completed sample-plan page:

| Queued / named sample | Existing material that does not qualify as a sample |
| --- | --- |
| Trucking — Prompt 44 | `trucking-business-plans.html`, industry tools, template PDF, acquisition story |
| Daycare — Prompt 45 | `daycare-business-plans.html`, industry tools, template PDF, founder story |
| Grocery | `grocery-business-plans.html` and related industry tools |
| HVAC | `hvac-business-plans.html` and related industry tools |
| Plumbing | `plumbing-business-plans.html` and related industry tools |

These queue labels come from the supplied request; this report does not assert their completion or a publication date. All other sample industries named in Section A exist. Construction, marketing agency and pet store were also found and included.

## Navigation and reciprocal links

- Inbound link: a prominent library feature block in `blog-learning-hub.html`, the existing Learning Centre linked from the shared main navigation. The request permits the closest existing hub as the inbound source.
- Backlinks: all 14 sample files listed above received a visible `Related sample plans` section immediately after their main content. These links survive the site's JavaScript breadcrumb replacement.
- The outline/excerpts page also links to the hub.
- Matching card-to-industry links: construction → `construction-business-plans.html`; car dealership → `dealership-business-plans.html`; marketing agency → `marketing-growth-strategy.html`.
- Construction and marketing service pages already linked to their samples. Added a sample link and hub link to `dealership-business-plans.html` to complete the reciprocal dealership path.
- Additional hub links include `business-plan-generator.html`, `business-plan-template.html`, `free-business-plan-template.html` (the general free-template asset guide), `services.html`, `canadian-business-plan-benchmarks-2026.html`, `about-business-plan.html` and `editorial-policy.html`.

## URL choices and remaps

Used `/sample-business-plans.html`, matching the existing Learning Centre and industry hub patterns. No directory URL, redirects, placeholder cards, invented destination slugs or remaps were introduced. Industry/service pages were not substituted for missing samples.

## Content, schema and maintainability

- Title: “Sample Business Plans — Free Examples by Industry” (49 characters).
- Meta description: 160 characters.
- Exact requested H1; primary keyword appears in the opening sentence.
- Introduction: 347 words. Browser text count excluding cards: 1,769 words, including explanatory guidance, FAQ, navigation and author text; explanatory guidance remains over 1,500 words after removing navigation and author text.
- Four qualifying sector groups with 4, 3, 3 and 4 cards respectively.
- Four-step use strip, financial reading guidance, adaptation guidance, onward routes and the missing-industry block.
- All card financial descriptors explicitly say “illustrative.” No traffic, ranking, popularity or download figures are asserted.
- Article, FAQPage (five questions) and Person use valid JSON-LD. Author identity matches the shared Atul Jagga entity.
- ItemList uses HTML microdata directly on the library and its 14 card blocks. Each card is a ListItem with its actual sample URL, name and unique position. This makes the schema list and visible cards the same source, eliminating a second URL list to update.
- Each sector has an `INSERT NEW SAMPLE CARDS HERE` comment. Add one complete card block with the next unique position, a real sample URL, illustrative financial descriptor and any matching industry link. Add a backlink on the new sample and regenerate the sitemap. Do not add a separate sector heading until at least two samples qualify.
- TOC links resolve to existing section IDs.

## Sitemap

Regenerated `sitemap.xml` with the existing `scripts/generate_seo.py`. It includes the new canonical URL and refreshes committed-date metadata according to the existing generator. Its existing fallback date is used for an uncommitted new page; regenerate after committing for the committed content date. Canonicals and robots remain consistent with the generator.

## Verification

Passed:

- `python scripts/generate_seo.py --check` — 260 indexable pages.
- `git diff --check`.
- Every internal hub link, referenced local asset and fragment target exists.
- All 14 rendered sample pages retain their hub backlink after the shared schema/breadcrumb script runs.
- Card URL and position inventory matches the ItemList exactly; Article/FAQPage/Person JSON parses successfully.
- Five visible FAQ questions and answers match their structured data.
- Desktop (1440px) and mobile (390px): no horizontal overflow; mobile menu opens; no page JavaScript errors.
- Reciprocal industry/service mappings, Learning Centre inbound link and sitemap entry verified.

The full `python scripts/audit_site.py` does **not** pass because of pre-existing findings. Compared against the unchanged repository, it reports the same missing workbook `downloads/free-financial-projections-template-3yr.xlsx` twice on `free-business-plan-template.html`, existing eager-logo/image findings and shared-header/footer variants. The new page inherits the shared header's eager logo, which adds the corresponding existing-style audit warning. No broken link or local asset was introduced by the hub. The template guide itself exists; its spreadsheet download needs separate repair.

## Deployment

The existing `.github/workflows/deploy-s3.yml` builds the embedded generator and syncs the static website to S3 when changes reach `main`. This change has not run that workflow. The working tree includes the new hub and all edited source files; use the existing release workflow to publish.
