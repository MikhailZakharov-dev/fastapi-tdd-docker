import logging
from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import AnyUrl

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = bool(0)
    database_url: AnyUrl = None  # pyright: ignore[reportAssignmentType]


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the enviroment...")
    return Settings()
