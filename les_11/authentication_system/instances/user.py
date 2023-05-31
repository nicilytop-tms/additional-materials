from les_11.authentication_system.exceptions.auth_exceptions import LoginTooLong


class User:
    def __init__(self, login, password, age=None):
        self.login = login
        self.password = password
        self.age = age

        self.check_login()
        self.check_password()

    def check_login(self):
        if len(self.login) > 10:
            raise LoginTooLong

    def check_password(self):
        pass
