from florest.frameworks_and_drivers import (
    MongodbUserRepository,
    UserAlreadyExistsError,
    UserNotFoundError,
)
from florest.user.entities.user import User


class UserFactoryMongodbRepository(MongodbUserRepository):
    def __init__(self, repository: MongodbUserRepository):
        self.repo = repository

    def create_user(self, name, email):
        user = User(name=name, email=email)
        try:
            self.repo.create(user)
            return f"User {user.name} added successfully with ID: {user.id}"
        except UserAlreadyExistsError:
            return "A user with this email already exists."

    def update_user(self, user):
        try:
            self.repo.update(user)
            return f"User {user.id} updated successfully."
        except UserNotFoundError:
            return "User not found. Couldn't update."

    def delete_user(self, user_id):
        try:
            self.repo.delete(user_id)
            return f"User {user_id} deleted successfully."
        except UserNotFoundError:
            return "User not found. Couldn't delete."

    def list_all_users(self):
        return self.repo.list_all()

    def add_bulk_users(self, users):
        try:
            self.repo.add_bulk(users)
            return "Bulk users added successfully."
        except Exception as e:
            return f"Bulk insert failed: {e}"

    def delete_bulk_users(self):
        user_ids = [user.id for user in self.repo.list_all()]
        try:
            self.repo.delete_bulk(user_ids)
            return "Bulk users deleted successfully."
        except Exception as e:
            return f"Bulk delete failed: {e}"
