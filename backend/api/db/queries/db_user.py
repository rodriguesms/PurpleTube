import re
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import insert

from ..models.user import DbUser
from ...schemas.user import User, UserLogin

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

def get_all(db:Session):
    return db.query(DbUser).all()

def get_by_id(db:Session, codigo_usuario: int):
    return db.query(DbUser).filter(codigo_usuario==DbUser.codigo_usuario).one()

def delete_user_by_codigo(db:Session,codigo_usuario:int):
    user = db.query(DbUser).filter(codigo_usuario== DbUser.codigo_usuario).one()
    db.delete(user)
    db.commit()
    return user


def login_user(db:Session,request: UserLogin):
    user = db.query(DbUser).filter(request.email == DbUser.email).first()
    return user
