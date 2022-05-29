from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class DbDiretor(Base):
    __tablename__ = "diretor"
    codigo_diretor = Column(Integer, primary_key=True, index=True)
    nome_diretor = Column(String)

    filmes = relationship("DbFilme", secondary="direcao", back_populates="diretores")