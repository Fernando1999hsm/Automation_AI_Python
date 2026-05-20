import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from data.test_data import TestData

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page) -> None:
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.login_page.load()

    def test_standard_user_login_and_inventory_visible(self) -> None:
        """TC_LOG_001"""
        self.login_page.login(TestData.standard_user)
        self.inventory_page.should_be_on_inventory_page()
        self.inventory_page.click_title()
        self.inventory_page.click_inventory_container()
        self.inventory_page.should_all_item_descriptions_be_visible()

    def test_problem_user_login_and_add_to_cart(self) -> None:
        """TC_LOG_002"""
        self.login_page.login(TestData.problem_user)
        self.inventory_page.should_be_on_inventory_page()
        self.inventory_page.should_item_images_be_visible("4", "0", "1", "5")
        self.inventory_page.should_item_descriptions_be_visible(4)
        self.inventory_page.add_item_to_cart("sauce-labs-bike-light")
        self.inventory_page.should_show_cart_badge("1")

    def test_login_invalid_credentials(self) -> None:
        """TC_LOG_006"""
        self.login_page.login(TestData.invalid_user)
        self.login_page.should_show_error(
            "Epic sadface: Username and password do not match any user in this service"
        )
        self.login_page.should_not_be_on_inventory()

    def test_login_wrong_password(self) -> None:
        """TC_LOG_007"""
        self.login_page.login_with_credentials("standard_user", "wrong_password")
        self.login_page.should_show_error(
            "Epic sadface: Username and password do not match any user in this service"
        )
        self.login_page.should_not_be_on_inventory()

    def test_login_empty_fields(self) -> None:
        """TC_LOG_008"""
        self.login_page.should_show_inputs()
        self.login_page.click_login()
        self.login_page.should_show_error("Epic sadface: Username is required")
        self.login_page.should_not_be_on_inventory()
