const { test, expect } = require('@playwright/test');

test('homepage loads without uncaught JavaScript exceptions', async ({ page }) => {
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));

    await page.goto('/', { waitUntil: 'load' });
    await expect(page.locator('body')).toBeVisible();
    await page.waitForTimeout(500);

    expect(errors).toEqual([]);
});

test('homepage uses its lightweight local stylesheet without legacy UI dependencies', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('link[rel="stylesheet"]')).toHaveCount(1);
    await expect(page.locator('link[rel="stylesheet"]')).toHaveAttribute('href', 'css/homepage.css');
    await expect(page.locator('link[href*="fonts.googleapis.com"]')).toHaveCount(0);
    await expect(page.locator('script[src*="bootstrap"]')).toHaveCount(0);
    await expect(page.locator('script[src*="owl"]')).toHaveCount(0);
});

test('mobile navigation exposes accessible state and opens without a framework', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 800 });
    await page.goto('/');
    const toggle = page.getByRole('button', { name: /menu/i });
    await expect(toggle).toHaveAttribute('aria-expanded', 'false');
    await toggle.click();
    await expect(toggle).toHaveAttribute('aria-expanded', 'true');
    await expect(page.locator('#primary-menu')).toHaveClass(/open/);
});

test('consultation menu buttons open Calendly while contact links stay on-site', async ({ page }) => {
    await page.goto('/');

    const consultButtons = page.locator('.nav-cta');
    await expect(consultButtons).toHaveCount(1);
    for (const button of await consultButtons.all()) {
        await expect(button).toHaveAttribute('href', 'https://calendly.com/atul_jagga/business-plan-free-consult');
        await expect(button).toHaveAttribute('target', '_blank');
        await expect(button).toHaveAttribute('rel', 'noopener');
    }

    await expect(page.locator('footer').getByRole('link', { name: 'Contact', exact: true }))
        .toHaveAttribute('href', 'contact.html');
});
