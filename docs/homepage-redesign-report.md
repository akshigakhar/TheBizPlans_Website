# Homepage Redesign Report

## 1. Previous homepage structure

The previous 52,408-byte homepage used a full-background hero, a large desktop mega-navigation, separate introductory and credentials sections, four image-led service cards, a five-step process, testimonials, eight image-led industry cards, pricing, books, a learning-hub promotion, six FAQs, related pages, a final CTA and an extensive city-heavy footer. Its 19 HTML images and Bootstrap, icon-font, Google Font and template dependencies added visual and transfer weight beyond the commercial purpose of the page.

## 2. New homepage structure

The new page follows a shorter commercial journey:

1. Text-first professional business plan writer hero
2. Compact trust and capability strip
3. Professional writing-services introduction
4. Four CSS-only core service cards
5. Founder credentials and consultant positioning
6. Canadian bank-financing resources
7. Free template and generator comparison
8. Compact industry and city text links
9. Static case study, testimonial and pricing links
10. Focused consultation CTA

Visible copy is intentionally concise rather than an article. It concentrates the offer, audience, deliverables and use cases near the start of the page.

## 3. Navigation before and after

**Before:** The homepage header exposed Home, Services, Financing, Immigration, Industries, Learn, Results and Pricing plus a consultation CTA. Desktop mega menus listed dozens of financing, immigration and industry destinations. Mobile used a separate flat list.

**After:** The logo is the Home link. The primary labels are Services, Financing, Industries, Free Tools, Learn, About and Book a Consult. Each disclosure contains only a small, curated set of links. Desktop and mobile use the same semantic navigation; CSS changes its presentation rather than maintaining duplicate menus. This repository is static and has no shared header include or build-time component, so the redesign is scoped to the homepage as requested; applying the new header to every deeper page should be a separate, regression-tested rollout.

## 4. Images removed and retained

- Removed the visual hero and its `hero-bizplans.png` preload.
- Removed all service, industry, pricing, book, blog and decorative content images from homepage markup.
- Retained the brand logo in the header as an eager, explicitly sized image.
- Retained one explicitly sized, lazy-loaded footer logo.
- Retained the existing hero asset only as social sharing metadata; it is not requested during a normal page render.
- Homepage markup image count decreased from **19 to 2**.

## 5. Performance optimizations

- Homepage HTML decreased from **52,408 bytes to 17,636 bytes** (66.4% smaller, measured before final report-only changes).
- External stylesheet/script elements decreased from **5 to 0**; GTM remains intentionally created after `load` and idle time, so analytics is preserved without making it parser-blocking.
- Google Font host references decreased from **4 to 0**. The homepage now uses a system font stack; this eliminates font downloads and avoids font-swap layout shifts without making a risky site-wide font migration.
- `script src` dependencies decreased from **3 to 2**, both small local scripts. Bootstrap, `main.min.js`, Font Awesome, Bootstrap Icons and Google Fonts are no longer loaded on the homepage.
- Owl Carousel, WOW, CounterUp, Waypoints and Easing are not loaded. No carousel or animation library replaced them.
- A text/CSS hero provides a stable LCP candidate. CSS cards, borders and typography replace stock photography.
- The only below-fold image is lazy-loaded with explicit dimensions and asynchronous decoding.

## 6. Commercial keyword targeting

The preserved title targets “Professional Business Plan Writer Canada.” The sole H1 is “Professional Business Plan Writers in Canada.” Within the opening copy, The Biz Plans is explicitly positioned as professional business plan writers and consultants serving Canada, preparing customized business plans, financial projections and supporting market research for bank financing, investors, acquisitions, startups and expansion. Secondary terms such as professional business plan writing, business plan consultants and business plan experts appear only where context supports them. `/services.html` remains the primary service-intent destination.

## 7. Internal-link architecture

