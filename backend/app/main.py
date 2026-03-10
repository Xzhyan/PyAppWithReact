from fastapi import FastAPI

# Config e CORS
from app.core import settings, setup_cors


def create_app() -> FastAPI:
    app = FastAPI(
        title = settings.TITLE,
        version = settings.VERSION
    )

    # Inclui CORSMiddleware
    setup_cors(app)

    return app

app = create_app()
