from sqlalchemy import create_engine, Column, Integer, String
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
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        raise ValueError(f"Username '{username}' is already taken.")
    
    user = User(username=username)
    session.add(user)
    session.commit()



