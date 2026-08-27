const { test, expect } = require('@playwright/test');

const externalLinks = [
    {
        page: '/cibc.html',
        href: 'https://www.cibc.com/en/business/loans-and-lines-of-credit.html',
        name: 'CIBC Business Loans and Lines of Credit'
    },
    {
        page: '/indigenous-aboriginal-entrepreneurship.html',
        href: 'https://nacca.ca',
        name: 'National Aboriginal Capital Corporations Association (NACCA)'
    },
    {
        page: '/indigenous-aboriginal-entrepreneurship.html',
        href: 'https://www.ccab.com',
        name: 'Canadian Council for Aboriginal Business (CCAB)'
    }
];

test('external resources use descriptive anchor text', async ({ page }) => {
    for (const link of externalLinks) {
        await page.goto(link.page);

        const matchingLink = page.locator(`a[href="${link.href}"]`).filter({ hasText: link.name }).first();
        await expect(matchingLink).toHaveText(link.name);
    }
});

test('known retired external resource URLs are not linked', async ({ page }) => {
    const retiredLinks = [
        ['/cibc.html', 'fees-and-details.html'],
        ['/dallas-business-plan-writers.html', 'small-business-center.aspx'],
        ['/export-development-canada.html', '/en/insights-and-resources.html'],
        ['/export-development-canada.html', '/en/articles.html'],
        ['/authoritative-resources.html', '/en/articles.html']
    ];

    for (const [sitePage, retiredPath] of retiredLinks) {
        await page.goto(sitePage);
        await expect(page.locator(`a[href*="${retiredPath}"]`)).toHaveCount(0);
    }
});
