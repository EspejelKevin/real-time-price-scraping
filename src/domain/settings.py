from pydantic_settings import BaseSettings

from functools import lru_cache


class Settings(BaseSettings):
    DB_URL: str
    ECHO: bool = False

    STORE_REGEX: str
    SCRAPING_STRATEGY_REGEX: str


@lru_cache
def get_settings() -> Settings:
    return Settings()
