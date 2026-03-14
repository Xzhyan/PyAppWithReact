from app.database import Base
from datetime import datetime
from sqlalchemy import Table, Column, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

# pra resolver o alerta do Pylance, sobre a tipagem
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User


class AuthToken(Base):
    __tablename__ = 'tokens'

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        unique=True
    )

    user: Mapped['User'] = relationship(
        back_populates='token'
    )

    token: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    expires_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )
