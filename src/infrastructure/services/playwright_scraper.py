from playwright.async_api import async_playwright
from playwright_stealth import Stealth

from src.domain import ScraperService, Settings
from .scraping_strategies import CSSExtractionStrategy, XPathExtractionStrategy, MetaTagExtractionStrategy


class PlayWrightScraper(ScraperService):
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.stealth = Stealth()
        self.strategies = {
            'CSS': CSSExtractionStrategy(),
            'XPath': XPathExtractionStrategy(),
            'MetaTag': MetaTagExtractionStrategy()
        }

    async def get_price(self, url: str, selector: str, strategy_name: str) -> float:
        strategy = self.strategies.get(strategy_name)

        if not strategy:
            raise ValueError(f"La estrategia de scraping '{strategy_name}' no está soportada.")
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent=self.settings.USER_AGENT
            )

            page = await context.new_page()
            await self.stealth.apply_stealth_async(page)

            await page.goto(url, wait_until='networkidle')

            html_content = await page.content()

            await browser.close()

        return strategy.extract(html_content, selector)
