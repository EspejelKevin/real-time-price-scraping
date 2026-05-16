from dependency_injector import containers, providers

from infrastructure import DatabaseConnection, SQLAlchemyProductRepository
from domain import Settings


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

    
