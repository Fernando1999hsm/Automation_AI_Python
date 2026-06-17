from playwright.sync_api import Page, expect


def test_inventory_displayed(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    expect(page.locator("[data-test=\"product-sort-container\"]")).to_have_value("az")
    page.locator("[data-test=\"product-sort-container\"]").select_option("hilo")
    expect(page.locator("[data-test=\"product-sort-container\"]")).to_have_value("hilo")
    
    items = page.locator("[data-test=\"inventory-item\"]")

    item0 = items.nth(0)
    expect(item0.locator("[data-test=\"inventory-item-name\"]")).to_have_text("Sauce Labs Fleece Jacket")

    item0 = items.nth(5)
    expect(item0.locator("[data-test=\"inventory-item-name\"]")).to_have_text("Sauce Labs Onesie")