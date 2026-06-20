from pathlib import Path

import pytest
from playwright.sync_api import BrowserContext, Page
from config.config import config
from utils.logger import logger


@pytest.fixture(scope="session")
def browser_name() -> str:
    return config.browser


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args: dict) -> dict:
    return {
        **browser_context_args,
        "viewport": {"width": config.viewport_width, "height": config.viewport_height},
    }


@pytest.fixture(scope="function", autouse=True)
def tracing(context: BrowserContext, request: pytest.FixtureRequest) -> None:
    trace_dir = Path(config.report_dir) / "traces"
    trace_dir.mkdir(parents=True, exist_ok=True)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    trace_path = trace_dir / f"trace_{request.node.name.replace('/', '_')}.zip"
    context.tracing.stop(path=str(trace_path))


@pytest.fixture(scope="function")
def page(page: Page, request: pytest.FixtureRequest) -> Page:
    page.set_default_timeout(config.timeout)
    logger.info(f"Test started: {request.node.name}")
    yield page
    logger.info(f"Test finished: {request.node.name}")
