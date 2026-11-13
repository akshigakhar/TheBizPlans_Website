const { test, expect } = require('@playwright/test');
if (process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH) {
  test.use({ launchOptions: { executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH } });
}
const result = page => page.locator('[data-results]');

test('break-even rounds units up, handles zero contribution, and clears stale results on invalid input', async ({ page }) => {
  await page.goto('/break-even-calculator.html');
  await expect(result(page)).toContainText('500');
  await expect(result(page)).toContainText('$25,000.00');
  await page.locator('#fixed').fill('10001');
  await expect(result(page)).toContainText('501');
  await expect(result(page)).toContainText('$25,050.00');
  await page.locator('#price').fill('30');
  await expect(result(page)).toContainText('No achievable break-even');
  await page.locator('#fixed').fill('-1');
  await expect(result(page)).toContainText('unavailable');
  await page.locator('#fixed').fill('');
  await expect(page.locator('[data-error]')).not.toBeEmpty();
  await page.locator('#fixed').fill('0');
  await expect(result(page)).toContainText('Zero sales covers zero fixed costs');
});

test('loan amortization matches reference values and zero interest works', async ({ page }) => {
  await page.goto('/loan-payment-calculator.html');
  await expect(result(page)).toContainText('$1,933.28');
  await expect(result(page)).toContainText('$15,996.81');
  await page.locator('#rate').fill('0');
  await expect(result(page)).toContainText('$1,666.67');
  await expect(result(page)).toContainText('$0.00');
  await page.locator('#years').fill('0');
  await expect(result(page)).toContainText('unavailable');
  await page.locator('#years').fill('1.5');
  await expect(result(page)).toContainText('unavailable');
});

test('CSBFP requires prime, applies both caps, finances fees within limits and reconciles total cost', async ({ page }) => {
  await page.goto('/csbfp-loan-calculator.html');
  await expect(page.locator('#prime')).toHaveValue('');
  await expect(result(page)).toContainText('unavailable');
  // Test assumption only, not a site claim about current prime.
  await page.locator('#prime').fill('4');
  await page.locator('#years').fill('1');
  await page.locator('#loc').fill('10000');
  await expect(result(page)).toContainText('7%');
  await expect(result(page)).toContainText('9%');
  await expect(result(page)).toContainText('$75.00');
  await expect(result(page)).toContainText('$3,965.68'); // term + LOC interest
  await expect(result(page)).toContainText('$95,765.68'); // 90k advances + 1800 fee + interest
  await page.locator('#finance').check();
  await expect(result(page)).toContainText('$81,600.00');
  await expect(result(page)).toContainText('$10,200.00');
  await expect(result(page)).toContainText('$76.50');
  await expect(result(page)).toContainText('$95,844.99');
  await page.locator('#term').fill('1000000');
  await expect(page.locator('[data-error]')).toContainText('financed balance');
  await page.locator('#finance').uncheck();
  await page.locator('#loc').fill('150000');
  await expect(page.locator('[data-error]')).toBeEmpty();
  await page.locator('#loc').fill('150001');
  await expect(result(page)).toContainText('unavailable');
});

test('markup and margin use distinct denominators and handle zero and loss', async ({ page }) => {
  await page.goto('/markup-margin-calculator.html');
  await expect(result(page)).toContainText('66.67%');
  await expect(result(page)).toContainText('40%');
  await page.locator('#cost').fill('0');
  await expect(result(page)).toContainText('Undefined (zero cost)');
  await page.locator('#price').fill('0');
  await expect(result(page)).toContainText('Undefined (zero price)');
  await page.locator('#cost').fill('60');
  await page.locator('#price').fill('30');
  await expect(result(page)).toContainText('-$30.00');
  await expect(result(page)).toContainText('-50%');
  await expect(result(page)).toContainText('-100%');
});

test('startup line items start at zero, sum groups, add, edit, validate, remove', async ({ page }) => {
  await page.goto('/startup-cost-calculator.html');
  for (const input of await page.locator('[data-amount]').all()) await expect(input).toHaveValue('0');
  await page.locator('#amount-once-0').fill('1000');
  await page.locator('#amount-operating-0').fill('300');
  await expect(result(page)).toContainText('$1,300.00');
  await page.locator('[data-group=once] [data-add]').click();
  await page.locator('#custom-cost-0-label').fill('My quote');
  await page.locator('#custom-cost-0').fill('50');
  await expect(result(page)).toContainText('$1,350.00');
  await page.locator('#custom-cost-0').fill('-1');
  await expect(result(page)).toContainText('unavailable');
  await page.locator('.cost-row').filter({ has: page.locator('#custom-cost-0') }).locator('[data-remove]').click();
  await expect(result(page)).toContainText('$1,300.00');
});

