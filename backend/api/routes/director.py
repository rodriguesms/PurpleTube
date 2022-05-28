from fastapi import APIRouter,Depends
#from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

from ..db.database import get_db
from ..db.queries import db_director
from ..schemas.director import Diretor, DiretorDisplay

router = APIRouter(
    prefix="/directors",
    tags=['Director']
)

@router.post("",response_model=DiretorDisplay)
async def insert_movie(request: Diretor, db:Session = Depends(get_db)):
    return db_director.insert(db,request)