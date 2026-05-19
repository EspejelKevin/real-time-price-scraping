from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from dependency_injector.wiring import inject, Provide

from typing import List

from src.application import RegisterProductUseCase, GetProductUseCase, GetProductsUseCase
from src.domain import ProductDTO, ProductResponse

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

@router.get('/{product_id}')
@inject
def get_product(product_id: int,
                     usecase: GetProductUseCase = Depends(Provide['get_product_usecase'])):
    response, status_code = usecase.execute(product_id)
    return JSONResponse(jsonable_encoder(response), status_code=status_code) 
