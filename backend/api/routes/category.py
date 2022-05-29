from fastapi import APIRouter,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session
from typing import List

from ..db.database import get_db
from ..db.queries import db_category
from ..schemas.category import Category, CategoryDisplay

router = APIRouter(
    prefix="/categories",
    tags=['Category']
)

@router.post("",response_model=CategoryDisplay)
def insert_category(request: Category, db:Session = Depends(get_db)):
    return db_category.insert(db,request)

@router.get("/all",response_model=List[CategoryDisplay])
def get_categories(db:Session=Depends(get_db)):
    return db_category.get_all(db)