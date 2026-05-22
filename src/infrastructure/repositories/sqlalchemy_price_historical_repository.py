from sqlalchemy.orm import Session

from typing import Callable
from contextlib import AbstractContextManager

from src.domain import PriceHistorical, PriceHistoricalRepository


class SQLAlchemyPriceHistoricalRepository(PriceHistoricalRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self._session_factory = session_factory
    
    def save(self, price_historical: PriceHistorical) -> PriceHistorical:
        with self._session_factory() as session:
            session.add(price_historical)
            session.flush()
            session.refresh(price_historical)
            return price_historical
