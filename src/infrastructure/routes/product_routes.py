from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from typing import List

from src.application import RegisterProductUseCase, GetProductUseCase, GetProductsUseCase, UpdateProductUseCase
from src.domain import ProductDTO, ProductResponse, UpdateStatusDTO

router = APIRouter(prefix='/api/v1/products', tags=['Products'])

@router.post('', response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
@inject
def register_product(request: ProductDTO,
                     usecase: RegisterProductUseCase = Depends(Provide['register_product_usecase'])):
    return usecase.execute(request)


@router.get('', response_model=List[ProductResponse], status_code=status.HTTP_200_OK)
@inject
def get_products(usecase: GetProductsUseCase = Depends(Provide['get_products_usecase'])):
    return usecase.execute()


@router.get('/{product_id}', response_model=ProductResponse, status_code=status.HTTP_200_OK)
@inject
def get_product(product_id: int,
                     usecase: GetProductUseCase = Depends(Provide['get_product_usecase'])):
    return usecase.execute(product_id) 


@router.put('/{product_id}', status_code=status.HTTP_200_OK)
@inject
def update_product(product_id: int, request: UpdateStatusDTO,
                     usecase: UpdateProductUseCase = Depends(Provide['update_product_usecase'])):
    usecase.execute(product_id, request)
    return {'message': f'product {product_id} updated with success'}
