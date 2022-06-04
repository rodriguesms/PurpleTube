from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 
SQLALCHEMY_DATABASE_URL = 'postgresql://agthfdmeglgyxj:ffd90989b990ac15cda7fb9665ffa5d52b0c6fe3d13bac4098c1f93282c66ce5@ec2-52-3-200-138.compute-1.amazonaws.com:5432/dcd643nqdo3g58'
#SQLALCHEMY_DATABASE_URL = 'postgresql://kxhptwkc:frYTKlDzj1obbD1N4LiVWFBGiH8sFp-Y@hattie.db.elephantsql.com/kxhptwkc'
 
engine = create_engine(SQLALCHEMY_DATABASE_URL)
 
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
 
Base = declarative_base()
 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()