import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.test_data import TestData


class TestInventory:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page) -> None:
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.login_page.load()
        self.login_page.login(TestData.standard_user)

    def test_inventory_displayed(self) -> None:
        """TC_INV_001"""
        self.inventory_page.should_be_on_inventory_page()
        self.inventory_page.should_have_items(6)

        for i in range(6):
            self.inventory_page.should_item_details_be_visible(i)

    def test_inventory_sort_az(self) -> None:
        """TC_INV_002"""
        self.inventory_page.should_have_sort_value("az")
        self.inventory_page.should_item_have_name(0, "Sauce Labs Backpack")
        self.inventory_page.should_item_have_name(5, "Test.allTheThings() T-Shirt (Red)")

    def test_inventory_sort_za(self) -> None:
        """TC_INV_003"""
        self.inventory_page.should_have_sort_value("az")
        self.inventory_page.select_sort_option("za")
        self.inventory_page.should_have_sort_value("za")
        self.inventory_page.should_item_have_name(0, "Test.allTheThings() T-Shirt (Red)")
        self.inventory_page.should_item_have_name(5, "Sauce Labs Backpack")

    def test_inventory_sort_lohi(self) -> None:
        """TC_INV_004"""
        self.inventory_page.should_have_sort_value("az")
        self.inventory_page.select_sort_option("lohi")
        self.inventory_page.should_have_sort_value("lohi")
        self.inventory_page.should_item_have_name(0, "Sauce Labs Onesie")
        self.inventory_page.should_item_have_name(5, "Sauce Labs Fleece Jacket")

    def test_inventory_sort_hilo(self) -> None:
        """TC_INV_005"""
        self.inventory_page.should_have_sort_value("az")
        self.inventory_page.select_sort_option("hilo")
        self.inventory_page.should_have_sort_value("hilo")
        self.inventory_page.should_item_have_name(0, "Sauce Labs Fleece Jacket")
        self.inventory_page.should_item_have_name(5, "Sauce Labs Onesie")
