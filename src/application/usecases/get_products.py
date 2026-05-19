from typing import List

from src.domain import ProductRepository, Product


class GetProductsUseCase:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def execute(self) -> List[Product]:
        return self.product_repository.get_all_active()
