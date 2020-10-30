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

#RETRIEVE ALL USERS
def get_users():
    userlist = session.query(User).order_by(User.name)
    session.close()
    return userlist

#INSERT DATA
def insert_user(username):
    session.add(User(name=username))
    session.commit()
    session.close()