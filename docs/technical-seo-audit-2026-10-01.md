# Technical SEO audit — 2026-10-01

## Crawl and indexing findings

- All 229 root HTML documents have one self-referencing canonical URL on the HTTPS apex domain.
- `sitemap.xml` contains all 229 HTML URLs and a `lastmod` value for each URL. `robots.txt` advertises the sitemap.
- No HTML document path is disallowed by `robots.txt`. The file intentionally blocks query-string duplicates and non-public repository/tooling paths.
- `whatsapp.html` is the single HTML document with a `noindex, follow` directive. This is intentional: it is a utility redirect to WhatsApp rather than a search landing page. It remains crawlable, has a canonical, and is listed in the complete HTML inventory in the sitemap.

## Hosting and transport controls

The repository contains two deploy/configuration mechanisms:

1. The `main` branch deployment workflow publishes static files to Amazon S3 and explicitly excludes `.htaccess`. S3 does not consume Apache configuration, so hostname redirects and response headers for that deployment must be attached at its external CDN/load-balancer layer (normally CloudFront); that infrastructure is not represented in this repository.
2. `vercel.json` configures the repository's Vercel build. It now issues a permanent `www.thebizplans.com` to `https://thebizplans.com` redirect and sends `Strict-Transport-Security: max-age=31536000` on all paths.

For an Apache deployment, `.htaccess` already redirects every non-apex host (including `www`) and HTTP request to the HTTPS apex in one 301 response. It also sends the same one-year HSTS policy over HTTPS. `includeSubDomains` is intentionally omitted until HTTPS support for every subdomain is confirmed.

The live response could not be independently inspected from the audit environment because its outbound proxy returned HTTP 403 before reaching the domain. The repository checks therefore pass, while a post-deployment `curl` check remains required for the S3/CDN production route.

## Image accessibility

Every HTML `<img>` element has non-empty alternative text; no markup changes were required.

## Images over 200 KiB

These source assets should be considered for resizing and/or WebP/AVIF recompression:

| File | Bytes | Approximate size |
| --- | ---: | ---: |
| `img/service-immigration.jpg` | 3,657,168 | 3571.5 KiB |
| `img/blog-learning-hub.jpg` | 3,231,912 | 3156.2 KiB |
| `img/why-bizplans.jpg` | 2,781,056 | 2715.9 KiB |
| `img/what-sets-us-apart.jpg` | 2,503,635 | 2445.0 KiB |
| `img/industry-fintech.jpg` | 2,251,126 | 2198.4 KiB |
| `img/industry-food-franchise.jpg` | 2,009,752 | 1962.6 KiB |
| `img/hero-bizplans.png` | 1,966,036 | 1920.0 KiB |
| `img/service-investor-lender.jpg` | 1,773,677 | 1732.1 KiB |
| `img/industry-marine.jpg` | 1,380,768 | 1348.4 KiB |
| `img/industry-medical.jpg` | 1,185,549 | 1157.8 KiB |
| `img/services-overview.jpg` | 1,138,064 | 1111.4 KiB |
| `img/industry-brewery.jpg` | 1,045,244 | 1020.7 KiB |
| `img/service-financial-modeling.jpg` | 932,333 | 910.5 KiB |
| `img/industry-telecom.jpg` | 880,469 | 859.8 KiB |
| `img/testimonials.jpg` | 747,357 | 729.8 KiB |
| `img/service-marketing-strategy.jpg` | 633,281 | 618.4 KiB |
| `img/industry-mobile-app.jpg` | 527,971 | 515.6 KiB |
| `img/pricing.jpg` | 435,945 | 425.7 KiB |

The threshold is 200 KiB (204,800 bytes).

## Checklist

- **PASS — Canonical URLs:** 229/229 HTML files use the non-`www`, HTTPS canonical origin.
- **PASS — Redirect configuration:** Apache and Vercel configurations enforce `www` to apex with a permanent redirect. The S3 production edge rule requires deployment-level verification.
- **PASS — Sitemap:** 229/229 HTML files are present, every entry has `lastmod`, and `robots.txt` references the sitemap.
- **PASS — Crawl block investigation:** no HTML path is disallowed; the sole `noindex` utility page is intentional.
- **PASS — HSTS configuration:** Apache and Vercel set a one-year HSTS policy. The S3 production edge header requires deployment-level verification.
- **PASS — Image alt text:** every HTML image has non-empty alt text.
- **PASS — Large-image inventory:** all 18 image assets over 200 KiB are listed above.
