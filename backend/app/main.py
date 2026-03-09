from fastapi import FastAPI
from app.core.middleware import setup_cors

def create_app() -> FastAPI:
    """Montagem do app e suas configs"""

    # Monta o app
    app = FastAPI(
        title="Learn FastAPI",
        version="1.0.0"
    )

    # CORSMiddleware
    setup_cors(app)
    
    # Retorna o app
    return app

app = create_app()