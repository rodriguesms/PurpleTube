# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgres+pyscopg2://agthfdmeglgyxj:ffd90989b990ac15cda7fb9665ffa5d52b0c6fe3d13bac4098c1f93282c66ce5@ec2-52-3-200-138.compute-1.amazonaws.com:5432/dcd643nqdo3g58"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
# )
# SessionLocal = sessionmaker(
#     autocommit=False, autoflush=False, bind=engine, future=True
# )

# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


def banana():
    print("banana")

