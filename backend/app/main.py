from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import setup_logging
from app.core.logger import get_logger
from app.core.middleware import RequestLoggingMiddleware

setup_logging()

logger = get_logger(__name__)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.add_middleware(RequestLoggingMiddleware)


@app.on_event("startup")
async def startup():
    logger.info("GIIP Backend Started")


@app.on_event("shutdown")
async def shutdown():
    logger.info("GIIP Backend Stopped")


@app.get("/")
async def root():
    logger.info("Root endpoint accessed")

    return {
        "application": settings.APP_NAME,
        "status": "running",
    }


@app.get("/health")
async def health():
    logger.info("Health endpoint checked")

    return {
        "status": "healthy",
    }
