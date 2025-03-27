from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, age={self.age})>"

engine = create_engine('sqlite:///example.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_user(name, age):
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    print(f"Added user: {new_user}")

def get_all_users():
    users = session.query(User).all()
    for user in users:
        print(user)

def update_user(user_id, new_name, new_age):
    user_to_update = session.query(User).filter(User.id == user_id).first()
    if user_to_update:
        user_to_update.name = new_name
        user_to_update.age = new_age
        session.commit()
        print(f"Updated user: {user_to_update}")
    else:
        print("User not found.")

def delete_user(user_id):
    user_to_delete = session.query(User).filter(User.id == user_id).first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        print(f"Deleted user: {user_to_delete}")
    else:
        print("User not found.")

if __name__ == "__main__":
    add_user("Alice", 30)
    add_user("Bob", 25)

    print("\nAll Users:")
    get_all_users()

    update_user(1, "Alicia", 31)

    print("\nAll Users After Update:")
    get_all_users()

    delete_user(2)

    print("\nAll Users After Deletion:")
    get_all_users()
