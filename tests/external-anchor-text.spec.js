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
