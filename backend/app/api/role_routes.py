from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.role_schemas import RoleResponse
from app.services import role_services

role_router = APIRouter(
    prefix='/roles',
    tags=['Roles']
)

@role_router.get('/')
def roles(db: Session = Depends(get_db)):
    return role_services.get_roles(db)