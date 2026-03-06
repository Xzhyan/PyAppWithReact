from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

print(BASE_DIR)

class Settings(BaseSettings):
    DATABASE_URL: str = f'sqlite:///{BASE_DIR}/data/database.db'

settings = Settings()