from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

from ..db.database import get_db
from ..db import db_movie
from .schemas import Filme, FilmeDisplay


router = APIRouter(
    prefix='/movie',
    tags=['movie']
)

@router.post('/',response_model=FilmeDisplay)
def insert_movie(request: Filme, db:Session = Depends(get_db)):
    return db_movie.insert(db,request)