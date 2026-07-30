const { test, expect } = require('@playwright/test');

test('contact form requires every lead field and displays the confirmation', async ({ page }) => {
    await page.route('https://api.web3forms.com/submit', async route => {
        const request = route.request();
        const body = request.postData() || '';

        expect(body).toContain('name=Taylor');
        expect(body).toContain('phone=647');
        expect(body).toContain('email=taylor%40example.com');
        expect(body).toContain('message=I+need+a+business+plan');
        expect(body).toContain('access_key=df77cdd7-6ba9-470c-bc93-726ca8d2bca2');
        expect(body).toContain('subject=New+website+enquiry+from+The+Biz+Plans');

        await route.fulfill({
            status: 200,
            contentType: 'application/json',
            body: JSON.stringify({ success: true })
        });
    });

    await page.goto('/contact.html');

    for (const field of ['name', 'phone', 'email', 'message']) {
        await expect(page.locator(`[name="${field}"]`)).toHaveAttribute('required', '');
    }

    await page.locator('[name="name"]').fill('Taylor');
    await page.locator('[name="phone"]').fill('647 555 0100');
    await page.locator('[name="email"]').fill('taylor@example.com');
    await page.locator('[name="message"]').fill('I need a business plan');
    await page.getByRole('button', { name: 'Send Message' }).click();

    const confirmation = page.locator('#contact-success');
    await expect(confirmation).toBeVisible();
    await expect(confirmation).toContainText('Your message has been received by the team.');
    await expect(confirmation).toContainText('You will hear back from us in 24–48 hours.');
    await expect(confirmation.getByRole('link', { name: 'Call Us' })).toBeVisible();
    await expect(confirmation.getByRole('link', { name: 'Book a Consult' })).toBeVisible();
});

test('contact form handles a non-JSON server error without exposing a parsing error', async ({ page }) => {
    await page.route('https://api.web3forms.com/submit', route => route.fulfill({
        status: 405,
        contentType: 'text/html',
        body: '<html><head><title>Method Not Allowed</title></head></html>'
    }));

    await page.goto('/contact.html');
    await page.locator('[name="name"]').fill('Taylor');
    await page.locator('[name="phone"]').fill('647 555 0100');
    await page.locator('[name="email"]').fill('taylor@example.com');
    await page.locator('[name="message"]').fill('I need a business plan');
    await page.getByRole('button', { name: 'Send Message' }).click();

    const status = page.locator('.contact-form-status');
    await expect(status).toContainText('We could not send your message online.');
    await expect(status).toContainText('info@thebizplans.com');
    await expect(status).not.toContainText('Unexpected token');
    await expect(page.getByRole('button', { name: 'Send Message' })).toBeEnabled();
});
