# Model
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# View
class LoginView:
    def display_error(self, message):
        print("Error:", message)


# Presenter
class LoginPresenter:
    def __init__(self, username, password, view):
        self.model = User(username, password)
        self.view = view

    def login(self, username, password):
        if username == self.model.username and password == self.model.password:
            print("Login successful!")
        else:
            self.view.display_error("Invalid credentials")


# Usage
view = LoginView()
presenter = LoginPresenter("Mohammed", "124", view)
presenter.login("example", "password")
