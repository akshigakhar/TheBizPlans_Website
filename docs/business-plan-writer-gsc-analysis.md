# Business Plan Writer Search Console analysis

## Scope and evidence

This review is deliberately limited to the homepage, Toronto and Vancouver landing pages, directly relevant internal links, and hostname consolidation. The supplied 28-day Search Console filter shows that the apex homepage receives 1,059 impressions at position 20.56, Toronto receives 158 at 62.88, and Vancouver receives 140 at 13.79. The separate `www` homepage and Toronto rows are evidence that hostname consolidation is incomplete at the delivery layer.

## Ownership and diagnosis

### Generic Canadian intent

The homepage should own **business plan writer Canada**, **professional business plan writers**, **business plan writers**, and the broader Canadian professional-service intent. It already has the strongest combination of generic relevance and authority: the exact service category in the title and H1, Canada-wide positioning, financing/investor/immigration service summaries, founder credentials, process, testimonials, case studies, FAQs, conversion paths, and Organization schema. Its 1,059 filtered impressions confirm that Google already treats it as the cluster's principal page. The homepage was therefore clarified—not stuffed—with explicit national-versus-local scope and links to the two priority location pages.

`services.html` remains a service catalogue and conversion-support page, not the generic query owner. City pages should own only their geographic modifiers.

### Toronto

The supplied query averages (positions 16.32 and 16.38 for Toronto-modified queries) are much stronger than the Toronto URL's 62.88 page average. Search Console query and page aggregates do not prove a query-to-page pairing, but the discrepancy, the homepage's high generic visibility, Toronto address in Organization schema, and two-host duplication make the homepage (and possibly the `www` Toronto duplicate) the most plausible alternate URLs receiving some Toronto-query impressions. The query/page export should be filtered simultaneously by each Toronto query to confirm the exact URL.

The Toronto page was not thin in word count: it already contained GTA-specific trade areas, commuter patterns, occupancy/labour assumptions, sectors and funding sources. Its actual weakness was differentiation of commercial intent and trust. It shared its title/meta formula, heading formula, page structure, most service copy, FAQs and CTA with 35 generated city pages. It also described the method without identifying who leads the work. The revised page uses a Toronto/GTA service-focused title and H1, specifies lender/investor/acquisition intent, adds verified founder credentials and delivery disclosures, links to national credentials and the lender-plan service, and uses the project brief as its primary conversion action. It does not add a fake office claim.

### Vancouver

Vancouver's position 13.79 is the near-page-one opportunity. Its stronger performance is consistent with a more distinctive local entity/use-case combination: Lower Mainland scope, port/airport access, tourism seasonality, high occupancy and wage pressures, cross-border revenue, BC funding sources, and an existing topical relationship with the Vancity and BC program content. Search Console does not establish competitor-page factors, so no unsupported competitor claims are made.

The revised Vancouver page preserves that local evidence, aligns the title/H1 with a professional service search, adds financing/investor/acquisition intent, verified founder credentials (including the existing UBC connection), a clear remote-service/no-local-office disclosure, national and BC-specific supporting links, and a stronger assessment CTA. The Vancity guide now provides one contextual link back to Vancouver rather than adding mass exact-match anchors.

## Hostname audit

Repository-controlled signals consistently prefer `https://thebizplans.com/`:

- Canonicals and sitemap URLs use the apex HTTPS host.
- `robots.txt` declares the apex sitemap.
- homepage Open Graph, Organization schema and priority city Service schema use apex URLs.
- internal links are root-relative or relative and therefore inherit the requested host; no tracked content contains an intentional `www` canonical.
- `.htaccess` contains a 301 rule that sends non-HTTPS or non-apex requests to `https://thebizplans.com` in one hop and separately consolidates `/index.html`.

No CloudFront, S3, Terraform or other AWS distribution configuration exists in this repository. `.htaccess` is effective only when the origin/web server is Apache and CloudFront forwards the relevant request. Search Console's `www` impressions mean the live CloudFront/S3 path must be verified; repository tags alone cannot make a permanent redirect.

### Manual AWS/CloudFront action

1. Add `www.thebizplans.com` as an alternate domain on a distribution that has an ACM certificate covering that hostname.
2. Configure a CloudFront Function on the **viewer request** event for the `www` alias to return a `301` (or `308`) response whose `Location` is `https://thebizplans.com` plus the original URI and, only if intentionally retained, query string. Do not send the request to an S3 website error document.
3. Ensure HTTP also redirects directly to the apex HTTPS URL, avoiding an HTTP→HTTPS→apex chain.
4. Test `/`, `/toronto-business-plan-writers.html`, and an arbitrary deep URL on `www` with `curl -I`; each should return one permanent redirect and preserve the path.
5. Invalidate affected CloudFront objects, keep both DNS records active, and retain the `www` alias/certificate so crawlers can receive the redirect.

## Canadian city-page classification

The classifications reflect current content differentiation, not a direction to delete or redirect pages.

### A — strong unique landing pages

- **Toronto** — strong GTA/trade-area evidence plus newly differentiated service intent, accountable lead and supporting links.
- **Vancouver** — strong Lower Mainland/BC operating evidence, financing ecosystem relevance, accountable lead and topical supporting links.

### B — useful but needs further differentiation

- Montreal, Calgary, Edmonton, Ottawa, Winnipeg, Quebec City, Hamilton, Kitchener-Waterloo, Mississauga, Brampton, Vaughan, Markham, Richmond Hill, Oakville, Oshawa, Burlington, Pickering, Ajax, Whitby, Halifax, Regina, Saskatoon, St. John's and Victoria.
- These pages contain genuinely different local sectors, economics, geography and official resources, so they are useful. However, they retain the same layout, generic method paragraphs, FAQ pattern and conversion section. Before further promotion, each needs independently sourced local evidence, a distinct use-case emphasis, and contextual inbound links earned from closely related content.

### C — highly templated / future consolidation candidates

- No Canadian page is classified C solely because it shares a template: the current generated set includes unique local theses, modelling issues and program resources.
- Operationally, any B page that is not maintained, receives no location-specific demand, or loses accurate local evidence should be reclassified C during a future query/page and engagement review. That evidence—not city size alone—should control consolidation.

## Cannibalization controls

- Homepage: national professional-provider intent.
- Toronto: Toronto/GTA commercial intent.
- Vancouver: Vancouver/Lower Mainland/BC commercial intent.
- Financing, bank and immigration pages: their distinct decision/program intents, with city links used only when geography changes the analysis.
- Avoid sitewide exact-match additions. Existing footer city links support discovery but are not a reason to add more repeated anchors.
