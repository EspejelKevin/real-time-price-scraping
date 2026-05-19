from fastapi import FastAPI

from src.container import Container
from src.infrastructure import product_routes, DatabaseConnection
from src.domain import Base

def create_app() -> FastAPI:
    container = Container()
    container.wire(modules=[product_routes])

    app = FastAPI(title='Real-Time Price Scraping API')
    app.container = container
    app.include_router(product_routes.router)

    db_conn: DatabaseConnection = container.db_connection()
    Base.metadata.create_all(db_conn._engine)

    @app.get('/health', tags=['HealthCheck'])
    def health_check():
        return {'status': 'service is up'}
    
    return app

app = create_app()
