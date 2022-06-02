import re
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert

from ..models.avaliation import DbAvaliation
from ...schemas.avaliation import Avaliation

def insert(db: Session, request: Avaliation):
    new_avaliation = DbAvaliation(
        codigo_usuario = request.codigo_usuario,
        codigo_filme =  request.codigo_filme,
        nota = request.nota
    )

    db.add(new_avaliation)
    db.commit()
    db.refresh(new_avaliation)
    
    return new_avaliation

def get_all(db:Session):
    return db.query(DbAvaliation).all()

def get_movie_media_avaliation(db:Session, codigo_fime: int):
    soma = 0
    n = 0
    for row in db.query(DbAvaliation).filter(DbAvaliation.codigo_filme == codigo_fime).all():
        soma += row.nota
        n+=1
    if (n == 0):
        return {"media": 0}
    return {"media": soma / n}
