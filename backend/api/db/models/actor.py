from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base

class DbActor(Base):
    __tablename__ = "ator"
    codigo_ator = Column(Integer, primary_key=True, index=True)
    nome_ator = Column(String)
    nacionalidade = Column(String)
    imagem_ator = Column(String)
    biografia = Column(String)
    nascimento = Column(DateTime)

    filmes = relationship("DbFilme", secondary="papel", back_populates="atores")