# from sqlalchemy import Integer, String, ForeignKey, Column
# from sqlalchemy.orm import relationship

# from ..db_setup import Base

# class Filme(Base):
#     __tablename__ = "filme"

#     codigo_filme = Column(Integer, pimary_key=True, index=True, nullable=False)
#     nome_filme = Column(String(100), index=True)
#     ano = Column(String(4), index=True)
#     descricao = Column(String(500), index=True)
#     duracao = Column(String(16), index=True)
#     baner = Column(String(100), index=True)

from ..db_setup import banana
print("ahhhh")
banana()