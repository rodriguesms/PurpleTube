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

class User(BaseModel):
    nome_usuario: str
    email: str
    senha: str
    imagem_usuario: str

class UserDisplay(BaseModel):
    codigo_usuario : int
    nome_usuario: str
    imagem_usuario: str
    class Config():
        orm_mode = True

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