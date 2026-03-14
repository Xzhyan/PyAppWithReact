from sqlalchemy.orm import Session

# Model
from app.models.perms import Permission

# Schema
from app.schemas.perm_schemas import PermCreate


def get_perm(db: Session):
    """Buscar as permissões no banco"""
    perms = db.query(Permission).all()
    return perms


def create(db: Session, perm_data: PermCreate):
    """Cria a permissão no banco"""
    perm = Permission(
        perm_text=perm_data.perm_text
    )

    db.add(perm)
    db.commit()
    db.refresh(perm)

    return perm
