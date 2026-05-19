from domain import ProductRepository, ProductDTO, Product


class RegisterProductUseCase:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def execute(self, product_dto: ProductDTO) -> Product:
        product = Product(
            name=product_dto.name,
            url=product_dto.url,
            store=product_dto.store,
            scraping_strategy=product_dto.scraping_strategy,
            selector=product_dto.selector,
            target_price=product_dto.target_price,
            email=product_dto.email
        )

        return self.product_repository.save(product)
