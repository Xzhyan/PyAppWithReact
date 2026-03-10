from fastapi import FastAPI
from app.core.middleware import setup_cors
from app.api.routes import api_router

def create_app() -> FastAPI:
    """Montagem do app e suas configs"""

    # Monta o app
    app = FastAPI(
        title="Learn FastAPI",
        version="1.0.0"
    )

    # CORSMiddleware
    setup_cors(app)

    # Inclui rotas
    app.include_router(api_router)
    
    # Retorna o app
    return app

app = create_app()