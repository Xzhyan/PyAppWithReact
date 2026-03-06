from fastapi import APIRouter

router = APIRouter()

@router.get("/home")
def home():
    return {'message': "Olá mundo!"}

@router.post("/user/register")
def user_register():
    return