const { test, expect } = require('@playwright/test');

const pages = [
  '/', '/services.html', '/bank-loan-business-plans.html', '/royal-bank-of-canada.html',
  '/business-development-bank-of-canada.html', '/industry-business-plans.html',
  '/trucking-business-plans.html', '/toronto-business-plan-writers.html',
  '/vancouver-business-plan-writers.html', '/immigration-business-plans.html',
  '/blog-learning-hub.html', '/about-business-plan.html', '/pricing.html', '/contact.html',
  '/business-plan-template.html', '/business-plan-generator.html'
];

const labels = ['Services', 'Financing', 'Industries', 'Free Tools', 'Learn', 'About'];

test('representative public pages use the canonical accessible header', async ({ page }) => {
  for (const path of pages) {
    await page.goto(path);
    const nav = page.getByRole('navigation', { name: 'Primary navigation' });
    await expect(nav).toHaveCount(1);
    await expect(nav.locator('.navbar-brand')).toHaveAttribute('href', '/');
    await expect(nav.locator('#navbarCollapse')).toHaveCount(1);
    await expect(nav.locator('#navbarCollapse > .navbar-nav')).toHaveCount(1);
    await expect(nav.getByRole('link', { name: 'Home', exact: true })).toHaveCount(0);
    await expect(nav.locator('.nav-cta')).toHaveAttribute('href', 'contact.html');
    for (const label of labels) await expect(nav.getByRole('link', { name: label, exact: true })).toHaveCount(1);
  }
});

test('desktop dropdowns work without a visible caret and use 15px labels', async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto('/services.html');
  const services = page.getByRole('link', { name: 'Services', exact: true });
  await expect(services).toHaveCSS('font-size', '15px');
  expect(await services.evaluate(el => getComputedStyle(el, '::after').display)).toBe('none');
  await services.click();
  await expect(page.getByRole('link', { name: 'Business Plan Writing Services', exact: true })).toBeVisible();
  await expect(services).toHaveAttribute('aria-expanded', 'true');
});

test('mobile collapse and dropdown update accessible state without overflow', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 800 });
  await page.goto('/contact.html');
  const toggle = page.getByRole('button', { name: 'Toggle navigation' });
  await expect(toggle).toHaveAttribute('aria-expanded', 'false');
  await toggle.click();
  await expect(toggle).toHaveAttribute('aria-expanded', 'true');
  const services = page.getByRole('link', { name: 'Services', exact: true });
  await expect(services).toHaveCSS('font-size', '16px');
  await services.click();
  await expect(services).toHaveAttribute('aria-expanded', 'true');
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= document.documentElement.clientWidth)).toBe(true);
});
