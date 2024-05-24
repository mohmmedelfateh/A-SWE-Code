# Repository Interface
class UserRepository:
    def find_by_id(self, user_id):
        pass

    def save(self, user):
        pass

    def delete(self, user):
        pass


# Concrete Repository Implementation (Database)
class DatabaseUserRepository(UserRepository):
    def find_by_id(self, user_id):
        # Logic to retrieve user from the database
        pass

    def save(self, user):
        # Logic to save user to the database
        pass

    def delete(self, user):
        # Logic to delete user from the database
        pass


# Business Logic
class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user_by_id(self, user_id):
        return self.user_repository.find_by_id(user_id)

    def create_user(self, user):
        self.user_repository.save(user)

    def delete_user(self, user):
        self.user_repository.delete(user)


# Usage
if __name__ == "__main__":
    # Create concrete repository instance
    database_repository = DatabaseUserRepository()

    # Inject repository into the business logic
    user_service = UserService(database_repository)

    # Example usage
    user = user_service.get_user_by_id(1)
    print(user)
