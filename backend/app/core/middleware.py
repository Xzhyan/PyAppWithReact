from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    """Configuração de CORSMiddleware da api"""

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['http://localhost:5173'], # autoriza o react
        allow_credentials=True,
        allow_methods=['*'], # autoriza todos os metodos
        allow_headers=['*'] # autoriza todos os cabeçalhos
    )