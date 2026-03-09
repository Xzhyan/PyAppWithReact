from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    """Configuração de middleware de CORS para a api"""

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],  # * permite todos os tipos de metodos
        allow_headers=["*"],  # * permite todos os headers
    )
