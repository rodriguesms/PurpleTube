from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from typing import List

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

@router.get("/all", response_model=List[UserDisplay])
def get_users(db:Session=Depends(get_db)):
    return db_user.get_all(db)

@router.delete("/remove/{codigo_usuario}", response_model= UserDisplay)
def delete_user(codigo_usuario:int, db:Session=Depends(get_db)):
    return db_user.delete_user_by_codigo(db, codigo_usuario)