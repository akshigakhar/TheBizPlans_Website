const { test, expect } = require('@playwright/test');

test('homepage loads without uncaught JavaScript exceptions', async ({ page }) => {
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));

    await page.goto('/', { waitUntil: 'load' });
    await expect(page.locator('body')).toBeVisible();
    await page.waitForTimeout(500);

    expect(errors).toEqual([]);
});
