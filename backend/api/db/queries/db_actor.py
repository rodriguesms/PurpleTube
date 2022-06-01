import re
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert

from ..models.actor import DbActor
from ..models.movie import DbFilme
from ...schemas.actor import Ator

def insert(db: Session, request: Ator):
    new_actor = DbActor(
        nome_ator = request.nome_ator,
        nacionalidade = request.nacionalidade,
        imagem_ator = request.imagem_ator,
        biografia = request.biografia,
        nascimento = request.nascimento
    )

    db.add(new_actor)
    db.commit()
    db.refresh(new_actor)
    
    return new_actor

def get_all(db:Session):
    return db.query(DbActor).all()


def get_movie_actors(db:Session,codigo_filme:int):
    return db.query(DbActor).\
        join(DbActor.filmes).\
            filter(DbFilme.codigo_filme == codigo_filme).all()
