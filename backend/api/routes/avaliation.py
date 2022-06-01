from fastapi import APIRouter,Depends
#from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from typing import List

from ..db.database import get_db
from ..db.queries import db_avaliation
from ..schemas.avaliation import Avaliation, AvaliationDisplay, AvaliationMediaDisplay

router = APIRouter(
    prefix="/avaliations",
    tags=['Avaliations']
)

@router.post("",response_model=AvaliationDisplay)
async def insert_avaliation(request: Avaliation, db:Session = Depends(get_db)):
    return db_avaliation.insert(db,request)

@router.get("/all", response_model=List[AvaliationDisplay])
def get_avaliations(db:Session=Depends(get_db)):
    return db_avaliation.get_all(db)

@router.get("/movie_media_avaliation/{codigo_filme}", response_model=AvaliationMediaDisplay)
def get_movie_avaliations(codigo_filme:int, db:Session=Depends(get_db)):
    return db_avaliation.get_movie_media_avaliation(db,codigo_filme)

