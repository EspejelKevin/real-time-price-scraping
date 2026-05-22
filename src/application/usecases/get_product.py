from fastapi import status, HTTPException

from src.domain import ProductRepository, Product, ProductResponse


class GetProductUseCase:
    def __init__(self, product_repository: ProductRepository) -> ProductResponse:
        self.product_repository = product_repository

    def execute(self, product_id: int) -> Product:
        product = self.product_repository.get_by_id(product_id)

        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'product not found with id {product_id}')
        
        return ProductResponse(
            id=product.id,
            name=product.name,
            url=product.url,
            status=product.status)
