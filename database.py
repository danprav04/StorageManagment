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
            if isinstance(arg, Session):
                return func(*args, **kwargs)
        session = Session()
        result = func(session, *args, **kwargs)
        session.close()
        return result
    return wrapper


@one_session
def create_user(session, username, password, email):
    new_user = User(username=username, password=password, email=email)
    session.add(new_user)
    session.commit()
