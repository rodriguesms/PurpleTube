from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class DbComment(Base):
    __tablename__ = "comentario"
    codigo_comentario = Column(Integer, primary_key=True, index=True, autoincrement=True)
    codigo_filme = Column(ForeignKey("filme.codigo_filme"), primary_key=True)
    codigo_usuario = Column(ForeignKey("usuario.codigo_usuario"), primary_key=True)
    conteudo = Column(String)