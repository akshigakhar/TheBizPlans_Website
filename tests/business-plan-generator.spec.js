const { test, expect } = require('@playwright/test');

test('generator is embedded while static SEO content remains', async ({ page }) => {
  await page.goto('/business-plan-generator.html');
  await expect(page.locator('#business-plan-generator-app')).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Build your business plan draft' })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Can AI write a complete business plan?' })).toBeVisible();
  await expect(page.locator('link[rel="canonical"]')).toHaveAttribute('href', 'https://thebizplans.com/business-plan-generator.html');
});

test('generator saves answers, navigates, and does not overflow at responsive widths', async ({ page }) => {
  for (const width of [1440, 1200, 1024, 768, 430, 375]) {
    await page.setViewportSize({ width, height: 900 });
    await page.goto('/business-plan-generator.html');
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= document.documentElement.clientWidth)).toBe(true);
  }
  await page.getByLabel('Business name').fill('Sample Company');
  await page.getByRole('button', { name: 'Save and continue' }).click();
  await expect(page).toHaveURL(/#generator-2$/);
  await page.reload();
  await page.getByRole('button', { name: /Business/ }).click();
  await expect(page.getByLabel('Business name')).toHaveValue('Sample Company');
});

test('generator landing uses the available page width without breaking its hero layout', async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto('/business-plan-generator.html');

  const layout = await page.locator('.business-plan-generator-tool').evaluate((tool) => {
    const hero = tool.querySelector('.free-landing .hero');
    const heading = tool.querySelector('.hero-copy h1');
    const preview = tool.querySelector('.plan-preview');
    const toolBounds = tool.getBoundingClientRect();
    const heroBounds = hero.getBoundingClientRect();
    const headingBounds = heading.getBoundingClientRect();
    const previewBounds = preview.getBoundingClientRect();

    return {
      toolWidth: toolBounds.width,
      heroWidth: heroBounds.width,
      headingWidth: headingBounds.width,
      previewWidth: previewBounds.width,
      viewportWidth: document.documentElement.clientWidth,
    };
  });

  expect(layout.toolWidth).toBe(layout.viewportWidth);
  expect(layout.heroWidth).toBe(layout.viewportWidth);
  expect(layout.headingWidth).toBeGreaterThan(450);
  expect(layout.previewWidth).toBeGreaterThan(400);
});
