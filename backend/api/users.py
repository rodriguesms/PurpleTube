import fastapi
from typing import Optional, List
from pydantic import BaseModel

router = fastapi.APIRouter()

class User(BaseModel):
    codigo_usuario : int
    nome_usuario: str
    email: str
    imagem_usuario: str


users = []

@router.get("/users",tags=["Users"], response_model=List[User])
async def get_users():
    return users

@router.post("/users", tags=["Users"])
def create_user(user: User):
    users.append(user)
    return "Success"

@router.get("/users/{id}", tags=["Users"])
async def get_user(id: int):
    return users[id]