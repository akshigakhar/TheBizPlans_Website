# TheBizPlanAI generator

This independently maintained Vite/React package mounts only into `#business-plan-generator-app`. It has no router, authentication, external API, Supabase, or Vercel dependency. Draft answers remain in browser `localStorage`; printing uses the browser's PDF support.

## Build

From the website root, run `npm run build:generator`, or run `npm install && npm run build` inside this directory. The production bundle is written to `../ai-generator-dist` with stable entry names for the static page.

Do not place secrets in `VITE_` variables: every such value is bundled publicly. This application currently requires no environment variables.
