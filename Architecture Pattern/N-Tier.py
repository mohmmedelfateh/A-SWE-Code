# Presentation Layer (UI)
class PresentationLayer:
    def __init__(self, controller):
        self.controller = controller

    def login(self, username, password):
        result = self.controller.login(username, password)
        if result:
            print("Login successful")
        else:
            print("Login failed")


# Application Layer (Business Logic)
class ApplicationController:
    def __init__(self, service):
        self.service = service

    def login(self, username, password):
        return self.service.authenticate(username, password)


# Domain Layer (Domain Logic)
class AuthService:
    def authenticate(self, username, password):
        # Simulating authentication logic
        if username == "example" and password == "password":
            return True
        else:
            return False


# Usage
if __name__ == "__main__":
    # Create instances of layers
    service = AuthService()
    controller = ApplicationController(service)
    presentation_layer = PresentationLayer(controller)

    # Simulate user input
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Trigger login process
    presentation_layer.login(username, password)
