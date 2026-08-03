import logging
from pathlib import Path

from app.core.config import settings


def setup_logging():
    log_dir = Path(settings.LOG_DIRECTORY)
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / "application.log"

    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(),
        ],
    )
