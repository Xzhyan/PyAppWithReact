from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

# pra resolver o alerta do Pylance, sobre a tipagem
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .perms import Permission
    from .user import User


# Tabela de associação das permissões com os cargos
role_perms = Table(
    'role_perms',
    Base.metadata,
    Column('role_id', ForeignKey('roles.id'), primary_key=True),
    Column('perm_id', ForeignKey('perms.id'), primary_key=True)
)


class Role(Base):
    __tablename__ = 'roles'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    perms: Mapped[list['Permission']] = relationship(
        secondary=role_perms,
        back_populates='roles'
    )

    users: Mapped[list['User']] = relationship(
        'User',
        back_populates='role'
    )
