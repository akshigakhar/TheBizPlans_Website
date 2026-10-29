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

    const leadFields = page.locator('#contact-form .form-control');
    await expect(leadFields).toHaveCount(4);
    for (const [index, field] of ['name', 'email', 'phone', 'message'].entries()) {
        await expect(leadFields.nth(index)).toHaveAttribute('name', field);
    }

    await expect(page.getByRole('button', { name: 'Send Message' })).toHaveAttribute('type', 'submit');
});

test('contact form submits without leaving the contact page', async ({ page }) => {
    await page.route('https://api.web3forms.com/submit', async (route) => {
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
    await page.getByRole('button', { name: 'Send Message' }).click();

    await expect(page).toHaveURL(/\/contact\.html$/);
    await expect(page.getByRole('status')).toHaveText('Thank you! Your message has been sent.');
});

test('WhatsApp calls to action use the public business click-to-chat URL', async ({ page }) => {
    await page.goto('/contact.html');

    await expect(page.getByRole('link', { name: 'Connect on WhatsApp' }))
        .toHaveAttribute('href', 'https://wa.me/16478968362');
});

test('WhatsApp redirect remains crawlable but is excluded from search results', async ({ page }) => {
    await page.goto('/whatsapp.html');

    await expect(page.locator('meta[name="robots"]')).toHaveAttribute('content', 'noindex, follow');
});
