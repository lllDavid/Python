from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from user import User
from datetime import datetime

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    message_text = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    read = Column(Integer, default=False)

engine = create_engine('sqlite:///chatapp.db')
Base.metadata.create_all(engine) 

Session = sessionmaker(bind=engine)
session = Session()

def send_message(message_text):
    message = Message(message_text=message_text)
    session.add(message)
    session.commit()


