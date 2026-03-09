from fastapi import FastAPI

def create_app() -> FastAPI:
    """Montagem do app e suas configs"""

    app = FastAPI(
        title="Learn FastAPI",
        version="1.0.0"
    )

    return app

app = create_app()