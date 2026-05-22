from fastapi import FastAPI

from contextlib import asynccontextmanager

from src.container import Container
from src.infrastructure import product_routes, DatabaseConnection, APSchedulerAdapter
from src.domain import Base


container = Container()
settings = container.settings()

scheduler_adapter = APSchedulerAdapter(container, settings)

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_conn: DatabaseConnection = container.db_connection()
    Base.metadata.create_all(db_conn._engine)

    scheduler_adapter.start()

    yield

    scheduler_adapter.stop()


def create_app() -> FastAPI:
    container.wire(modules=[product_routes])

    app = FastAPI(title='Real-Time Price Scraping API', lifespan=lifespan)
    app.container = container
    app.include_router(product_routes.router)

    @app.get('/health', tags=['HealthCheck'])
    def health_check():
        return {'status': 'service is up'}
    
    return app

app = create_app()
