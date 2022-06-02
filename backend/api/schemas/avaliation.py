from typing import Optional
from pydantic import BaseModel

class Avaliation(BaseModel):
    codigo_usuario : int
    codigo_filme:int
    nota: int
    
class AvaliationDisplay(BaseModel):
    codigo_usuario : int
    codigo_filme: int
    nota: int
    class Config():
        orm_mode = True

class AvaliationMediaDisplay(BaseModel):
    media :Optional[str]
    class Config():
        orm_mode = True