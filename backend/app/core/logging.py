import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from app.core.config import settings

LOG_DIR = Path(settings.LOG_DIRECTORY)
LOG_DIR.mkdir(parents=True, exist_ok=True)

LOG_FORMAT = (
    "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
)


def _create_handler(filename: str):
    handler = RotatingFileHandler(
        LOG_DIR / filename,
        maxBytes=5 * 1024 * 1024,   # 5 MB
        backupCount=5,
        encoding="utf-8",
    )

    handler.setFormatter(logging.Formatter(LOG_FORMAT))

    return handler


def setup_logging():
    root = logging.getLogger()

    root.setLevel(settings.LOG_LEVEL)

    root.handlers.clear()

    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter(LOG_FORMAT))

    root.addHandler(console)

    root.addHandler(_create_handler("application.log"))
