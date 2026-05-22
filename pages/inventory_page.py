from playwright.sync_api import Page, expect
import re
from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_CONTAINER = "[data-test=\"inventory-container\"]"
    INVENTORY_ITEM = "[data-test=\"inventory-item\"]"
    ITEM_DESCRIPTION = "[data-test=\"inventory-item-description\"]"
    SHOPPING_CART_BADGE = "[data-test=\"shopping-cart-badge\"]"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def should_be_on_inventory_page(self) -> None:
        expect(self.page).to_have_url(re.compile(r".*inventory\.html"))

    def click_title(self) -> None:
        self.page.get_by_text("Swag Labs").click()

    def click_inventory_container(self) -> None:
        self.click(self.page.locator(self.INVENTORY_CONTAINER))

    def should_have_items(self, count: int) -> None:
        expect(self.page.locator(self.INVENTORY_ITEM)).to_have_count(count)

    def should_all_item_descriptions_be_visible(self) -> None:
        items = self.page.locator(self.ITEM_DESCRIPTION)
        count = items.count()
        for i in range(count):
            expect(items.nth(i)).to_be_visible()

    def should_item_images_be_visible(self, *item_ids: str) -> None:
        for item_id in item_ids:
            expect(self.page.locator(f"[data-test=\"item-{item_id}-img-link\"]")).to_be_visible()

    def should_item_descriptions_be_visible(self, count: int) -> None:
        for i in range(count):
            expect(self.page.locator(self.ITEM_DESCRIPTION).nth(i)).to_be_visible()

    def add_item_to_cart(self, item_name: str) -> None:
        self.click(self.page.locator(f"[data-test=\"add-to-cart-{item_name}\"]"))

    def should_show_cart_badge(self, expected_text: str) -> None:
        expect(self.page.locator(self.SHOPPING_CART_BADGE)).to_be_visible()
        expect(self.page.locator(self.SHOPPING_CART_BADGE)).to_contain_text(expected_text)
