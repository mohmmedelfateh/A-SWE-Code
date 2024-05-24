# Dependency Inversion Principle
class BaseUser:
    def get_user_info(self):
        raise NotImplementedError("Subclasses must implement get_user_info method")


class User(BaseUser):
    def get_user_info(self):
        return "info"


class VIPUser(BaseUser):
    def get_user_info(self):
        return "VIPinfo"


def run_program(user_obj: BaseUser):
    return user_obj.get_user_info()
