from les_11.authentication_system.app.messages import Messages


class UserAlreadyExists(Exception):
    def __init__(self):
        self.message = Messages.user_already_exists.value
        super().__init__(self.message)


class LoginOrPasswordWrong(Exception):
    def __init__(self):
        self.message = Messages.error_auth.value
        super().__init__(self.message)


class LoginTooLong(Exception):
    def __init__(self):
        self.message = Messages.too_long_login.value
        super().__init__(self.message)
