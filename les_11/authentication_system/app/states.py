from enum import Enum


class States(Enum):
    authenticated = 'Authenticated'
    logged_out = 'Logged out'


class UserState:
    state = States.logged_out
    current_user = None
