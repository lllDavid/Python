from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)

engine = create_engine('sqlite:///chatapp.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def register_user(username):
    user = User(username=username)
    session.add(user)
    session.commit()


