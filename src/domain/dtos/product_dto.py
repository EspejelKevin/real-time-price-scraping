from pydantic import BaseModel


class ProductDTO(BaseModel):
    name: str
    url: str
    store: str
    scraping_strategy: str
    selector: str
    target_price: float
    email: str
