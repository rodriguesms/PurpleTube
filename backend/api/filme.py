import fastapi
from typing import Optional, List
from pydantic import BaseModel

router = fastapi.APIRouter()

class Filme(BaseModel):
    codigo_filme : int
    nome_filme: str
    ano: str
    descricao: str
    duracao: str
    baner: str

filmes = []

@router.get("/filmes", tags=["Filmes"], response_model=List[Filme])
async def get_filmes():
    return filmes

@router.post("/filmes", tags=["Filmes"])
def create_filmes(filme: Filme):
    filmes.append(filme)
    return "Success"

@router.get("/filmes/{id}", tags=["Filmes"])
async def get_filme(id: int):
    return filme[id]