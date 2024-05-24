# Liskov Substitution Principle
from abc import ABC, abstractmethod


class Authentication(ABC):
    @abstractmethod
    def authenticate(self) -> bool:
        pass


class BasicAuth(Authentication):
    def __init__(self, password_source: str):
        self.password_source = password_source

    def authenticate(self) -> bool:
        password = self.get_password()
        # Placeholder authentication logic
        return True

    def get_password(self) -> str:
        return self.password_source


class PassAuth(Authentication):
    def __init__(self, password_source: str):
        super().__init__()
        self.password_source = password_source

    def authenticate(self) -> bool:
        password = self.password_source
        # Add your authentication logic here
        return True

    def get_password(self) -> str:
        return self.password_source


class DNAAuth(Authentication):
    def __init__(self, password_source: str):
        super().__init__()
        self.password_source = password_source

    def authenticate(self) -> bool:
        # Add your authentication logic here
        return True


def auth_user(auth_method: Authentication) -> bool:
    return auth_method.authenticate()


if __name__ == "__main__":
    basic_auth = BasicAuth("password123")
    pass_auth = PassAuth("password456")
    dna_auth = DNAAuth("DNACode123")

    # Authentication using different methods
    print(auth_user(basic_auth))
    print(auth_user(pass_auth))
    print(auth_user(dna_auth))
