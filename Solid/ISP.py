# Interface Segregation Principle
from abc import ABC, abstractmethod


class CreateService(ABC):
    @abstractmethod
    def save(self, data):
        pass


class RetrieveService(ABC):
    @abstractmethod
    def get(self, id):
        pass


class UpdateService(ABC):
    @abstractmethod
    def update(self, id, data):
        pass


class DeleteService(ABC):
    @abstractmethod
    def delete(self, id):
        pass


class UserService(CreateService, RetrieveService, UpdateService, DeleteService):
    def save(self, data):
        print("User was saved")

    def get(self, id):
        print("User was retrieved")

    def update(self, id, data):
        print("User was updated")

    def delete(self, id):
        print("User was deleted")


class OrderService(CreateService, RetrieveService, UpdateService):
    def save(self, data):
        print("Order was saved")

    def get(self, id):
        print("Order was retrieved")

    def update(self, id, data):
        print("Order was updated")


# Example usage
if __name__ == "__main__":
    user_service = UserService()
    order_service = OrderService()

    user_service.save("User data")
    user_service.get(123)
    user_service.update(123, "Updated user data")
    user_service.delete(123)

    order_service.save("Order data")
    order_service.get(456)
    order_service.update(456, "Updated order data")
