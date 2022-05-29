from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class DbMovieCategory(Base):
    __tablename__ = "filme_categoria"
    codigo_categoria = Column(ForeignKey("categoria.codigo_categoria"), primary_key=True)
    codigo_filme = Column(ForeignKey("filme.codigo_filme"), primary_key=True)
    