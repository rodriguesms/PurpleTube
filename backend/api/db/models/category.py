from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class DbCategory(Base):
    __tablename__ = 'categoria'
    codigo_categoria = Column(Integer, primary_key=True, index=True)
    nome_categoria = Column(String)
    
    filmes = relationship("DbFilme", secondary="filme_categoria", back_populates="categorias")