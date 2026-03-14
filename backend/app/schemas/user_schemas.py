# from pydantic import BaseModel
# from typing import Optional


# class UserBase(BaseModel):
#     """Base do schema de usuario"""
#     username: str


# class UserCreate(UserBase):
#     """Criar novo usuario"""
#     password: str
#     role_id: int


# class UserUpdate(BaseModel):
#     """Atualizar usuario"""
#     username: Optional[str] = None
#     password: Optional[str] = None


# class UserResponde(UserBase):
#     """Retornar usuário"""
#     id: int
#     role_id: int
#     is_active: bool

#     class Config:
#         from_attributes = True