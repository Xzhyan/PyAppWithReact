from sqlalchemy.orm import Session

# Models
from app.models.role import Role

# Schemas
from app.schemas.role_schemas import RoleCreate


def get_roles(db: Session):
    roles = db.query(Role).all()

    return roles

def create_role(db: Session, role_data: RoleCreate):
    """Cria novo cargo"""
    role = Role(
        name=role_data.name
    )

    db.add(role)
    db.commit()
    db.refresh(role)

    return role