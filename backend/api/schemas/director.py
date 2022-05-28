from pydantic import BaseModel

class Diretor(BaseModel):
    nome_diretor: str
    
class DiretorDisplay(BaseModel):
    codigo_diretor:int
    nome_diretor: str
    
    class Config():
        orm_mode = True