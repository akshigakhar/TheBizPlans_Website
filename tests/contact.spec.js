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
