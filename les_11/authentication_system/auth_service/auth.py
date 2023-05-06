from les_11.authentication_system.instances.user import User
from les_11.authentication_system.app.messages import Messages
from les_11.authentication_system.app.states import UserState, States
from les_11.authentication_system.auth_service.user import UserManager
from les_11.authentication_system.app.data_storage import JsonDataStorage
from les_11.authentication_system.exceptions.auth_exceptions import LoginOrPasswordWrong, UserAlreadyExists


class UserService:
    storage = JsonDataStorage('users.json')

    @classmethod
    def convert_user_to_dict(cls, user):
        return {
            'login': user.login,
            'password': user.password,
            'age': user.age
        }

    @classmethod
    def create_user(cls):
        login, password = input(Messages.enter_login_password).split(' ')
        return User(login, password)

    @classmethod
    def update_user_age(cls):
        new_age = input(Messages.enter_new_age)
        user = UserState.current_user

        dict_user = cls.convert_user_to_dict(user)
        cls.storage.remove(dict_user)

        user.age = new_age
        dict_user = cls.convert_user_to_dict(user)
        cls.storage.update(dict_user)


class SignOutService(UserService):
    @classmethod
    def logout(cls):
        UserState.state = States.logged_out
        UserState.current_user = None


class SignUpService(UserService):
    @classmethod
    def sign_up(cls):
        user = cls.create_user()
        if UserManager.is_login_already_exist(user.login, cls.storage):
            raise UserAlreadyExists

        cls.__sign_up_user(user, cls.storage)

    @classmethod
    def __sign_up_user(cls, user, storage):
        data = cls.convert_user_to_dict(user)
        storage.update(data)


class AuthService(UserService):
    @classmethod
    def auth(cls):
        input_user = cls.create_user()
        user = UserManager.get_user_by_login(input_user.login, cls.storage)
        if not user or user.password != input_user.password:
            raise LoginOrPasswordWrong

        UserState.state = States.authenticated
        UserState.current_user = user
