from sqlalchemy.orm import Session

# Modelo
from app.models.role import Role


def get_roles(db: Session):
    roles = db.query(Role).all()

    return roles