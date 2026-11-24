const { test, expect } = require('@playwright/test');

test('generator is embedded while static SEO content remains', async ({ page }) => {
  await page.goto('/business-plan-generator.html');
  await expect(page.locator('#business-plan-generator-app')).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Free Business Plan Generator', exact: true })).toBeVisible();
  await expect(page.getByRole('heading', { name: 'Can AI write a complete business plan?' })).toBeVisible();
  await expect(page.locator('link[rel="canonical"]')).toHaveAttribute('href', 'https://thebizplans.com/business-plan-generator.html');
});

test('generator saves answers, navigates, and does not overflow at responsive widths', async ({ page }) => {
  for (const width of [1440, 1200, 1024, 768, 430, 375]) {
    await page.setViewportSize({ width, height: 900 });
    await page.goto('/business-plan-generator.html');
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= document.documentElement.clientWidth)).toBe(true);
  }
  const consult = page.getByRole('region', { name: 'Professional business plan writing' });
  await expect(consult.getByRole('heading')).toHaveText('Want this done for you?');
  await page.getByRole('button', { name: 'Build My Business Plan' }).click();
  const businessName = page.locator('.info-card input').first();
  await businessName.fill('Sample Company');
  await page.getByRole('button', { name: 'Continue to Business Plan' }).click();
  await expect(consult).toHaveCount(0);
  await page.getByRole('button', { name: 'Continue to Financial Projections' }).click();
  await page.getByRole('button', { name: /Projection Preview/ }).click();
  await page.getByRole('button', { name: 'Continue to Review' }).click();
  await expect(page.getByText('Sample Company', { exact: true })).toBeVisible();
  await expect(consult.getByRole('link', { name: 'Call +1-647-896-8362' })).toHaveAttribute('href', 'tel:+16478968362');
  await expect(consult.getByRole('link', { name: 'See business plan writing services' })).toHaveAttribute('href', '/business-plan-writing-services.html');
  await expect(consult.getByRole('link', { name: 'See pricing' })).toHaveAttribute('href', '/pricing.html');
  await page.getByRole('button', { name: 'Continue to Download' }).click();
  await expect(page.getByRole('heading', { name: /Download Business Plan PDF/i })).toBeVisible();
  await page.reload();
  await page.getByRole('button', { name: 'Build My Business Plan' }).click();
  await expect(businessName).toHaveValue('Sample Company');
});

test('generator landing uses the available page width without breaking its hero layout', async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto('/business-plan-generator.html');

  await expect(page.locator('.free-landing .landing-nav')).toHaveCount(0);
  await expect(page.getByRole('button', { name: 'Start My Free Plan' })).toHaveCount(0);

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
