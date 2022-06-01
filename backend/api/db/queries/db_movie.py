import re
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert



from ..models.movie import DbFilme
from ...schemas.movie import Filme
from ..models.comment import DbComment
from ..models.category import DbCategory
from ..models.actor import DbActor
from ..models.role import DbRole

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

def get_movie(db:Session,codigo_filme:int):
    return db.query(DbFilme).\
        filter(codigo_filme==DbFilme.codigo_filme).first()

def get_movie_by_category(db:Session,nome_categoria: str):
    return db.query(DbFilme).\
            join(DbFilme.categorias).\
                filter(DbCategory.nome_categoria == nome_categoria).all()

#acho que tá bugado
# def get_movie_by_name(db:Session,nome_filme: str):
#     return db.query(DbFilme).filter(DbFilme.nome_filme == nome_filme)
        


