import re
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert
from ..db.models import DbFilme
from ..routers.schemas import Filme


def insert(db: Session, request: Filme):
    new_post = DbFilme(
        nome_filme=request.nome_filme,
        ano=request.ano,
        descricao=request.descricao,
        duracao=request.duracao,
        baner=request.baner
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
