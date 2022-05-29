import re
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert

from ..models.diretor import DbDiretor 
from ...schemas.director import Diretor

def insert(db: Session, request: Diretor):
    new_diretor = DbDiretor(
        nome_diretor = request.nome_diretor
    )

    db.add(new_diretor)
    db.commit()
    db.refresh(new_diretor)
    
    return new_diretor

def get_all(db:Session):
    return db.query(DbDiretor).all()