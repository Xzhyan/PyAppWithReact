from fastapi import APIRouter

router = APIRouter()

# Rota de teste
@router.get("/home")
def home():
    return {'message': "Olá mundo!"}

@router.post("/user/register")
def user_register():
    return 