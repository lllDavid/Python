from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///mydatabase.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name='Alice', age=25)
session.add(new_user)
session.commit()

alice = session.query(User).filter_by(name='Alice').first()
print(f"User: {alice.name}, Age: {alice.age}")

alice.age = 26
session.commit()

session.delete(alice)
session.commit()

session.close()
