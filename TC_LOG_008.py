import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    expect(page.locator("[data-test=\"username\"]")).to_be_visible()
    expect(page.locator("[data-test=\"password\"]")).to_be_visible()
    page.locator("[data-test=\"login-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username is required")
    expect(page).not_to_have_url(re.compile(r".*inventory\.html"))

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
    