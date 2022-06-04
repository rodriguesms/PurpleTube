from pydantic import BaseModel

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

class UserLogin(BaseModel):
    email: str
    senha: str

