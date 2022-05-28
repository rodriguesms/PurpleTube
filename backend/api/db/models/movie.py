from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class DbFilme(Base):
    __tablename__ = 'filme'
    codigo_filme = Column(Integer, primary_key=True, index=True)
    nome_filme = Column(String)
    ano = Column(String)
    descricao = Column(String)
    duracao = Column(String)
    baner = Column(String)

    usuarios = relationship("DbUser", secondary="comentario", back_populates="filmes")
