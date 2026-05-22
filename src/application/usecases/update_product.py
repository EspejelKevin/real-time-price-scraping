from fastapi import status, HTTPException

from src.domain import ProductRepository, UpdateStatusDTO


class UpdateProductUseCase:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def execute(self, product_id: int, request: UpdateStatusDTO) -> None:
        existing_product = self.product_repository.get_by_id(product_id)

        if not existing_product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'product not found with id {product_id}')
        
        self.product_repository.update_status(product_id, request.status)
