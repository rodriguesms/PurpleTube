from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 
# postgresql://agthfdmeglgyxj:ffd90989b990ac15cda7fb9665ffa5d52b0c6fe3d13bac4098c1f93282c66ce5@ec2-52-3-200-138.compute-1.amazonaws.com:5432/dcd643nqdo3g58
SQLALCHEMY_DATABASE_URL = 'postgresql://kxhptwkc:33TCa5934Nf2ybUY4nZ_E7zGh99LcM_0@hattie.db.elephantsql.com:5432/kxhptwkc'
 
engine = create_engine(SQLALCHEMY_DATABASE_URL)
 
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
 
Base = declarative_base()
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()