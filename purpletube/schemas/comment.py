from pydantic import BaseModel

class Comentario(BaseModel):
    codigo_usuario : int
    codigo_filme:int
    conteudo: str
    

class ComentarioDisplay(BaseModel):
    codigo_comentario: int
    codigo_usuario : int
    codigo_filme:int
    conteudo: str
    class Config():
        orm_mode = True