from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class DbAvaliation(Base):
    __tablename__ = "avaliacao"
    codigo_filme = Column(ForeignKey("filme.codigo_filme"), primary_key=True)
    codigo_usuario = Column(ForeignKey("usuario.codigo_usuario"), primary_key=True)
    nota = Column(Integer)