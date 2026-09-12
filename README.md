# The Biz Plans website

## AI generator

The React source lives in `ai-generator/` and mounts into `business-plan-generator.html`. Run `npm run build:generator` from the repository root. The S3 workflow does not run Node, so commit the resulting `ai-generator-dist/` files before deploying. Vercel runs the root `npm run build` command and publishes the staged `site-dist/` directory.

Never put private credentials in a `VITE_` variable; Vite exposes those values to browsers. This implementation requires no environment variables or external API credentials.

### Owner deployment checklist

1. In a network-enabled checkout, replace the scaffold in `ai-generator/` with the canonical `TheBizPlans_AI` repository source (keep the guarded `business-plan-generator-app` mount and embedded Vite output settings).
2. Copy the AI repository's `.env.example` values into local/CI environment variables. Only use browser-safe public values; move secret-backed operations to a backend endpoint.
3. Run `cd ai-generator && npm install && npm run type-check && npm test && npm run build`.
4. Confirm `ai-generator-dist/generator.js` and `generator.css` changed, then test `business-plan-generator.html` locally at desktop and mobile widths.
5. Commit both `ai-generator/` and `ai-generator-dist/`, merge the PR to `main`, and let `.github/workflows/deploy-s3.yml` upload the static files.
6. Keep the existing AI repository and Vercel deployment available until production testing is complete.

### Vercel settings

Keep the project Root Directory blank (the repository root). `vercel.json` supplies `npm run build` as the Build Command and `site-dist` as the Output Directory. Do not override those fields in the Vercel dashboard. Redeploy after this commit reaches the configured production branch.

If Vercel reports `No Output Directory named "site-dist" found` immediately after a short Vite build, the project is using `ai-generator` as its Root Directory. In **Settings → Build and Deployment**, change Root Directory back to the repository root (`./`), select **Other** as the framework preset, and remove dashboard overrides for Build Command and Output Directory. Redeploy without the build cache. A correct log runs the root `thebizplans-website` build and ends with `Staged the static website in site-dist for Vercel.`
