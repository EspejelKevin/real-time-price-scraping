from abc import ABC, abstractmethod


class ScraperService(ABC):
    @abstractmethod
    async def get_price(self, url: str, selector: str) -> float:
        raise NotImplementedError
