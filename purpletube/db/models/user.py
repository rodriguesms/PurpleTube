from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class DbUser(Base):
    __tablename__ = 'usuario'
    codigo_usuario = Column(Integer, primary_key=True, index=True)
    nome_usuario = Column(String)
    email = Column(String)
    senha = Column(String)
    imagem_usuario = Column(String)
    
    filmes = relationship("DbFilme", secondary="comentario", back_populates="usuarios")