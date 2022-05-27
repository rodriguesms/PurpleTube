from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

from ..db.database import get_db
from ..db.queries import db_movie
from .schemas import Filme, FilmeDisplay

router = APIRouter(
    prefix="/movies",
    tags=['Movie']
)

@router.post("",response_model=FilmeDisplay)
def insert_movie(request: Filme, db:Session = Depends(get_db)):
    return db_movie.insert(db,request)