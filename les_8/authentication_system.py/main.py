from typing import Dict, List, Optional
import json


FILE_NAME = 'users.json'


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def save(self):
        data = _get_data_from_file()
        data.append({self.login: self.password})
        with open(FILE_NAME, 'w') as json_file:
            json.dump(data, json_file)


def _get_data_from_file():
    with open(FILE_NAME, 'r') as json_file:
        data = json_file.read()
        return [] if not data else json.loads(data)


def _get_users_from_file():
    data = _get_data_from_file()
    result = []

    for el in data:
        for login, password in el.items():
            user = User(login, password)
            result.append(user)

    return result

    # wrong
    # with open(FILE_NAME, 'r') as json_file:
    #     return list(map(lambda x: User(list(x.keys())[0], x[list(x.keys())[0]]), json.load(json_file)))


def get_user_by_login(login, users=None) -> Optional[User, None]:
    if not users:
        users = _get_users_from_file()

    for user in users:
        if user.login == login:
            return user


def get_login():
    return input('Enter login')


def get_password():
    return input('Enter password')


def authenticate():
    login, password = get_login(), get_password()
    user = get_user_by_login(login)
    if not user:
        return 'User not found'

    return f'Welcome {user.login}' if user.password == password else 'Your password is wrong'


def sign_up():
    login, password = get_login(), get_password()
    if get_user_by_login(login):
        return 'User already exists'

    user = User(login, password)
    user.save()
    return 'Congratulations! Now you can authenticate!'


def update():
    pass


while True:
    activity = input('Enter su to sign up, au to authenticate or sm else to exit')

    menu = {
        'su': sign_up,
        'au': authenticate,
        'up': update,
    }

    do = menu.get(activity)
    if not do:
        break

    print(do())
