from pydantic import BaseModel

class Category(BaseModel):
    nome_categoria: str
    
class CategoryDisplay(BaseModel):
    codigo_categoria: int
    nome_categoria: str
    class Config():
        orm_mode = True