const slugs = ['business-calculators', 'break-even-calculator', 'loan-payment-calculator', 'csbfp-loan-calculator', 'markup-margin-calculator', 'startup-cost-calculator', 'ebitda-calculator'];
test('all pages fit desktop and mobile, have local links and valid FAQ JSON-LD', async ({ page }) => {
  for (const slug of slugs) {
    await page.goto(`/${slug}.html`);
    for (const width of [1440, 375]) {
      await page.setViewportSize({ width, height: 900 });
      expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    }
    await expect(page.locator('h1')).toHaveCount(1);
    const fs = require('node:fs');
    const path = require('node:path');
    for (const href of await page.locator('main a[href]').evaluateAll(links => links.map(a => a.getAttribute('href')))) {
      if (!href.startsWith('http') && !href.startsWith('#')) {
        expect(fs.existsSync(path.join(process.cwd(), href.split('#')[0])), href).toBe(true);
      }
    }
    await expect(page.locator('link[rel=canonical]')).toHaveAttribute('href', `https://thebizplans.com/${slug}.html`);
    if (slug !== 'business-calculators') {
      const schema = JSON.parse(await page.locator('[data-page-faq]').textContent());
      expect(schema['@type']).toBe('FAQPage');
      expect(schema.mainEntity.length).toBeGreaterThan(1);
      await expect(page.locator('main details[open]')).toBeVisible();
    }
  }
});

test('explanations, examples, FAQs and next steps remain readable with JavaScript disabled', async ({ browser }) => {
  const context = await browser.newContext({ javaScriptEnabled: false });
  const page = await context.newPage();
  for (const slug of slugs.slice(1)) {
    await page.goto(`http://127.0.0.1:4173/${slug}.html`);
    await expect(page.getByRole('heading', { name: 'Formula and assumptions' })).toBeVisible();
    await expect(page.getByText('Worked example — illustrative only')).toBeVisible();
    await expect(page.getByRole('heading', { name: 'Frequently asked questions' })).toBeVisible();
    await expect(page.locator('noscript').last()).toBeVisible();
    await expect(page.locator('[data-add]:visible, [data-remove]:visible')).toHaveCount(0);
    await page.locator('main details').last().locator('summary').click();
    await expect(page.locator('main details').last()).toHaveAttribute('open', '');
  }
  await context.close();
});


test('EBITDA reconciles add-backs, optional fields, losses, zero revenue and invalid inputs', async ({ page }) => {
  await page.goto('/ebitda-calculator.html');
  await expect(result(page)).toContainText('$100,000.00');
  await expect(result(page)).toContainText('20%');
  await page.locator('#includes-da').uncheck();
  await expect(result(page)).toContainText('$80,000.00');
  await expect(result(page)).toContainText('16%');
  await page.locator('#opex').fill('200000');
  await expect(result(page)).toContainText('$100,000.00');
  await page.locator('#includes-da').check();
  await page.locator('#depreciation').fill('');
  await page.locator('#amortisation').fill('');
  await expect(result(page)).toContainText('$100,000.00');
  await page.locator('#revenue').fill('100000');
  await expect(result(page)).toContainText('-$300,000.00');
  await expect(result(page)).toContainText('-300%');
  await page.locator('#revenue').fill('0');
  await expect(result(page)).toContainText('Undefined (zero revenue)');
  await page.locator('#cogs').fill('-1');
  await expect(result(page)).toContainText('unavailable');
  await expect(page.locator('#cogs')).toHaveAttribute('aria-invalid', 'true');
  await page.locator('#cogs').fill('0');
  await page.locator('#revenue').fill('');
  await expect(result(page)).toContainText('unavailable');
  await page.locator('#revenue').fill('0');
  await page.locator('#opex').fill('0');
  await expect(result(page)).toContainText('$0.00');
  const schema = JSON.parse(await page.locator('[data-page-faq]').textContent());
  const faqs = page.locator('main details:not([open])');
  for (let i = 0; i < schema.mainEntity.length; i++) {
    await expect(faqs.nth(i).locator('summary')).toHaveText(schema.mainEntity[i].name);
    await expect(faqs.nth(i).locator('p')).toHaveText(schema.mainEntity[i].acceptedAnswer.text);
  }
});
