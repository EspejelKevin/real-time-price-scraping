from abc import ABC, abstractmethod
from typing import List, Optional

from ..models.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product) -> Product:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, product_id: int) -> Optional[Product]:
        raise NotImplementedError
    
    @abstractmethod
    def get_all_active(self) -> List[Product]:
        raise NotImplementedError
    
    @abstractmethod
    def update_status(self, product_id: int, status: str) -> None:
        raise NotImplementedError
