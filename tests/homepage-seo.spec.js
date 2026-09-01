const { test, expect } = require('@playwright/test');

test('homepage preserves primary SEO signals and valid structured data', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle('Professional Business Plan Writer Canada | The Biz Plans');
  await expect(page.locator('h1')).toHaveCount(1);
  await expect(page.locator('h1')).toHaveText('Professional Business Plan Writers in Canada');
  await expect(page.locator('link[rel="canonical"]')).toHaveCount(1);
  await expect(page.locator('link[rel="canonical"]')).toHaveAttribute('href', 'https://thebizplans.com/');
  await expect(page.locator('meta[name="description"]')).toHaveAttribute('content', /Professional business plan writers serving Canada/);
  await expect(page.locator('meta[name="robots"][content*="noindex"]')).toHaveCount(0);

  const jsonLd = await page.locator('script[type="application/ld+json"]').allTextContents();
  expect(() => jsonLd.map(JSON.parse)).not.toThrow();
  const nodes = jsonLd.map(JSON.parse).flatMap(data => data['@graph'] || [data]);
  const organizations = nodes.filter(node => node['@type'] === 'Organization');
  expect(organizations).toHaveLength(1);
  expect(organizations[0].url).toBe('https://thebizplans.com/');
  expect(organizations[0]['@id']).toBe('https://thebizplans.com/#organization');
  expect(organizations[0].founder['@id']).toBe('https://thebizplans.com/#atul-jagga');
});

test('commercial journey and homepage links work at desktop, tablet and mobile widths', async ({ page }) => {
  for (const width of [1440, 768, 375]) {
    await page.setViewportSize({ width, height: 900 });
    await page.goto('/');
    await expect(page.locator('#hero')).toBeVisible();
    await expect(page.locator('#our-services')).toBeVisible();
    await expect(page.locator('#our-services h3')).toHaveCount(4);
    await expect(page.locator('body')).not.toHaveCSS('overflow-x', 'scroll');
  }

  const expectedLinks = [
    'services.html', 'project-brief.html', 'bank-loan-business-plans.html',
    'immigration-business-plans.html', 'investor-business-plan.html',
    'strategic-business-plan.html', 'financial-modeling.html', 'pricing.html', 'case-studies.html',
    'testimonials.html', 'about-business-plan.html', 'blog-learning-hub.html',
    'business-plan-essentials.html', 'business-plan-template.html',
    'business-plan-generator.html', 'industry-business-plans.html', 'contact.html'
  ];
  for (const href of expectedLinks) {
    await expect(page.locator(`a[href="${href}"]`).first()).toBeVisible();
  }
  await expect(page.locator('a[href="https://calendly.com/atul_jagga/business-plan-free-consult"]').first()).toBeVisible();
});
