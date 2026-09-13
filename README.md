# The Biz Plans website

## Embedded AI generator

The React source lives in `ai-generator/`, mounts into `business-plan-generator.html`, and builds to `ai-generator-dist/`. Build it from the repository root with:

```bash
npm run build
```

The production workflow builds the generator and uploads the static website directly to the existing S3 bucket. Vercel is not part of the production architecture. The workflow deliberately excludes React source, dependencies, tests, and other development-only files from S3 while publishing `ai-generator-dist/` with the website.

Never put private credentials in a `VITE_` variable because Vite exposes those values to browsers. Secret-backed AI operations must use a protected backend endpoint.

### Maintaining the generator

The canonical public generator is integrated in `ai-generator/`. Keep the guarded
`business-plan-generator-app` mount and the Vite output directory
`../ai-generator-dist` when updating it. Before publishing an update, run:

```bash
cd ai-generator
npm install
npm run type-check
npm test
npm run build
```

Then test `business-plan-generator.html` locally, including draft persistence,
financial calculations, PDF and workbook exports, refresh, mobile layouts, and
browser back/forward navigation. The generator is deliberately browser-only; do
not add private credentials to `VITE_` variables or introduce privileged browser
operations.
