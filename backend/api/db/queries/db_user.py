import re
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert

from ..models.user import DbUser
from ...schemas.user import User

def insert(db: Session, request: User):
    new_user = DbUser(
        nome_usuario = request.nome_usuario,
        email = request.email,
        senha = request.senha,
        imagem_usuario = request.imagem_usuario
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
   
    return new_user