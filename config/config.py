from pathlib import Path
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    base_url: str = "https://www.saucedemo.com"
    headless: bool = False
    browser: str = "chromium"
    slow_mo: int = 0
    timeout: int = 30000
    viewport_width: int = 1280
    viewport_height: int = 720
    report_dir: Path = Path("reports")
    log_dir: Path = Path("logs")

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


config = Config()
