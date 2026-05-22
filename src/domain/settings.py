from pydantic_settings import BaseSettings

from functools import lru_cache


class Settings(BaseSettings):
    DB_URL: str
    ECHO: bool = False

    STORE_REGEX: str
    SCRAPING_STRATEGY_REGEX: str
    PRODUCT_STATUS_REGEX: str
    USER_AGENT: str
    INTERVAL_TIME: int = 1
    JOB_ID: str = 'price_scraping_job'
    JOB_NAME: str = 'Scrapea los precios de los productos activos'


@lru_cache
def get_settings() -> Settings:
    return Settings()
