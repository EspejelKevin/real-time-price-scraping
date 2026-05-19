from fastapi import status

from typing import Optional

from src.domain import ProductRepository, Product, ProductResponse


class GetProductUseCase:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def execute(self, product_id: int) -> Optional[Product]:
        product = self.product_repository.get_by_id(product_id)

        if not product:
            return {'message': f'product not found with id: {product_id}'}, status.HTTP_404_NOT_FOUND
        
        return ProductResponse(
            id=product.id,
            name=product.name,
            url=product.url,
            status=product.status), status.HTTP_200_OK
