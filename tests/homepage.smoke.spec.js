const { test, expect } = require('@playwright/test');

test('homepage loads without uncaught JavaScript exceptions', async ({ page }) => {
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));

    await page.goto('/', { waitUntil: 'load' });
    await expect(page.locator('body')).toBeVisible();
    await page.waitForTimeout(500);

    expect(errors).toEqual([]);
});

test('homepage uses the shared Bootstrap header plus its local page stylesheet', async ({ page }) => {
  await page.goto('/');
  await expect(page.locator('link[href="css/bootstrap.min.css"]')).toHaveCount(1);
  await expect(page.locator('link[href="css/style.min.css"]')).toHaveCount(1);
  await expect(page.locator('link[href="css/homepage-redesign.css"]')).toHaveCount(1);
  await expect(page.locator('link[href*="fonts.googleapis.com"]')).toHaveCount(0);
  await expect(page.locator('script[src*="bootstrap"]')).toHaveCount(1);
    await expect(page.locator('script[src*="owl"]')).toHaveCount(0);
});

test('mobile navigation exposes accessible state and opens', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 800 });
    await page.goto('/');
  const toggle = page.getByRole('button', { name: 'Toggle navigation' });
    await expect(toggle).toHaveAttribute('aria-expanded', 'false');
    await toggle.click();
    await expect(toggle).toHaveAttribute('aria-expanded', 'true');
  await expect(page.locator('#navbarCollapse')).toHaveClass(/show/);
});

test('global consultation links direct visitors to Calendly', async ({ page }) => {
    await page.goto('/');

    const calendlyUrl = 'https://calendly.com/atul_jagga/business-plan-free-consult';
    const consultButtons = page.locator('.nav-cta');
    await expect(consultButtons).toHaveCount(1);
    for (const button of await consultButtons.all()) {
        await expect(button).toHaveAttribute('href', calendlyUrl);
    }

    await expect(page.locator('footer').getByRole('link', { name: 'Book a Consult', exact: true }))
        .toHaveAttribute('href', calendlyUrl);
    await expect(page.locator('footer').getByRole('link', { name: 'Contact', exact: true }))
        .toHaveAttribute('href', 'contact.html');
});

test('homepage highlights the founder and keeps planning resources available', async ({ page }) => {
  await page.goto('/');

  await expect(page.getByRole('heading', { name: 'Founder-Led Business Plan and Financial Work' })).toBeVisible();
  await expect(page.locator('.credential-badges')).toContainText('CPA');
  await expect(page.getByRole('link', { name: 'Free Business Plan Generator', exact: true }).last())
    .toHaveAttribute('href', 'business-plan-generator.html');
  await expect(page.getByRole('link', { name: 'Business Plan Essentials', exact: true }).last())
    .toHaveAttribute('href', 'business-plan-essentials.html');
});
