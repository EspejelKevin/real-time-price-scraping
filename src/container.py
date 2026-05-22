from dependency_injector import containers, providers

from src.infrastructure import (DatabaseConnection,
                                SQLAlchemyProductRepository, 
                                BS4ScraperService, 
                                PlayWrightScraper, 
                                SQLAlchemyPriceHistoricalRepository)
from src.application import (RegisterProductUseCase,
                             GetProductUseCase, 
                             GetProductsUseCase, 
                             UpdateProductUseCase,
                             ScrapingTaskUseCase,
                             ScrapingOrchestrator)
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

    price_historical_repository = providers.Factory(
        SQLAlchemyPriceHistoricalRepository,
        session_factory=db_session.provider
    )

    scraper_service_bs4 = providers.Factory(
        BS4ScraperService
    )

    scraper_service_playwright = providers.Factory(
        PlayWrightScraper,
        settings=settings
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

    scraping_task = providers.Factory(
        ScrapingTaskUseCase,
        product_repository=product_repository,
        price_historical_repository=price_historical_repository,
        scraper=scraper_service_playwright
    )

    scraping_orchestrator = providers.Factory(
        ScrapingOrchestrator,
        get_products=get_products_usecase,
        scraping_task=scraping_task
    )
