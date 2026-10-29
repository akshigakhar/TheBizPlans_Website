const { test, expect } = require('@playwright/test');

// Isolate local layout work from third-party availability. Artificially delayed
// styles and scripts reproduce the old unstyled paint / late DOM insertion race.
for (const file of ['index.html', 'blog-learning-hub.html', 'daycare-business-plans.html',
  'medical-services-business-plans.html', 'mobile-app-business-plans.html', 'business-plan-generator.html']) {
  test(`${file} reserves layout before delayed enhancements`, async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.route('https://**/*', route => route.abort());
    await page.route(/^http:\/\/127\.0\.0\.1:4173\/(css\/.*|fonts\/.*|js\/schema.min.js|ai-generator-dist\/generator.js)$/, async route => {
      await new Promise(resolve => setTimeout(resolve, 700));
      await route.continue();
    });
    await page.addInitScript(() => {
      window.layoutShiftTotal = 0;
      new PerformanceObserver(list => {
        for (const entry of list.getEntries()) {
          if (!entry.hadRecentInput) window.layoutShiftTotal += entry.value;
        }
      }).observe({ type: 'layout-shift', buffered: true });
    });
    await page.goto(`/${file}`);
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(1000);
    expect(await page.evaluate(() => window.layoutShiftTotal)).toBeLessThan(0.1);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    if (file !== 'index.html' && file !== 'business-plan-generator.html') {
      await expect(page.locator('.site-breadcrumb')).toHaveCount(1);
    }
    if (file === 'business-plan-generator.html') {
      await expect(page.getByLabel('Business name')).toBeVisible();
    }
  });
}

test('analytics waits for load and keeps queued events', async ({ page }) => {
  await page.route('https://**/*', route => route.abort());
  await page.route('**/analytics-fixture.html', route => route.fulfill({ contentType: 'text/html', body: '<!doctype html><html><head></head><body></body></html>' }));
  await page.goto('/analytics-fixture.html');
  await page.evaluate(async () => {
    window.dataLayer = [{ event: 'contact_test' }];
    // Exercise the loader while load is still pending, independent of idle timing.
    Object.defineProperty(document, 'readyState', { configurable: true, get: () => 'loading' });
    await new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = '/js/analytics.js'; script.onload = resolve; script.onerror = reject;
      document.head.appendChild(script);
    });
  });
  await expect(page.locator('script[src*="gtm.js?id="]')).toHaveCount(0);
  await page.evaluate(() => window.dispatchEvent(new Event('load')));
  await expect(page.locator('script[src*="gtm.js?id="]')).toHaveCount(1);
  expect(await page.evaluate(() => dataLayer.some(item => item.event === 'contact_test'))).toBe(true);
});

test('prerendered generator activates and preserves saved answers', async ({ page }) => {
  await page.route('https://**/*', route => route.abort());
  await page.goto('/business-plan-generator.html');
  await expect(page.locator('#business-plan-generator-app')).not.toHaveAttribute('inert', '');
  await page.getByLabel('Business name').fill('CWV regression check');
  await page.getByRole('button', { name: 'Save and continue' }).click();
  await expect(page).toHaveURL(/#generator-2$/);
  await page.reload();
  await expect(page.getByLabel('Business name')).toHaveValue('CWV regression check');
});
