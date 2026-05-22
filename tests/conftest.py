from pathlib import Path

import pytest
from playwright.sync_api import Page, BrowserContext, Playwright, sync_playwright
from typing import Generator
from config.config import config
from utils.logger import logger


@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser_type(playwright_instance: Playwright):
    browsers = {
        "chromium": playwright_instance.chromium,
        "firefox": playwright_instance.firefox,
        "webkit": playwright_instance.webkit,
    }
    return browsers[config.browser]


@pytest.fixture(scope="function")
def context(browser_type, request) -> Generator[BrowserContext, None, None]:
    browser = browser_type.launch(
        headless=config.headless,
        slow_mo=config.slow_mo,
    )
    context = browser.new_context(
        viewport={"width": config.viewport_width, "height": config.viewport_height},
    )
    trace_dir = Path(config.report_dir) / "traces"
    trace_dir.mkdir(parents=True, exist_ok=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield context
    trace_path = trace_dir / f"trace_{request.node.name.replace('/', '_')}.zip"
    context.tracing.stop(path=str(trace_path))
    context.close()
    browser.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Generator[Page, None, None]:
    page = context.new_page()
    page.set_default_timeout(config.timeout)
    logger.info(f"Test started")
    yield page
    logger.info(f"Test finished")
    page.close()
