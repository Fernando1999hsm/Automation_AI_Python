import logging
from config.config import config


def setup_logger(name: str = "POM") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    log_dir = config.log_dir
    log_dir.mkdir(parents=True, exist_ok=True)

    fh = logging.FileHandler(log_dir / "test.log", encoding="utf-8")
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    fmt = logging.Formatter("%(asctime)s | %(levelname)-8s | %(name)s | %(message)s")
    fh.setFormatter(fmt)
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


logger = setup_logger()
