from fastapi import FastAPI
from backend.app.core.middleware import register_middleware
from backend.app.api.routes import router
from backend.app.database.session import engine
from backend.app.database.base import Base
import backend.app.models

def create_app() -> FastAPI:
    app = FastAPI()

    register_middleware(app)
    app.include_router(router)

    Base.metadata.create_all(bind=engine)

    return app

app = create_app()