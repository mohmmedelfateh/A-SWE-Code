# Model
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# View
class LoginView:
    def display_error(self, message):
        print("Error:", message)


# Controller
class LoginController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def login(self, username, password):
        if username == self.model.username and password == self.model.password:
            print("Login successful")
        else:
            self.view.display_error("Invalid username or password")


# Usage
user = User("Mohammed", "1234")
view = LoginView()
controller = LoginController(user, view)
controller.login("example", "password")
