from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert

from ..models.category import DbCategory
from ...schemas.category import Category

def insert(db: Session, request: Category):
    new_category = DbCategory(
        nome_categoria=request.nome_categoria,
    )

    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    

    return new_category

def get_all(db:Session):
    return db.query(DbCategory).all()