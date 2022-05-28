from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

from ..db.database import get_db
from ..db.queries import db_user
from ..schemas.user import User, UserDisplay

router = APIRouter(
    prefix="/users",
    tags=['User']
)

@router.post("", response_model= UserDisplay)
def insert_user(request: User, db:Session = Depends(get_db)):
    return db_user.insert(db,request)