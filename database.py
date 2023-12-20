# models.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User


engine = create_engine('sqlite:///StorageManagement.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def one_session(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, type(Session)):
                return func(*args, **kwargs)
        session = Session()
        result = func(session, *args, **kwargs)
        session.close()
        return result
    return wrapper


@one_session
def create_user(session, username, password, email):
    try:
        new_user = User(username=username, password=password, email=email)
        session.add(new_user)
        session.commit()
        return 'success'
    except Exception as e:
        return str(e)


@one_session
def get_users(session):
    users = session.query(User).all()
    return users
