from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base
from ..models import movie_category
from ..models import role
from ..models import direction

class DbFilme(Base):
    __tablename__ = 'filme'
    codigo_filme = Column(Integer, primary_key=True, index=True)
    nome_filme = Column(String)
    ano = Column(String)
    descricao = Column(String)
    duracao = Column(String)
    baner = Column(String)

    usuarios = relationship("DbUser", secondary="comentario", back_populates="filmes")
    categorias = relationship("DbCategory", secondary="filme_categoria", back_populates="filmes")
    atores = relationship("DbActor", secondary="papel", back_populates="filmes")
    diretores = relationship("DbDiretor", secondary="direcao", back_populates="filmes")
