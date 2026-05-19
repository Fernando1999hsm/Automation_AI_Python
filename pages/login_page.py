from playwright.sync_api import Page, expect
import re
from pages.base_page import BasePage
from data.test_data import User


class LoginPage(BasePage):
    USERNAME_INPUT = "[data-test=\"username\"]"
    PASSWORD_INPUT = "[data-test=\"password\"]"
    LOGIN_BUTTON = "[data-test=\"login-button\"]"
    ERROR_MESSAGE = "[data-test=\"error\"]"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def load(self) -> None:
        self.navigate("/")

    def login(self, user: User) -> None:
        self.fill(self.page.locator(self.USERNAME_INPUT), user.username)
        self.fill(self.page.locator(self.PASSWORD_INPUT), user.password)
        self.click(self.page.locator(self.LOGIN_BUTTON))

    def login_with_credentials(self, username: str, password: str) -> None:
        self.fill(self.page.locator(self.USERNAME_INPUT), username)
        self.fill(self.page.locator(self.PASSWORD_INPUT), password)
        self.click(self.page.locator(self.LOGIN_BUTTON))

    def click_login(self) -> None:
        self.click(self.page.locator(self.LOGIN_BUTTON))

    def should_show_inputs(self) -> None:
        expect(self.page.locator(self.USERNAME_INPUT)).to_be_visible()
        expect(self.page.locator(self.PASSWORD_INPUT)).to_be_visible()

    def should_show_error(self, expected_text: str) -> None:
        expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible()
        expect(self.page.locator(self.ERROR_MESSAGE)).to_contain_text(expected_text)

    def should_not_be_on_inventory(self) -> None:
        expect(self.page).not_to_have_url(re.compile(r".*inventory\.html"))
