from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Project Root (GIIP)
BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    # Application
    APP_NAME: str
    APP_VERSION: str
    APP_ENV: str
    DEBUG: bool

    # Server
    HOST: str
    PORT: int

    # Database
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    DB_POOL_SIZE: int
    DB_MAX_OVERFLOW: int
    DB_POOL_RECYCLE: int
    DB_POOL_PRE_PING: bool

    # Pipeline
    ROLLING_MONTHS: int
    BATCH_SIZE: int
    MAX_RETRIES: int
    REQUEST_TIMEOUT: int

    # Scheduler
    SCHEDULER_HOUR: int
    SCHEDULER_MINUTE: int

    # Logging
    LOG_LEVEL: str
    LOG_DIRECTORY: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        case_sensitive=True,
        extra="ignore",
    )

    @property
    def DATABASE_URL(self):
        return (
            f"mysql+pymysql://"
            f"{self.DATABASE_USER}:{self.DATABASE_PASSWORD}"
            f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}"
            f"/{self.DATABASE_NAME}"
        )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
