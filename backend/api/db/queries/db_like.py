import re
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert

from ..models.like import DbLike
from ...schemas.like import Like
from ..models.movie import DbFilme

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

def get_movie_likes(db:Session, codigo_fime: int):
    qnt = 0
    for _ in db.query(DbLike).filter(DbLike.codigo_filme == codigo_fime).all():
        qnt+=1
    return {"qnt_likes": qnt}