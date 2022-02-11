from datetime import datetime


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session

from sqlalchemy.ext.declarative import declarative_base




from app.config import DATABASE_URL


Base = declarative_base()



def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session



class User(Base):
    __tablename__='user'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    register_date = Column(String, default=datetime.utcnow())
    
    
    
    
