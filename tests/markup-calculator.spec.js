const { test, expect } = require('@playwright/test');

test('calculates both modes and rejects invalid or overflowing values locally', async ({ page }) => {
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.route('**/*', route => new URL(route.request().url()).hostname === '127.0.0.1' ? route.continue() : route.abort());
    await page.goto('/markup-calculator.html');
    const result = id => page.locator(`#${id}-result`);
    await expect(result('markup')).toHaveText('50.00%');
    await expect(result('margin')).toHaveText('33.33%');
    await expect(result('profit')).toHaveText('$25.00');
    for (const [cost, price, markup, margin, profit] of [[50,100,'100.00%','50.00%','$50.00'],[80,100,'25.00%','20.00%','$20.00'],[100,80,'-20.00%','-25.00%','-$20.00']]) {
        await page.locator('#cost').fill(String(cost));
        await page.locator('#price').fill(String(price));
        await expect(result('markup')).toHaveText(markup);
        await expect(result('margin')).toHaveText(margin);
        await expect(result('profit')).toHaveText(profit);
    }
    for (const value of ['', '0', '-1']) {
        await page.locator('#cost').fill(value);
        await expect(result('markup')).toHaveText('—');
        await expect(page.locator('#cost')).toHaveAttribute('aria-invalid', 'true');
    }
    await page.locator('#cost').fill('50');
    await page.locator('#price').fill('0');
    await expect(result('margin')).toHaveText('—');
    await page.selectOption('#calculation-mode', 'markup');
    await expect(page.locator('#price')).toBeDisabled();
    await page.locator('#target-markup').fill('100');
    await expect(result('price')).toHaveText('$100.00');
    await expect(result('margin')).toHaveText('50.00%');
    await page.locator('#target-markup').fill('0');
    await expect(result('profit')).toHaveText('$0.00');
    await page.locator('#target-markup').fill('-1');
    await expect(result('price')).toHaveText('—');
    await page.locator('#cost').fill('1e308');
    await page.locator('#target-markup').fill('1e308');
    await expect(result('markup')).toHaveText('—');
    await expect(page.locator('#calculator-error')).toContainText('too large');
    expect(errors).toEqual([]);
});

test('FAQ schema matches visible answers and mobile layout fits', async ({ page }) => {
    await page.goto('/markup-calculator.html');
    const faq = await page.locator('script[type="application/ld+json"]').evaluateAll(nodes => nodes.flatMap(node => JSON.parse(node.textContent)['@graph'] || []).find(item => item['@type'] === 'FAQPage'));
    expect(faq.mainEntity).toHaveLength(5);
    for (const question of faq.mainEntity) {
        await expect(page.getByRole('heading', { name: question.name, exact: true })).toBeVisible();
        await expect(page.getByText(question.acceptedAnswer.text, { exact: true })).toBeVisible();
    }
    await page.setViewportSize({ width: 390, height: 844 });
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth)).toBe(true);
});
