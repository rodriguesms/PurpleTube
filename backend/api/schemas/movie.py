from pydantic import BaseModel

class Filme(BaseModel):
    nome_filme: str
    ano: str
    descricao: str
    duracao: str
    baner: str

class FilmeDisplay(BaseModel):
    codigo_filme:int
    nome_filme: str
    ano: str
    descricao: str
    duracao: str
    baner: str
    class Config():
        orm_mode = True