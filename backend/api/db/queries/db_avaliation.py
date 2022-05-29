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
        conteudo = request.conteudo
    )

    db.add(new_avaliation)
    db.commit()
    db.refresh(new_avaliation)
    
    return new_avaliation

def get_all(db:Session):
    return db.query(DbAvaliation).all()