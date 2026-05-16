from pydantic_settings import BaseSettings

from functools import lru_cache


class Settings(BaseSettings):
    DB_URL: str
    ECHO: bool = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
