from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class DbComment(Base):
    __tablename__ = "comentario"
    codigo_comentario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo_filme = Column(ForeignKey("filme.codigo_filme"), primary_key=True)
    codigo_usuario = Column(ForeignKey("usuario.codigo_usuario"), primary_key=True)
    conteudo = Column(String)


class DbFilme(Base):
    __tablename__ = 'filme'
    codigo_filme = Column(Integer, primary_key=True, index=True)
    nome_filme = Column(String)
    ano = Column(String)
    descricao = Column(String)
    duracao = Column(String)
    baner = Column(String)

    usuarios = relationship("DbUser", secondary="comentario", back_populates="filmes")

class DbUser(Base):
    __tablename__ = 'usuario'
    codigo_usuario = Column(Integer, primary_key=True, index=True)
    nome_usuario = Column(String)
    email = Column(String)
    senha = Column(String)
    imagem_usuario = Column(String)
    
    filmes = relationship("DbFilme", secondary="comentario", back_populates="usuarios")

    



    

    