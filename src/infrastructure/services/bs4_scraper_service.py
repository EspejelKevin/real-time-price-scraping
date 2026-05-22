from curl_cffi.requests import AsyncSession

from src.domain import ScraperService
from .scraping_strategies import CSSExtractionStrategy, XPathExtractionStrategy, MetaTagExtractionStrategy


class BS4ScraperService(ScraperService):
    def __init__(self) -> None:
        self.headers = {
            "Accept-Language": "es-MX,es;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0"
        }

        self.strategies = {
            'CSS': CSSExtractionStrategy(),
            'XPath': XPathExtractionStrategy(),
            'MetaTag': MetaTagExtractionStrategy()
        }

    async def get_price(self, url: str, selector: str, strategy_name: str) -> float:
        strategy = self.strategies.get(strategy_name)

        if not strategy:
            raise ValueError(f"La estrategia de scraping '{strategy_name}' no está soportada.")

        async with AsyncSession(impersonate='chrome') as session:
            response = await session.get(url, headers=self.headers, allow_redirects=True)
            response.raise_for_status()
            html_content = response.text

        return strategy.extract(html_content, selector)
