from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

# Schema
from app.schemas.perm_schemas import PermCreate

# Service
from app.services import perm_services

# router das Permissões
perm_router = APIRouter(
    prefix='/perms',
    tags=['Permissões']
)


@perm_router.get('/')
def perms(db: Session = Depends(get_db)):
    """Retorna as permissões"""
    return perm_services.get_perm(db)


@perm_router.post('/create')
def create_perms(perm: PermCreate, db: Session = Depends(get_db)):
    return perm_services.create(db, perm)

