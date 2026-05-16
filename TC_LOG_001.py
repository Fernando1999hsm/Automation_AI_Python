import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url(re.compile(r".*inventory\.html"))
    page.get_by_text("Swag Labs").click()
    page.locator("[data-test=\"inventory-container\"]").click()
    expect(page.locator("[data-test=\"inventory-item-description\"]").first).to_be_visible()
    expect(page.locator("[data-test=\"inventory-item-description\"]").nth(1)).to_be_visible()
    expect(page.locator("[data-test=\"inventory-item-description\"]").nth(2)).to_be_visible()
    expect(page.locator("[data-test=\"inventory-item-description\"]").nth(3)).to_be_visible()
    expect(page.locator("[data-test=\"inventory-item-description\"]").nth(4)).to_be_visible()
    expect(page.locator("[data-test=\"inventory-item-description\"]").nth(5)).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
