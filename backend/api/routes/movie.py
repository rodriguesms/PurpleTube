from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from typing import List

from ..db.database import get_db
from ..db.queries import db_movie
from ..schemas.movie import Filme, FilmeDisplay

router = APIRouter(
    prefix="/movies",
    tags=['Movie']
)

@router.post("",response_model=FilmeDisplay)
def insert_movie(request: Filme, db:Session = Depends(get_db)):
    return db_movie.insert(db,request)

@router.get("/all",response_model=List[FilmeDisplay])
def get_movies(db:Session=Depends(get_db)):
    return db_movie.get_all(db)