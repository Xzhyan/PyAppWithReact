from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

# Tabela de associação de permissões e cargos
from .role import role_perms

# pra resolver o alerta do Pylance, sobre a tipagem
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .role import Role


class Permission(Base):
    __tablename__ = 'perms'

    id: Mapped[int] = mapped_column(primary_key=True)

    perm_text: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    roles: Mapped[list['Role']] = relationship(
        secondary=role_perms,
        back_populates='perms'
    )
