const { test, expect } = require('@playwright/test');

test('blog article links have descriptive anchor text', async ({ page }) => {
    await page.goto('/blog-learning-hub.html');

    const articleLinks = page.locator('main article > a.btn');
    await expect(articleLinks).toHaveCount(20);

    const linkNames = await articleLinks.allTextContents();
    for (const linkName of linkNames) {
        expect(linkName.trim()).not.toMatch(/^read more$/i);
        expect(linkName.trim().split(/\s+/).length).toBeGreaterThan(3);
    }
});

test('service cards have descriptive anchor text', async ({ page }) => {
    await page.goto('/services.html');

    await expect(page.getByRole('link', { name: 'Explore financial modeling and valuation' })).toHaveAttribute('href', 'financial-modeling.html');
    await expect(page.getByRole('link', { name: 'Explore marketing and growth strategy' })).toHaveAttribute('href', 'marketing-growth-strategy.html');
});
