from playwright.sync_api import Page, expect


def test_inventory_displayed(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    expect(page.locator("[data-test=\"inventory-container\"]")).to_be_visible()

    items = page.locator("[data-test=\"inventory-item\"]")
    expect(items).to_have_count(6)

    item0 = items.nth(0)
    expect(item0.locator("[data-test=\"item-4-img-link\"]")).to_be_visible()
    expect(item0.locator("[data-test=\"inventory-item-name\"]")).to_be_visible()
    expect(item0.locator("[data-test=\"inventory-item-desc\"]")).to_be_visible()
    expect(item0.locator("[data-test=\"inventory-item-price\"]")).to_be_visible()
    expect(item0.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_be_visible()

    item1 = items.nth(1)
    expect(item1.locator("[data-test=\"item-0-img-link\"]")).to_be_visible()
    expect(item1.locator("[data-test=\"inventory-item-name\"]")).to_be_visible()
    expect(item1.locator("[data-test=\"inventory-item-desc\"]")).to_be_visible()
    expect(item1.locator("[data-test=\"inventory-item-price\"]")).to_be_visible()
    expect(item1.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")).to_be_visible()

    item2 = items.nth(2)
    expect(item2.locator("[data-test=\"item-1-img-link\"]")).to_be_visible()
    expect(item2.locator("[data-test=\"inventory-item-name\"]")).to_be_visible()
    expect(item2.locator("[data-test=\"inventory-item-desc\"]")).to_be_visible()
    expect(item2.locator("[data-test=\"inventory-item-price\"]")).to_be_visible()
    expect(item2.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")).to_be_visible()

    item3 = items.nth(3)
    expect(item3.locator("[data-test=\"item-5-img-link\"]")).to_be_visible()
    expect(item3.locator("[data-test=\"inventory-item-name\"]")).to_be_visible()
    expect(item3.locator("[data-test=\"inventory-item-desc\"]")).to_be_visible()
    expect(item3.locator("[data-test=\"inventory-item-price\"]")).to_be_visible()
    expect(item3.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")).to_be_visible()

    item4 = items.nth(4)
    expect(item4.locator("[data-test=\"item-2-img-link\"]")).to_be_visible()
    expect(item4.locator("[data-test=\"inventory-item-name\"]")).to_be_visible()
    expect(item4.locator("[data-test=\"inventory-item-desc\"]")).to_be_visible()
    expect(item4.locator("[data-test=\"inventory-item-price\"]")).to_be_visible()
    expect(item4.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]")).to_be_visible()

    item5 = items.nth(5)
    expect(item5.locator("[data-test=\"item-3-img-link\"]")).to_be_visible()
    expect(item5.locator("[data-test=\"inventory-item-name\"]")).to_be_visible()
    expect(item5.locator("[data-test=\"inventory-item-desc\"]")).to_be_visible()
    expect(item5.locator("[data-test=\"inventory-item-price\"]")).to_be_visible()
    expect(item5.locator("[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]")).to_be_visible()
