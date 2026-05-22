from abc import ABC, abstractmethod

from ..models.price_historical import PriceHistorical


class PriceHistoricalRepository(ABC):
    @abstractmethod
    def save(self, price_historical: PriceHistorical) -> PriceHistorical:
        raise NotImplementedError
