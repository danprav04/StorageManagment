def users_to_dict(users):
    user_list = []
    for user in users:
        user_dict = {
            'id': user.id,
            'username': user.username,
            'password': user.password,
            'email': user.email
        }
        user_list.append(user_dict)
    return user_list


def storage_places_to_dict(storage_places):
    storage_places_list = []

    for storage_place in storage_places:
        storage_place_dict = {
            'id': storage_place.id,
            'name': storage_place.name,
            'description': storage_place.description,
            'image': storage_place.image,
        }
        storage_places_list.append(storage_place_dict)

    return storage_places_list


def storage_grids_to_dict(storage_grids):
    storage_grids_list = []

    for storage_grid in storage_grids:
        storage_grid_dict = {
            'id': storage_grid.id,
            'name': storage_grid.name,
            'description': storage_grid.description,
            'row_count': storage_grid.row_count,
            'column_count': storage_grid.column_count,
            'image': storage_grid.image,
            'storage_place_id': storage_grid.storage_place_id,
        }
        storage_grids_list.append(storage_grid_dict)

    return storage_grids_list


def storage_units_to_dict(storage_units):
    storage_units_list = []

    for storage_unit in storage_units:
        storage_unit_dict = {
            'id': storage_unit.id,
            'name': storage_unit.name,
            'description': storage_unit.description,
            'image': storage_unit.image,
            'storage_place_id': storage_unit.storage_place_id,
            'storage_grid_id': storage_unit.storage_grid_id,
            'storage_grid_row': storage_unit.storage_grid_row,
            'storage_grid_column': storage_unit.storage_grid_column,
        }
        storage_units_list.append(storage_unit_dict)

    return storage_units_list
