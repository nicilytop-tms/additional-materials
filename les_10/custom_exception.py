class ValidatePasswordException(Exception):
    RULE = 'Password must contain at least one digit!'

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __str__(self):
        message = f'{self.login}, your password {self.password} is wrong!\n{self.RULE}'
        return message


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

        if not self._is_password_valid():
            raise ValidatePasswordException(self.login, self.password)

    def _is_password_valid(self):
        for dt in '1234567890':
            if dt in self.password:
                return True
        return False


try:
    vasya = User('vasya123', 'dkslkjsdf2')
    dima = User('dimdim', '2231231237657465656767867')
    ivan = User('spaceboy', 'Hkljsadf')
except ValidatePasswordException as e:
    print(e)
