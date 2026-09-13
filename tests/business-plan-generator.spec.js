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
