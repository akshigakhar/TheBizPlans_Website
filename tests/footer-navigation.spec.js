const { test, expect } = require('@playwright/test');

test('footer progressively discloses locations, industries and financing links', async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto('/');

  for (const [label, revealedLink] of [
    ['Locations', 'Edmonton'],
    ['Industries', 'Brewery'],
    ['Financing Resources', 'TD']
  ]) {
    const button = page.getByRole('button', { name: `See All ${label}`, exact: true });
    await expect(button).toHaveAttribute('aria-expanded', 'false');
    await expect(page.getByRole('contentinfo').getByRole('link', { name: revealedLink, exact: true })).toBeHidden();
    await button.press('Enter');
    await expect(button).toHaveAttribute('aria-expanded', 'true');
    await expect(page.getByRole('contentinfo').getByRole('link', { name: revealedLink, exact: true })).toBeVisible();
    await page.getByRole('button', { name: `Show Fewer ${label}`, exact: true }).click();
    await expect(button).toHaveAttribute('aria-expanded', 'false');
  }
});

test('mobile footer categories are collapsed and keyboard accessible without overflow', async ({ page }) => {
  await page.setViewportSize({ width: 375, height: 800 });
  await page.goto('/');
  const locations = page.getByRole('button', { name: 'Locations', exact: true });
  await expect(locations).toHaveAttribute('aria-expanded', 'false');
  await locations.press('Space');
  await expect(locations).toHaveAttribute('aria-expanded', 'true');
  await expect(page.getByRole('contentinfo').getByRole('link', { name: 'Toronto', exact: true })).toBeVisible();
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= document.documentElement.clientWidth)).toBe(true);
});
