from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class DbRole(Base):
    __tablename__ = "papel"
    codigo_ator = Column(ForeignKey("ator.codigo_ator"), primary_key=True)
    codigo_filme = Column(ForeignKey("filme.codigo_filme"), primary_key=True)
    
    