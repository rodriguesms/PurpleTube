from fastapi import APIRouter,Depends
#from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from typing import List

from ..db.database import get_db
from ..db.queries import db_comment
from ..schemas.comment import Comentario, ComentarioDisplay

router = APIRouter(
    prefix="/comments",
    tags=['Comments']
)

@router.post("",response_model=ComentarioDisplay)
async def insert_comment(request: Comentario, db:Session = Depends(get_db)):
    return db_comment.insert(db,request)

@router.get("/all", response_model=List[ComentarioDisplay])
def get_comments(db:Session=Depends(get_db)):
    return db_comment.get_all(db)

@router.get("/movie_comments/{codigo_filme}", response_model=List[ComentarioDisplay])
def get_movie_comments(codigo_filme:int, db:Session=Depends(get_db)):
    return  db_comment.get_movie_comments(db,codigo_filme)
