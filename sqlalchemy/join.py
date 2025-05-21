from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="posts")

engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

alice = User(username='alice')
bob = User(username='bob')

session.add_all([
    Post(title='Post 1', content='Hello world', author=alice),
    Post(title='Post 2', content='Another post', author=alice),
    Post(title='Post 3', content='Bob\'s post', author=bob)
])

session.commit()

results = session.query(Post.title, User.username).join(User).all()

for title, username in results:
    print(f"'{title}' by {username}")
