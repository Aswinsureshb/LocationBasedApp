from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "mysql+pymysql://root:password@localhost/LocationBasedSocialApp"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit= False, bind=engine)

Base = declarative_base()

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()