from datetime import date
from pydantic import BaseModel

class Ator(BaseModel):
    nome_ator: str
    nacionalidade: str
    imagem_ator: str
    biografia: str
    nascimento: date
    

class AtorDisplay(BaseModel):
    codigo_ator: int
    nome_ator: str
    nacionalidade: str
    imagem_ator: str
    biografia: str
    nascimento: date
    class Config():
        orm_mode = True