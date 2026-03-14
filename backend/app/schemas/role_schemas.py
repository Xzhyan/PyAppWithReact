# from pydantic import BaseModel, Field
# from typing import Optional, List

# # permission schema
# from app.schemas.permission_schemas import PermissionResponse


# class RoleBase(BaseModel):
#     name: str


# class RoleCreate(RoleBase):
#     permissions: Optional[List[int]] = None


# class RoleUpdate(RoleBase):
#     name: Optional[str] = None
#     permissions: Optional[List[int]] = None


# class RoleResponse(RoleBase):
#     id: int
#     permissions: List[PermissionResponse] = Field(default_factory=list)

#     class Config:
#         from_attributes = True