const { test, expect } = require('@playwright/test');

test('homepage loads without uncaught JavaScript exceptions', async ({ page }) => {
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));

    await page.goto('/', { waitUntil: 'load' });
    await expect(page.locator('body')).toBeVisible();
    await page.waitForTimeout(500);

    expect(errors).toEqual([]);
});

test('consultation menu buttons open Calendly while contact links stay on-site', async ({ page }) => {
    await page.goto('/');

    const consultButtons = page.locator('.nav-cta');
    await expect(consultButtons).toHaveCount(2);
    for (const button of await consultButtons.all()) {
        await expect(button).toHaveAttribute('href', 'https://calendly.com/atul_jagga/business-plan-free-consult');
        await expect(button).toHaveAttribute('target', '_blank');
        await expect(button).toHaveAttribute('rel', 'noopener');
    }

    await expect(page.locator('footer').getByRole('link', { name: 'Contact', exact: true }))
        .toHaveAttribute('href', 'contact.html');
});
