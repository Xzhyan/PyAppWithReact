from fastapi import FastAPI
from app.core.middleware import register_middleware
from app.api.routes import router
from app.database.session import engine
from app.database.base import Base

def create_app() -> FastAPI:
    app = FastAPI()

    register_middleware(app)
    
    app.include_router(router)
  
    return app

app = create_app()