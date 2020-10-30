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


#users = session.query(User)
#for user in users:
#    print(user.name)



users = session.query(User).order_by(User.name)
for user in users:
    print(user.name)
    print(type(user.name))
