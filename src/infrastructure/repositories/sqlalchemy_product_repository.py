from sqlalchemy import select
from sqlalchemy.orm import Session

from typing import Callable, List, Optional
from contextlib import AbstractContextManager

from domain import Product, ProductRepository


class SQLAlchemyProductRepository(ProductRepository):
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self._session_factory = session_factory
    
    def save(self, product: Product) -> Product:
        with self._session_factory() as session:
            session.add(product)
            session.refresh(product)
            return product
    
    def get_by_id(self, product_id: int) -> Optional[Product]:
        with self._session_factory() as session:
            return session.get(Product, product_id)
    
    def get_all_active(self) -> List[Product]:
        with self._session_factory() as session:
            statement = select(Product).where(Product.status == 'activo')
            result = session.execute(statement)
            return list(result.scalars().all())

    def update_status(self, product_id: int, status: str) -> None:
        with self._session_factory() as session:
            product = session.get(Product, product_id)
            if product:
                product.status = status
