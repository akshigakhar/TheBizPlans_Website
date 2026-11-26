const { test, expect } = require('@playwright/test');

test('contact form posts every required lead field directly to Web3Forms', async ({ page }) => {
    await page.goto('/contact.html');

    const form = page.locator('#contact-form');
    await expect(form).toHaveAttribute('action', 'https://api.web3forms.com/submit');
    await expect(form).toHaveAttribute('method', 'post');
    await expect(form.locator('[name="access_key"]')).toHaveValue('df77cdd7-6ba9-470c-bc93-726ca8d2bca2');
    await expect(form.locator('[name="subject"]')).toHaveValue('New website enquiry from The Biz Plans');

    for (const field of ['name', 'email', 'phone', 'message']) {
        await expect(page.locator(`[name="${field}"]`)).toHaveAttribute('required', '');
    }

    const leadFields = form.locator('.form-control');
    const fieldNames = ['name', 'email', 'phone', 'purpose', 'source', 'message'];
    await expect(leadFields).toHaveCount(fieldNames.length);
    for (const [index, field] of fieldNames.entries()) {
        await expect(leadFields.nth(index)).toHaveAttribute('name', field);
    }

    await expect(page.getByRole('button', { name: 'Send Message' })).toHaveAttribute('type', 'submit');
});

for (const source of ['Referral', '']) {
    const sourceCase = source ? 'with attribution' : 'without attribution';

    test(`contact form validates and submits without leaving the page ${sourceCase}`, async ({ page }) => {
        const submissions = [];
        await page.route('https://www.googletagmanager.com/**', (route) => route.abort());
        await page.route('https://api.web3forms.com/submit', async (route) => {
            submissions.push(route.request().postData());
            await route.fulfill({
                status: 200,
                contentType: 'application/json',
                body: JSON.stringify({ success: true })
            });
        });
        await page.goto('/contact.html');

        await page.locator('[name="name"]').fill('Test User');
        await page.locator('[name="email"]').fill('test@example.com');
        await page.locator('[name="phone"]').fill('555-0100');
        await page.locator('[name="message"]').fill('Test message');
        const purpose = page.getByLabel('What do you need?');
        const sourceField = page.getByLabel('How did you hear about us?');
        const submit = page.getByRole('button', { name: 'Send Message' });

        await submit.click();
        await expect(purpose).toBeFocused();
        expect(await purpose.evaluate((field) => field.validity.valueMissing)).toBe(true);
        expect(submissions).toHaveLength(0);

        await purpose.selectOption('Pitch deck');
        if (source) await sourceField.selectOption(source);
        await submit.click();

        await expect(page).toHaveURL(/\/contact\.html$/);
        await expect(page.getByRole('status')).toHaveText('Thank you! Your message has been sent.');
        await expect(purpose).toHaveValue('');
        await expect(sourceField).toHaveValue('');
        expect(submissions).toHaveLength(1);
        expect(submissions[0]).toContain('name="purpose"\r\n\r\nPitch deck\r\n');
        expect(submissions[0]).toContain(`name="source"\r\n\r\n${source}\r\n`);
        const events = await page.evaluate(() => window.dataLayer
            .filter((entry) => entry[0] === 'event' && entry[1] === 'contact_form_submit')
            .map((entry) => entry[2]));
        expect(events).toEqual([{
            page_path: '/contact.html',
            purpose: 'Pitch deck',
            ...(source && { source })
        }]);
    });
}

test('WhatsApp calls to action use the public business click-to-chat URL', async ({ page }) => {
    await page.goto('/contact.html');

    await expect(page.getByRole('link', { name: 'Connect on WhatsApp' }))
        .toHaveAttribute('href', 'https://wa.me/16478968362');
});

test('WhatsApp redirect remains crawlable but is excluded from search results', async ({ page }) => {
    await page.goto('/whatsapp.html');

    await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', 'noindex, follow');
});
