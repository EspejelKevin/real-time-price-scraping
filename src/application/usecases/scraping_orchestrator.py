import asyncio

from .get_products import GetProductsUseCase
from .scraping_task import ScrapingTaskUseCase


class ScrapingOrchestrator:
    def __init__(self, get_products: GetProductsUseCase, scraping_task: ScrapingTaskUseCase) -> None:
        self.get_products = get_products
        self.scraping_task = scraping_task

    async def execute(self) -> None:
        active_products = self.get_products.execute()

        if not active_products:
            return
        
        tasks = [
            self.scraping_task.execute(product.id)
            for product in active_products
        ]

        await asyncio.gather(*tasks, return_exceptions=True)
