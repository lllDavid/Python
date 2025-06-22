def create_user(session, username: str, email: str):
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    return user

def get_user_by_id(session, user_id: int):
    return session.query(User).filter(User.id == user_id).first()

def update_user_email(session, user_id: int, new_email: str):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.email = new_email
        session.commit()
    return user

def delete_user(session, user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()