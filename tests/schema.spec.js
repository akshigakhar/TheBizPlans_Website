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

test('business plan generator uses webpage structured data without unsupported ratings', async ({ page }) => {
    await page.goto('/business-plan-generator.html');

    const structuredData = await page.locator('script[type="application/ld+json"]').allTextContents();
    const nodes = structuredData.flatMap((json) => {
        const data = JSON.parse(json);
        return data['@graph'] || [data];
    });
    const generatorPage = nodes.find((node) => node.url === 'https://thebizplans.com/business-plan-generator.html');

    expect(generatorPage).toMatchObject({
        '@type': 'WebPage',
        name: 'AI Business Plan Generator | TheBizPlanAI'
    });
    expect(nodes.some((node) => ['SoftwareApplication', 'WebApplication'].includes(node['@type']))).toBe(false);
});
