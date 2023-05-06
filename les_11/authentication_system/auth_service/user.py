from les_11.authentication_system.instances.user import User


class UserManager:
    @classmethod
    def is_login_already_exist(cls, login, storage):
        return True if cls.get_user_by_login(login, storage) else False

    @staticmethod
    def get_user_by_login(login, storage):
        for user in storage.data:
            if user['login'] == login:
                return User(**user)

        return None
