from datetime import datetime
from sqlalchemy import desc
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert

from ..models.user import DbUser
from ..models.comment import DbComment
from ...schemas.comment import Comentario

def insert(db: Session, request: Comentario):
    new_comment = DbComment(
        codigo_usuario = request.codigo_usuario,
        data=datetime.now().strftime("%m/%d/%Y"),
        codigo_filme =  request.codigo_filme,
        conteudo = request.conteudo

    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    
    return new_comment

def get_all(db:Session):
    return db.query(DbComment.data,DbUser.nome_usuario,DbComment.conteudo)\
            .join(DbUser,DbUser.codigo_usuario==DbComment.codigo_usuario)\
            .order_by(desc(DbComment.data)).all()

def get_movie_comments(db:Session,codigo_filme:int):
    return db.query(DbComment.data,DbUser.nome_usuario,DbComment.conteudo)\
            .join(DbUser,DbUser.codigo_usuario==DbComment.codigo_usuario)\
            .filter(DbComment.codigo_filme==codigo_filme).all()