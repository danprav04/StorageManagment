# models.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, StoragePlace, StorageGrid, StorageUnit


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


@one_session
def get_user_by_id(session, user_id):
    user = session.query(User).filter_by(id=user_id).first()
    return user


@one_session
def delete_user_by_id(session, user_id):
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return 'success'
    else:
        return 'User not found'


# StoragePlace functions

@one_session
def create_storage_place(session, name, description, image):
    try:
        new_storage_place = StoragePlace(name=name, description=description, image=image)
        session.add(new_storage_place)
        session.commit()
        return 'success'
    except Exception as e:
        return str(e)


@one_session
def get_storage_places(session):
    storage_places = session.query(StoragePlace).all()
    return storage_places


@one_session
def get_storage_place_by_id(session, storage_place_id):
    storage_place = session.query(StoragePlace).filter_by(id=storage_place_id).first()
    return storage_place


@one_session
def delete_storage_place_by_id(session, storage_place_id):
    storage_place = session.query(StoragePlace).filter_by(id=storage_place_id).first()
    if storage_place:
        session.delete(storage_place)
        session.commit()
        return 'success'
    else:
        return 'Storage Place not found'


# StorageGrid functions

@one_session
def create_storage_grid(session, name, description, row_count, column_count, image, storage_place_id):
    storage_place = session.query(StoragePlace).filter_by(id=storage_place_id).first()

    if storage_place:
        new_storage_grid = StorageGrid(name=name,
                                       description=description,
                                       row_count=row_count,
                                       column_count=column_count,
                                       image=image,
                                       storage_place_id=storage_place_id)
        session.add(new_storage_grid)
        session.commit()
        return 'success'
    else:
        return f"Storage Place '{storage_place_id}' not found."


@one_session
def get_storage_grids(session):
    storage_grids = session.query(StorageGrid).all()
    return storage_grids


@one_session
def get_storage_grid_by_id(session, storage_grid_id):
    storage_grid = session.query(StorageGrid).filter_by(id=storage_grid_id).first()
    return storage_grid


@one_session
def delete_storage_grid_by_id(session, storage_grid_id):
    storage_grid = session.query(StorageGrid).filter_by(id=storage_grid_id).first()
    if storage_grid:
        session.delete(storage_grid)
        session.commit()
        return 'success'
    else:
        return 'Storage Grid not found'


# StorageUnit functions

@one_session
def create_storage_unit(session, name, description, image, storage_place_id, storage_grid_id, storage_grid_row, storage_grid_column):
    storage_place = session.query(StoragePlace).filter_by(id=storage_place_id).first()

    if storage_place:
        storage_grid = storage_place.storage_grids.filter_by(id=storage_grid_id).first()

        if storage_grid.row_count < storage_grid_row or storage_grid.column_count < storage_grid_column or storage_grid_row < 0 or storage_grid_column < 0:
            return "Storage grid row or column are not valid."

        if storage_grid:
            new_storage_unit = StorageUnit(
                name=name,
                description=description,
                image=image,
                storage_grid=storage_grid,
                storage_place_id=storage_place_id,
                storage_grid_id=storage_grid_id,
                storage_grid_row=storage_grid_row,
                storage_grid_column=storage_grid_column,
            )
            session.add(new_storage_unit)
            session.commit()
            return 'success'
        else:
            return f"No storage grid found for {storage_grid_id}."
    else:
        return f"Storage Place '{storage_place_id}' not found."


@one_session
def get_storage_units(session):
    storage_units = session.query(StorageUnit).all()
    return storage_units


@one_session
def get_storage_unit_by_id(session, storage_unit_id):
    storage_unit = session.query(StorageUnit).filter_by(id=storage_unit_id).first()
    return storage_unit


@one_session
def delete_storage_unit_by_id(session, storage_unit_id):
    storage_unit = session.query(StorageUnit).filter_by(id=storage_unit_id).first()
    if storage_unit:
        session.delete(storage_unit)
        session.commit()
        return 'success'
    else:
        return 'Storage Unit not found'


def print_storage():
    storage_places = Session().query(StoragePlace).all()
    for storage_place in storage_places:
        print(
            f"Storage Place ID: {storage_place.id}, Name: {storage_place.name}, Description: {storage_place.description}, Image: {storage_place.image}")

        print("Associated Storage Grids:")
        for storage_grid in storage_place.storage_grids:
            print(
                f"  - Grid ID: {storage_grid.id}, Row Count: {storage_grid.row_count}, Column Count: {storage_grid.column_count}, Description: {storage_grid.description}, Image: {storage_grid.image}")

            print("  Associated Storage Units:")
            for storage_unit in storage_grid.storage_units:
                print(
                    f"    - Unit ID: {storage_unit.id}, Name: {storage_unit.name}, Description: {storage_unit.description}, Image: {storage_unit.image}, "
                    f"Row: {storage_unit.storage_grid_row}, Column: {storage_unit.storage_grid_column}")
            print('\n' * 1)
        print('\n' * 2)
    print('\n'*3)
