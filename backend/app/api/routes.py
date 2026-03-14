from fastapi import APIRouter

# rotas
from .perms_routes import perm_router


# router da api
api_router = APIRouter()


# incluir rotas na api
api_router.include_router(perm_router)