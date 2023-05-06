class User:
    def __init__(self, login, password, age=None):
        self.login = login
        self.password = password
        self.age = age

        self.check_login()
        self.check_password()

    def check_login(self):
        pass

    def check_password(self):
        pass
