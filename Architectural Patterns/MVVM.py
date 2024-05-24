# Model
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# ViewModel
class LoginViewModel:
    def __init__(self, model):
        self.model = model

    def login(self, username, password):
        return username == self.model.username and password == self.model.password


# View
class LoginView:
    def display_error(self, message):
        print("Error:", message)


# Usage
user = User("example", "password")
view = LoginView()
view_model = LoginViewModel(user)
if view_model.login("example", "password"):
    print("Login successful")
else:
    view.display_error("Invalid username or password")
