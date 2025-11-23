from fastapi import FastAPI, Request
from tortoise.contrib.fastapi import register_tortoise
import os
import logging
import sys
from app.api import ping, summaries, version
from app.db import init_db

# Configure logging - only show warnings and errors by default
logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

# Set specific loggers to INFO for important operations
logging.getLogger("app").setLevel(logging.INFO)
logging.getLogger("app.summarizer").setLevel(logging.INFO)
logging.getLogger("app.api.summaries").setLevel(logging.INFO)

logger = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()

    # Only log errors in requests
    @application.middleware("http")
    async def log_errors(request: Request, call_next):
        try:
            response = await call_next(request)
            if response.status_code >= 500:
                logger.error(f"Server error: {request.method} {request.url.path} - Status: {response.status_code}")
            return response
        except Exception as e:
            logger.error(f"Request failed: {request.method} {request.url.path} - {str(e)}", exc_info=True)
            raise

    db_url = os.environ.get("DATABASE_URL")
    if db_url:
        register_tortoise(
            application,
            db_url=db_url,
            modules={"models": ["app.models.tortoise"]},
            generate_schemas=True,
            add_exception_handlers=True,
        )
    else:
        logger.warning("DATABASE_URL not set, database features disabled")

    application.include_router(ping.router)
    application.include_router(version.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )
    
    return application


kek = create_application()

init_db(kek)
