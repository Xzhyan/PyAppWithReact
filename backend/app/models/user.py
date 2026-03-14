from app.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# pra resolver o alerta do Pylance, sobre a tipagem
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .role import Role
    from .auth_token import AuthToken


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    role_id: Mapped[int] = mapped_column(
        ForeignKey('roles.id')
    )

    role: Mapped['Role'] = relationship(
        back_populates='users'
    )

    token: Mapped['AuthToken'] = relationship(
        back_populates='user',
        uselist=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
