
## AI business plan generator

The embedded React generator is maintained in `ai-generator/` and mounts within the existing static `business-plan-generator.html` page. Build its committed production assets with:

```bash
npm run build:generator
```

The S3 deployment publishes repository files without a Node build step, so `ai-generator-dist/` is intentionally committed. See `ai-generator/README.md` for architecture and security notes.
