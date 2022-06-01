from fastapi import APIRouter,Depends
#from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from typing import List

from ..db.database import get_db
from ..db.queries import db_like
from ..schemas.like import Like, LikeDisplay, LikeQntDisplay

router = APIRouter(
    prefix="/likes",
    tags=['Like']
)

@router.post("",response_model=LikeDisplay)
async def insert_comment(request: Like, db:Session = Depends(get_db)):
    return db_like.insert(db,request)

@router.get("/all", response_model=List[LikeDisplay])
def get_comments(db:Session=Depends(get_db)):
    return db_like.get_all(db)

@router.get("/movie_likes/{codigo_filme}",response_model=LikeQntDisplay)
def get_movie_likes(codigo_filme:int, db:Session=Depends(get_db)):
    return db_like.get_movie_likes(db,codigo_filme)