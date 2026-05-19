from fastapi import status

from src.domain import ProductRepository, UpdateStatusDTO


class UpdateProductUseCase:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def execute(self, product_id: int, request: UpdateStatusDTO) -> dict:
        result = self.product_repository.update_status(product_id, request.status)

        if not result:
            return {'message': f'product not found with id: {product_id}'}, status.HTTP_404_NOT_FOUND
        
        return {'message': f'product: {product_id} updated with success'}, status.HTTP_200_OK
