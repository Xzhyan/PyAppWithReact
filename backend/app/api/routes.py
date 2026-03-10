from fastapi import APIRouter

# Import de rotas
from .role_routes import role_router
from .user_routes import user_router

api_router = APIRouter()

# Rotas de Usuário
api_router.include_router(role_router)
api_router.include_router(user_router)