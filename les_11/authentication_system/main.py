import os

from les_11.authentication_system.app.menu import MenuService
from les_11.authentication_system.app.messages import Messages
from les_11.authentication_system.app.states import UserState
from les_11.authentication_system.exceptions.auth_exceptions import LoginOrPasswordWrong, UserAlreadyExists
from les_11.authentication_system.exceptions.app_exceptions import UnidentifiedOperationSelected


class Application:
    @classmethod
    def clear_console(cls):
        os.system('clear')

    @classmethod
    def print_to_console(cls, data):
        print(data, end='\n\n')

    @classmethod
    def run(cls):
        MenuService.show_menu_by_state(UserState.state)
        user_action = input()

        try:
            MenuService.execute(UserState.state, user_action)
            cls.clear_console()
            cls.print_to_console(Messages.success.value)
        except (UserAlreadyExists, LoginOrPasswordWrong, UnidentifiedOperationSelected) as e:
            cls.clear_console()
            cls.print_to_console(e.message)

        cls.run()


Application.run()
