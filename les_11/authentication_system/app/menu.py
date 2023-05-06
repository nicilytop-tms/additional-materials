import sys

from les_11.authentication_system.app.states import States
from les_11.authentication_system.auth_service.auth import AuthService, SignUpService, SignOutService, UserService
from les_11.authentication_system.app.messages import Messages
from les_11.authentication_system.exceptions.app_exceptions import UnidentifiedOperationSelected


class MenuService:
    @classmethod
    def execute(cls, state, action):
        try:
            MENUS_BY_STATE[state][action]['action']()
        except KeyError:
            raise UnidentifiedOperationSelected

    @classmethod
    def show_menu_by_state(cls, state):
        for name_action, action in MENUS_BY_STATE[state].items():
            print(action["description"])


_MENU_LOGGED_OUT = {
    'WM': {
        'action': None,
        'description': Messages.welcome.value
    },
    'AU': {
        'action': AuthService.auth,
        'description': '1. input AU to authenticate'
    },
    'SU': {
        'action': SignUpService.sign_up,
        'description': '2. input SU to sign up'
    },
    'EX': {
        'action': sys.exit,
        'description': '3. input EX to exit'
    }
}

_MENU_AUTHENTICATED = {
    'UDA': {
        'action': UserService.update_user_age,
        'description': '1. input UDA to update user age',
    },
    'LO': {
        'action': SignOutService.logout,
        'description': '2. input LO to logout'
    }
}

MENUS_BY_STATE = {
    States.logged_out: _MENU_LOGGED_OUT,
    States.authenticated: _MENU_AUTHENTICATED,
}
