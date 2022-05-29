from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class DbLike(Base):
    __tablename__ = "curtida"
    codigo_filme = Column(ForeignKey("filme.codigo_filme"), primary_key=True)
    codigo_usuario = Column(ForeignKey("usuario.codigo_usuario"), primary_key=True)