from datetime import date
from pydantic import BaseModel

class Comentario(BaseModel):
    codigo_usuario : int
    codigo_filme:int
    conteudo: str
    

class ComentarioDisplay(BaseModel):
    
    data:date
    nome_usuario:str
    conteudo: str
    class Config():
        orm_mode = True

class ComentarioDisplayPost(BaseModel):
    codigo_usuario:int
    codigo_filme: int
    date: str
    conteudo: str
    class Config():
        orm_mode = True
