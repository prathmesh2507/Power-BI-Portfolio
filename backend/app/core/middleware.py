import time

from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logger import get_logger

logger = get_logger("api")


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()

        response = await call_next(request)

        duration = round(time.time() - start, 3)

        logger.info(
            "%s %s %s %ss",
            request.method,
            request.url.path,
            response.status_code,
            duration,
        )

        return response
