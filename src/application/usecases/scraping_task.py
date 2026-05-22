from src.domain import ProductRepository, ScraperService


class ScrapingTaskUseCase:
    def __init__(self, product_repository: ProductRepository, scraper: ScraperService) -> None:
        self.product_repository = product_repository
        self.scraper = scraper

    async def execute(self, product_id: int) -> None:
        product = self.product_repository.get_by_id(product_id)

        try:
            current_price = await self.scraper.get_price(product.url, product.selector)

            if current_price <= product.target_price:
                print('Alerta de precio')
        except Exception as ex:
            self.product_repository.update_status(product_id, 'error_selector')
            print(f'Error scraping: {ex}')
