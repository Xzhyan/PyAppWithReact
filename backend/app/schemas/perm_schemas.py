from pydantic import BaseModel
from typing import Optional


class PermCreate(BaseModel):
    """Valida a criação da permissão"""
    perm_text: str


class PermResponse(BaseModel):
    """Valida o retorno da permissão"""
    id: int
    perm_text: str

    class Config:
        from_attributes = True
