const { test, expect } = require('@playwright/test');

test('homepage ProfessionalService schema matches the visible NAP and business details', async ({ page }) => {
    await page.goto('/');

    const structuredData = await page.locator('script[type="application/ld+json"]').allTextContents();
    const nodes = structuredData.flatMap((json) => {
        const data = JSON.parse(json);
        return data['@graph'] || [data];
    });
    const service = nodes.find((node) => node['@type'] === 'ProfessionalService');

    expect(service).toMatchObject({
        name: 'The Biz Plans',
        url: 'https://thebizplans.com/',
        telephone: '+1-647-896-8362',
        address: {
            streetAddress: '51 Burnhamill Pl',
            addressLocality: 'Toronto',
            addressRegion: 'ON',
            postalCode: 'M9C 3S3',
            addressCountry: 'CA'
        },
        openingHoursSpecification: {
            dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            opens: '09:00',
            closes: '17:00'
        },
        areaServed: 'Canada',
        founder: { name: 'Atul Jagga' }
    });

    const footer = page.locator('#footer');
    await expect(footer).toContainText('The Biz Plans');
    await expect(footer).toContainText('+1-647-896-8362');
    await expect(footer).toContainText('51 Burnhamill Pl');
    await expect(footer).toContainText('Toronto, ON M9C 3S3');
    await expect(footer).toContainText('CA');
});

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
    expect(nodes.find((node) => node['@type'] === 'SoftwareApplication')).toMatchObject({
        name: 'TheBizPlanAI', applicationCategory: 'BusinessApplication', operatingSystem: 'Web',
        offers: { '@type': 'Offer', price: '0', priceCurrency: 'CAD' }
    });
    expect(nodes.find((node) => node['@type'] === 'FAQPage').mainEntity).toHaveLength(5);
    expect(nodes.find((node) => node['@type'] === 'Person').name).toBe('Atul Jagga');
    expect(nodes.some((node) => node.aggregateRating || node.review)).toBe(false);
});
