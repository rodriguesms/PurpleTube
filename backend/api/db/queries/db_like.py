import re
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert

from ..models.like import DbLike
from ...schemas.like import Like

def insert(db: Session, request: Like):
    new_like = DbLike(
        codigo_usuario = request.codigo_usuario,
        codigo_filme =  request.codigo_filme,
    )

    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    
    return new_like

def get_all(db:Session):
    return db.query(DbLike).all()