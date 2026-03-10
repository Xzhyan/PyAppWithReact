from fastapi import FastAPI

# Base e engine
from app.database import Base, engine

# Config e CORS
from app.core import settings, setup_cors

# Routes
from app.api.routes import api_router

# Modelos
from app.models.role import Role
from app.models.user import User

def create_app() -> FastAPI:
    """Factory function da api"""

    app = FastAPI(
        title = settings.TITLE,
        version = settings.VERSION
    )

    @app.on_event('startup')
    def create_tables():
        """Cria as tabelas do banco de dados quando a api iniciar"""
        Base.metadata.create_all(bind=engine)

    # CORSMiddleware
    setup_cors(app)

    # Rotas
    app.include_router(api_router)

    return app

app = create_app()
