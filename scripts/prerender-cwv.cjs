// Start a static server on port 4173, then run node scripts/prerender-cwv.cjs.
// Refresh after changing schema breadcrumbs or the shipped generator UI.
// CHROMIUM_PATH may select a system browser; otherwise use Playwright's browser.
const { chromium } = require('playwright');
const fs = require('node:fs');
const pages = ['blog-learning-hub.html', 'daycare-business-plans.html',
  'medical-services-business-plans.html', 'mobile-app-business-plans.html',
  'business-plan-generator.html'];
const breadcrumb = /<nav class="site-breadcrumb"[\s\S]*?<\/nav>/g;

(async () => {
  const browser = await chromium.launch(process.env.CHROMIUM_PATH
    ? { executablePath: process.env.CHROMIUM_PATH } : {});
  try {
    for (const file of pages) {
      const page = await browser.newPage(); // no localStorage / saved user answers
      await page.route('https://**/*', route => route.abort());
      await page.route(`**/${file}`, async route => {
        const response = await route.fetch();
        // Let schema.js generate fresh markup instead of reusing the snapshot.
        await route.fulfill({ response, body: (await response.text()).replace(breadcrumb, '') });
      });
      await page.goto(`http://127.0.0.1:4173/${file}`);
      let html = fs.readFileSync(file, 'utf8');
      const nav = await page.locator('.site-breadcrumb').evaluateAll(nodes => nodes.map(n => n.outerHTML).join(''));
      if (nav) {
        html = html.replace(breadcrumb, '').replace(/<nav class="cluster-breadcrumb"[\s\S]*?<\/nav>/, '');
        html = html.replace(/(<\/nav>\s*<\/div>\s*<\/div>)/, '$1' + nav);
      }
      if (file === 'business-plan-generator.html') {
        await page.waitForFunction(() => !document.querySelector('#business-plan-generator-app').inert);
        const form = await page.locator('#business-plan-generator-app').innerHTML();
        html = html.replace(/(<div id="business-plan-generator-app" inert>)[\s\S]*?(<\/div><noscript>)/, '$1' + form + '$2');
      }
      fs.writeFileSync(file, html);
      await page.close();
    }
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exitCode = 1; });
