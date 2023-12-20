# models.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User


engine = create_engine('sqlite:///StorageManagement.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
