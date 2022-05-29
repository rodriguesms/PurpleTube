import re
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert

from ..models.movie import DbFilme
from ...schemas.movie import Filme

def insert(db: Session, request: Filme):
    new_movie = DbFilme(
        nome_filme=request.nome_filme,
        ano=request.ano,
        descricao=request.descricao,
        duracao=request.duracao,
        baner=request.baner
    )

    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    

    return new_movie

def get_all(db:Session):
    return db.query(DbFilme).all()

