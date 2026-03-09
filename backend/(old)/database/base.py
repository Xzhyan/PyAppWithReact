from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Modelos
from app.models.user import User