from src.domain import (ProductRepository, ScraperService,
                        PriceHistoricalRepository, PriceHistorical)


class ScrapingTaskUseCase:
    def __init__(self, product_repository: ProductRepository,
                 price_historical_repository: PriceHistoricalRepository, scraper: ScraperService) -> None:
        self.product_repository = product_repository
        self.price_historical_repository = price_historical_repository
        self.scraper = scraper

    async def execute(self, product_id: int) -> None:
        product = self.product_repository.get_by_id(product_id)

        try:
            current_price = await self.scraper.get_price(product.url, product.selector, product.scraping_strategy)
            print(f'current_price: {current_price}')

            self.price_historical_repository.save(PriceHistorical(product_id=product_id, price=current_price))

            if current_price <= product.target_price:
                print('Alerta de precio')

        except Exception as ex:
            self.product_repository.update_status(product_id, 'error_selector')
            print(f'Error scraping: {ex}')
