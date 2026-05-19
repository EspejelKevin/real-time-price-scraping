from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from src.application import RegisterProductUseCase
from src.domain import ProductDTO, ProductResponse

router = APIRouter(prefix='/api/v1/products', tags=['Products'])

@router.post('/', response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
@inject
def register_product(request: ProductDTO,
                     usecase: RegisterProductUseCase = Depends(Provide['register_product_usecase'])):
    return usecase.execute(request)
