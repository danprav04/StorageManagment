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
