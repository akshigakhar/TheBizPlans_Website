# The Biz Plans website

## Embedded AI generator

The React source lives in `ai-generator/`, mounts into `business-plan-generator.html`, and builds to `ai-generator-dist/`. Build it from the repository root with:

```bash
npm run build
```

The production workflow builds the generator and uploads the static website directly to the existing S3 bucket. Vercel is not part of the production architecture. The workflow deliberately excludes React source, dependencies, tests, and other development-only files from S3 while publishing `ai-generator-dist/` with the website.

Never put private credentials in a `VITE_` variable because Vite exposes those values to browsers. Secret-backed AI operations must use a protected backend endpoint.

### Replacing the scaffold with the canonical AI application

1. Replace the contents of `ai-generator/` with the canonical `TheBizPlans_AI` source, excluding `node_modules`, `.git`, `.vercel`, build output, and all `.env` files.
2. Preserve the guarded `business-plan-generator-app` mount and the Vite output directory `../ai-generator-dist`.
3. Audit every `VITE_` variable and move private credentials or privileged operations behind an appropriate backend endpoint.
4. Run `cd ai-generator && npm install && npm run type-check && npm test && npm run build`.
5. Test `business-plan-generator.html` locally, including APIs, authentication, saving, export, refresh, mobile layouts, and browser back/forward.
6. Push the website branch and merge it to `main`; `.github/workflows/deploy-s3.yml` will build and publish the generator with the website.
7. Keep the old AI repository and Vercel deployment available until the S3-hosted production page is verified.
