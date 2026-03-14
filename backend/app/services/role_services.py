# from sqlalchemy.orm import Session

# # Models
# from app.models.role import Role
# from app.models.permission import Permission

# # Schemas
# from app.schemas.role_schemas import RoleCreate


# def get_roles(db: Session):
#     """Retorna os cargos"""
#     roles = db.query(Role).all()
#     return roles


# def create_role(db: Session, role_data: RoleCreate):
#     """Cria novo cargo"""
#     role = Role(
#         name=role_data.name
#     )

#     # Adicionar várias permissões
#     if role_data.permissions:
#         permissions = db.query(Permission).filter(
#             Permission.id.in_(role_data.permissions)
#         ).all()

#         role.permissions = permissions

#     db.add(role)
#     db.commit()
#     db.refresh(role)

#     return role