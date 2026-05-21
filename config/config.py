from dataclasses import dataclass, field
from pathlib import Path
from os.path import join, dirname
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=join(dirname(__file__), "..", ".env"))


@dataclass
class Config:
    base_url: str = os.getenv("BASE_URL", "https://www.saucedemo.com")
    headless: bool = os.getenv("HEADLESS", "false").lower() == "true"
    browser: str = os.getenv("BROWSER", "chromium")
    slow_mo: int = int(os.getenv("SLOW_MO", "0"))
    timeout: int = int(os.getenv("TIMEOUT", "30000"))
    viewport_width: int = int(os.getenv("VIEWPORT_WIDTH", "1280"))
    viewport_height: int = int(os.getenv("VIEWPORT_HEIGHT", "720"))
    report_dir: Path = field(default_factory=lambda: Path(__file__).parent.parent / "reports")
    log_dir: Path = field(default_factory=lambda: Path(__file__).parent.parent / "logs")


config = Config()
