from app.database import Base
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=True
    )

    password: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=True
    )

    role_id: Mapped[int] = mapped_column(
        ForeignKey('roles.id')
    )

    role = relationship('Role', back_populates='users')

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
