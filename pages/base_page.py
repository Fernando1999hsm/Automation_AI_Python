from playwright.sync_api import Page, Locator, expect
from config.config import config
from utils.logger import logger


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.timeout = config.timeout

    def navigate(self, url: str = "") -> None:
        full_url = f"{config.base_url}{url}"
        logger.info(f"Navigating to: {full_url}")
        self.page.goto(full_url)

    def click(self, locator: Locator) -> None:
        logger.info(f"Clicking on: {locator}")
        locator.click()

    def fill(self, locator: Locator, text: str) -> None:
        logger.info(f"Filling '{text}' on: {locator}")
        locator.click()
        locator.fill(text)

    def get_text(self, locator: Locator) -> str:
        return locator.text_content() or ""
