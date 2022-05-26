import fastapi
from typing import Optional, List
from pydantic import BaseModel

router = fastapi.APIRouter()

class Comentario(BaseModel):
    codigo_comentario : int
    codigo_usuario : int
    codigo_fime : int
    conteudo : str


comentarios = []

@router.get("/comentarios",tags=["Comentarios"], response_model=List[Comentario])
async def get_comentarios():
    return comentarios

@router.post("/comentarios", tags=["Comentarios"])
def create_comentario(comentario: Comentario):
    comentarios.append(comentario)
    return "Success"

@router.get("/comentarios/{id}", tags=["Comentarios"])
async def get_comentario(id: int):
    return comentarios[id]