The homepage directly links all requested commercial priorities: services, bank-loan plans, investor plans, strategic plans, financial modelling, free templates, the free generator, industries, the learning centre, credentials, case studies, pricing and contact. It also links selected RBC, TD, BDC, Scotiabank and CSBFP resources, ten industry pages and seven priority Canadian city pages.

Large inventories remain discoverable through the financing, industry and learning hubs and through `sitemap.xml`; they are no longer expanded in the primary navigation.

## 8. Footer changes

The previous wall of 36 city links was replaced with an organized seven-column footer: brand, Services, Financing, Resources, Locations, Company and Legal. It provides curated destinations plus “All Industries,” “Financing Centre,” and “All Pages & Locations” discovery paths. Social links are rendered as text, avoiding an icon-font request.

## 9. Mobile changes

Mobile uses the same information architecture and DOM as desktop. A small accessible menu button controls one scrollable navigation panel through `aria-controls` and `aria-expanded`. Native `details` disclosures support keyboard activation, only one submenu remains open at once, and Escape closes navigation and returns focus to the toggle. Cards, CTA buttons, footer groups and discovery columns collapse responsively without a second navigation tree.

## 10. SEO safeguards

- Canonical remains `https://thebizplans.com/`.
- The homepage URL and title are unchanged.
- Organization ID remains `https://thebizplans.com/#organization`.
- Founder Person ID remains `https://thebizplans.com/#atul-jagga`, including the relationship to the Organization.
- Existing address, social profiles, analytics/GTM ID and schema helper are preserved.
- No `noindex` directive, redirects, sitemap entries, files or URLs were changed.
- Social image metadata remains available even though the asset is no longer a visual homepage dependency.

## 11. Orphan-page audit

An automated local-link audit confirmed that every relative URL and image referenced by the redesigned homepage exists. The required priority pages are directly linked. Financing inventory remains reachable through `small-business-financing-canada.html`, industry inventory through `industry-business-plans.html`, educational inventory through `blog-learning-hub.html`, immigration content through the financing footer, and city inventory through selected contextual links plus `sitemap.xml`. The sitemap was not modified. No destination file was deleted, so the redesign does not create an orphan by removing a page from the site graph or sitemap.

## 12. Files modified

- `index.html` — rebuilt homepage, primary navigation and footer.
- `css/homepage.css` — isolated lightweight homepage layout, responsive design and focus styles.
- `js/homepage.js` — dependency-free accessible mobile and disclosure behaviour.
- `tests/homepage-seo.spec.js` — updated homepage SEO, navigation, priority-link and dependency assertions.
- `tests/homepage.smoke.spec.js` — updated render, menu and resource-loading assertions.
- `docs/homepage-redesign-report.md` — implementation and validation record.

## 13. Tests

Checks cover rendering at desktop, tablet and mobile widths; one H1; canonical, Organization and Person entity preservation; parseable JSON-LD; absence of `noindex`; unique IDs; required commercial links; menu accessibility state; local navigation and image targets; and the absence of former homepage dependencies. Static audits passed for 778 visible words, the single H1, canonical, unique IDs, JSON-LD parsing, all 13 priority links and all local targets. `git diff --check` also passed. Playwright could not run because its Chromium binary was absent and the browser CDN returned HTTP 403 when installation was attempted. Lighthouse is not installed in this project, so no Lighthouse scores are reported or inferred.

## 14. Manual review still required

- Validate analytics events in the production/tag-manager environment after deployment; production was not deployed by this task.
- Review dropdown behaviour in the final browser/device matrix, particularly touch devices and Safari.
- Capture visual-regression screenshots once a browser binary is available; the environment's Playwright browser download was blocked with HTTP 403.
- Confirm the retained social sharing image with Facebook, LinkedIn and X sharing debuggers.
- Consider rolling the simplified header to deeper static pages in a dedicated follow-up after full-site regression testing.
- Run production Lighthouse/WebPageTest against the deployed CDN response to include caching, compression, analytics and real network behaviour.
