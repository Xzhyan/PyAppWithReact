from pathlib import Path
from pydantic_settings import BaseSettings

# Caminho absoluto do projeto, pra configurar o caminho do banco de dados
BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    DATABASE_URL: str = f'sqlite:///{BASE_DIR}/data/database.db'

settings = Settings()