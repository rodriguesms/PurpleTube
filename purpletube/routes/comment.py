from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

from ..db.database import get_db
from ..db.queries import db_comment
from .schemas import Comentario, ComentarioDisplay

router = APIRouter(
    prefix="/comments",
    tags=['Comments']
)

@router.post("",response_model=ComentarioDisplay)
async def insert_movie(request: Comentario, db:Session = Depends(get_db)):
    return db_comment.insert(db,request)