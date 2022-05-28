from fastapi import APIRouter,Depends
#from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

from ..db.database import get_db
from ..db.queries import db_actor
from ..schemas.actor import Ator, AtorDisplay

router = APIRouter(
    prefix="/actor",
    tags=['Actors']
)

@router.post("",response_model=AtorDisplay)
async def insert_movie(request: Ator, db:Session = Depends(get_db)):
    return db_actor.insert(db,request)