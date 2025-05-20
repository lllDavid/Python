from sqlalchemy import create_engine, Column, Integer, DateTime, Text, String
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    username = Column(String)  
    message_text = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    read = Column(Integer, default=False)

engine = create_engine('sqlite:///chatapp.db')
Base.metadata.create_all(engine) 

Session = sessionmaker(bind=engine)
session = Session()

def send_message(username, message_text):
    message = Message(username=username, message_text=message_text)
    session.add(message)
    session.commit()




