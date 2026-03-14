from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

# router dos Cargos
role_router = APIRouter(
    prefix='/roles',
    tags=['Roles']
)


@role_router.get('/')
def roles():
    """Retorna os cargos"""
    return {'message': "Cargos"}


# # Services
# from app.services import role_services

# # Schemas
# from app.schemas.role_schemas import RoleResponse, RoleCreate


# role_router = APIRouter(
#     prefix='/roles',
#     tags=['Roles']
# )


# @role_router.get('/')
# def roles(db: Session = Depends(get_db)):
#     """Retorna os cargos do sistema"""
#     return role_services.get_roles(db)


# @role_router.post('/create')
# def create(role: RoleCreate, db: Session = Depends(get_db)):
#     """Rota para criar novo role"""
#     return role_services.create_role(db, role)
