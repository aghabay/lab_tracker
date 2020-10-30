from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///db.db', echo=True)
session = sessionmaker(bind=engine)
session = session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)


#INSERT DATA
user1 = User(name="Ali", fullname="Mahammadali", nickname="Ali")
session.add(user1)
session.commit()
