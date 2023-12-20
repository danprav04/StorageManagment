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
