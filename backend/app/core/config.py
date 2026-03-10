from pathlib import Path
from pydantic_settings import BaseSettings

# Caminho absoluto do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    TITLE: str = "Desktop App"
    VERSION: str = "1.0.0"
    DATABASE_URL: str = f'sqlite:///{BASE_DIR}/data/database.db'

settings = Settings()