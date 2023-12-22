from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    email = Column(String, unique=True)


class StoragePlace(Base):
    __tablename__ = 'storage_places'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    image = Column(String)

    storage_grids = relationship("StorageGrid", backref="storage_place", lazy="dynamic")
    storage_units = relationship("StorageUnit", backref="storage_place", lazy="dynamic")


class StorageGrid(Base):
    __tablename__ = 'storage_grids'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    row_count = Column(Integer, nullable=False)
    column_count = Column(Integer, nullable=False)
    image = Column(String)
    storage_place_id = Column(Integer, ForeignKey('storage_places.id'))

    storage_units = relationship("StorageUnit", backref="storage_grid", lazy="dynamic")


class StorageUnit(Base):
    __tablename__ = 'storage_units'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    image = Column(String)
    storage_place_id = Column(Integer, ForeignKey('storage_places.id'))
    storage_grid_id = Column(Integer, ForeignKey('storage_grids.id'))
    storage_grid_row = Column(Integer, nullable=False)
    storage_grid_column = Column(Integer, nullable=False)
