from datetime import datetime
from pydantic import BaseModel

class Ator(BaseModel):
    nome_ator: str
    nacionalidade: str
    imagem_ator: str
    biografia: str
    nascimento: datetime
    

class AtorDisplay(BaseModel):
    codigo_ator: int
    nome_ator: str
    nacionalidade: str
    imagem_ator: str
    biografia: str
    nascimento: datetime
    class Config():
        orm_mode = True