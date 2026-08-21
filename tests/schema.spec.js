const { test, expect } = require('@playwright/test');

test('site organization structured data includes a complete postal address', async ({ page }) => {
    await page.goto('/bank-loan-business-plans.html');

    const structuredData = await page.locator('script[type="application/ld+json"]').allTextContents();
    const nodes = structuredData.flatMap((json) => {
        const data = JSON.parse(json);
        return data['@graph'] || [data];
    });
    const organization = nodes.find((node) => node['@id'] === 'https://thebizplans.com/#organization');

    expect(organization).toBeDefined();
    expect(organization.address).toEqual({
        '@type': 'PostalAddress',
        streetAddress: '51 Burnhamill Pl',
        addressLocality: 'Toronto',
        addressRegion: 'ON',
        postalCode: 'M9C 3S3',
        addressCountry: 'CA'
    });
});
