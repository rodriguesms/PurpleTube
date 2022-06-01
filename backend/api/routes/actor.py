from fastapi import APIRouter,Depends
#from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from typing import List


from ..db.database import get_db
from ..db.queries import db_actor
from ..schemas.actor import Ator, AtorDisplay

router = APIRouter(
    prefix="/actor",
    tags=['Actors']
)

@router.post("", response_model=AtorDisplay)
async def insert_actor(request: Ator, db:Session = Depends(get_db)):
    return db_actor.insert(db,request)

@router.get("/all", response_model=List[AtorDisplay])
async def get_actors(db:Session=Depends(get_db)):
    return db_actor.get_all(db)

@router.get("/movie_actors/{codigo_filme}", response_model=List[AtorDisplay])
def get_movie_actors(codigo_filme:int, db:Session=Depends(get_db)):
    return db_actor.get_movie_actors(db,codigo_filme)