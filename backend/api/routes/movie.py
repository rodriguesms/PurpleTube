from typing import List
from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

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

@router.get("/movie_id/{codigo_filme}",response_model=FilmeDisplay)
def get_movie(codigo_filme:int,db:Session=Depends(get_db)):
    return db_movie.get_movie(db,codigo_filme)

@router.get("/movie_category/{nome_categoria}",response_model=List[FilmeDisplay])
def get_movie_by_category(nome_categoria:str, db:Session=Depends(get_db)):
    return db_movie.get_movie_by_category(db, nome_categoria)

#acho que tá bugado
@router.get("/movie_name/{nome_filme}",response_model=List[FilmeDisplay])
def get_movie_by_name(nome_filme:str, db:Session=Depends(get_db)):
    return db_movie.get_movie_by_name(db, nome_filme)
