from dependency_injector import containers, providers

from src.infrastructure import DatabaseConnection, SQLAlchemyProductRepository
from src.application import RegisterProductUseCase, GetProductUseCase, GetProductsUseCase, UpdateProductUseCase
from src.domain import Settings


class Container(containers.DeclarativeContainer):
    settings = providers.Singleton(Settings)

    db_connection = providers.Singleton(
        DatabaseConnection,
        db_url=settings.provided.DB_URL,
        echo=settings.provided.ECHO
    )

    db_session = providers.Factory(
        lambda conn: conn.session(),
        conn=db_connection
    )

    product_repository = providers.Factory(
        SQLAlchemyProductRepository,
        session_factory=db_session.provider
    )

    register_product_usecase = providers.Factory(
        RegisterProductUseCase,
        product_repository=product_repository
    )

    get_products_usecase = providers.Factory(
        GetProductsUseCase,
        product_repository=product_repository
    )

    get_product_usecase = providers.Factory(
        GetProductUseCase,
        product_repository=product_repository
    )

    update_product_usecase = providers.Factory(
        UpdateProductUseCase,
        product_repository=product_repository
    )
