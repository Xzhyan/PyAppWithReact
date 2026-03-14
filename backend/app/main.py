from fastapi import FastAPI
from app.database import Base, engine
from app.core import settings, setup_cors

# models
from app.models.perms import Permission
from app.models.role import Role
from app.models.user import User
from app.models.auth_token import AuthToken

# router da api
from app.api.routes import api_router


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

    # incluindo router da api ao app
    app.include_router(api_router)

    return app

app = create_app()
