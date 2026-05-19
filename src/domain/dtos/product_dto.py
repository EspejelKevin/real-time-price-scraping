from pydantic import BaseModel, Field, HttpUrl, EmailStr, ConfigDict

from ..settings import get_settings

settings = get_settings()

class ProductDTO(BaseModel):
    name: str = Field(..., min_length=3, description='Nombre descriptivo del producto')
    url: HttpUrl = Field(..., description='URL exacta del producto')
    store: str = Field(..., pattern=settings.STORE_REGEX, description='Nombre de la tienda (ej. MercadoLibre)')
    scraping_strategy: str = Field(..., pattern=settings.SCRAPING_STRATEGY_REGEX, description='Estrategia: CSS, XPath o MetaTag')
    selector: str = Field(..., description='El selector para encontrar el precio')
    target_price: float = Field(..., gt=0, description='Precio objetivo para la alerta')
    email: EmailStr = Field(..., description='Correo para recibir notificaciones')


class ProductResponse(BaseModel):
    id: int
    name: str
    url: HttpUrl
    status: str

    model_config = ConfigDict(from_attributes=True)
