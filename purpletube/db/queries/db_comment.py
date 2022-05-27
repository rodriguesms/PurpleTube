import re
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert

from ..models import DbComment
from ...routes.schemas import Comentario

def insert(db: Session, request: Comentario):
    new_comment = DbComment(
        codigo_usuario = request.codigo_usuario,
        codigo_filme =  request.codigo_filme,
        conteudo = request.conteudo
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    
    return new_comment
