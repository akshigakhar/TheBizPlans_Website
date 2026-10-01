# Technical SEO verification

Verified on 2026-10-01 against the deployable files in this repository.

## Pass/fail checklist

| Item | Result | Finding |
| --- | --- | --- |
| Canonical URLs | **PASS** | All 229 root HTML pages have exactly one absolute `https://thebizplans.com` canonical. The utility page was the only omission and now has one. |
| `www` redirect | **PASS (configuration)** | The host uses Apache-compatible `.htaccess` rules. One 301 rule normalizes every non-apex hostname (including `www`) and HTTP request to `https://thebizplans.com`, preserving the request URI. A live response check could not be completed because the verification environment's outbound proxy returned 403. |
| Sitemap | **PASS** | `sitemap.xml` contains all 228 indexable HTML pages, with one valid `lastmod` per URL. `robots.txt` references the sitemap. The sole noindex utility page is intentionally omitted, as required for sitemap/indexing consistency. |
| Blocked page | **PASS / intentional** | `whatsapp.html` is the only page carrying `noindex`. It is a query-driven WhatsApp redirect utility rather than search-result content, so the exclusion is intentional. It is not disallowed in `robots.txt`, allowing crawlers to see its `noindex, follow` directive. |
| HSTS | **PASS (configuration)** | Apache's `mod_headers` configuration sends `Strict-Transport-Security: max-age=31536000` on HTTPS responses. `includeSubDomains` is deliberately withheld until all subdomains are confirmed HTTPS-only. |
| Image alternative text | **PASS** | All 467 image elements across the 229 HTML pages have non-empty `alt` attributes. |
| Images over 200 KiB | **REVIEW** | 18 image assets exceed the compression-review threshold; see the inventory below. |

## Images over 200 KiB

The threshold is strictly greater than 204,800 bytes. Sizes are repository file sizes; MB values are MiB rounded to two decimals.

| File | Bytes | Approximate size |
| --- | ---: | ---: |
| `img/service-immigration.jpg` | 3,657,168 | 3.49 MB |
| `img/blog-learning-hub.jpg` | 3,231,912 | 3.08 MB |
| `img/why-bizplans.jpg` | 2,781,056 | 2.65 MB |
| `img/what-sets-us-apart.jpg` | 2,503,635 | 2.39 MB |
| `img/industry-fintech.jpg` | 2,251,126 | 2.15 MB |
| `img/industry-food-franchise.jpg` | 2,009,752 | 1.92 MB |
| `img/hero-bizplans.png` | 1,966,036 | 1.87 MB |
| `img/service-investor-lender.jpg` | 1,773,677 | 1.69 MB |
| `img/industry-marine.jpg` | 1,380,768 | 1.32 MB |
| `img/industry-medical.jpg` | 1,185,549 | 1.13 MB |
| `img/services-overview.jpg` | 1,138,064 | 1.09 MB |
| `img/industry-brewery.jpg` | 1,045,244 | 1.00 MB |
| `img/service-financial-modeling.jpg` | 932,333 | 0.89 MB |
| `img/industry-telecom.jpg` | 880,469 | 0.84 MB |
| `img/testimonials.jpg` | 747,357 | 0.71 MB |
| `img/service-marketing-strategy.jpg` | 633,281 | 0.60 MB |
| `img/industry-mobile-app.jpg` | 527,971 | 0.50 MB |
| `img/pricing.jpg` | 435,945 | 0.42 MB |
