from bs4 import BeautifulSoup
import httpx

from src.domain import ScraperService, Settings


class BS4ScraperService(ScraperService):
    def __init__(self, settings: Settings) -> None:
        self.headers = {
            'User-Agent': settings.USER_AGENT
        }

    async def get_price(self, url: str, selector: str) -> float:
        async with httpx.AsyncClient(headers=self.headers, follow_redirects=True) as client:
            response = await client.get(url)
            response.raise_for_status()

            beautiful_soup = BeautifulSoup(response.text, 'html.parser')
            element = beautiful_soup.select_one(selector)

            if not element:
                raise ValueError(f'Price not found with selector: {selector}')
            
            print('element: ', element.text)

            price_text = element.text.replace('$', '').replace(',', '').strip()
            return float(price_text)
