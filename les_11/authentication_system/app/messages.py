from enum import Enum


class Messages(Enum):
    success = 'Success!'
    welcome = 'Hey! Welcome to the system!'
    user_already_exists = 'User with this loging already exists!'
    error_auth = 'Password or login is wrong!'
    unidentified_operation = 'Unidentified operation selected!'
    enter_login_password = 'Enter your Login and password separated by a space: '
    enter_new_age = 'Enter new age: '
