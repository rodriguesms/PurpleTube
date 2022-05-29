from pydantic import BaseModel

class Like(BaseModel):
    codigo_usuario : int
    codigo_filme:int
   
    

class LikeDisplay(BaseModel):
    codigo_usuario : int
    codigo_filme:int
    
    class Config():
        orm_mode = True