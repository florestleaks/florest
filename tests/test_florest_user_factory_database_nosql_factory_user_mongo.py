import unittest
from unittest.mock import Mock
from florest.user.drivers.database.nosql.mongodb_driver import (
    UserAlreadyExistsError,
    UserNotFoundError,
)
from florest.user.entities import User
from florest.user.factory.database.nosql.factory_user_mongo import UserFactoryMongodbRepository


class TestUserFactoryMongodbRepository(unittest.TestCase):
    def setUp(self):
        # Mocking the MongodbUserRepository for testing without real DB
        self.mock_repo = Mock()
        self.user_factory = UserFactoryMongodbRepository(self.mock_repo)

    def test_create_user_success(self):
        self.mock_repo.create.return_value = None
        response = self.user_factory.create_user("John", "john@example.com")
        self.assertEqual(response, "User John added successfully with email: john@example.com")

    def test_create_user_already_exists(self):
        self.mock_repo.create.side_effect = UserAlreadyExistsError
        response = self.user_factory.create_user("John", "john@example.com")
        self.assertEqual(response, "User John added successfully with email: john@example.com")

    def test_update_user_success(self):
        user = User(name="John", email="john@example.com")
        self.mock_repo.update.return_value = None
        response = self.user_factory.update_user(user)
        self.assertEqual(response, "User john@example.com updated successfully.")

    def test_update_user_not_found(self):
        user = User(name="John", email="john@example.com")
        self.mock_repo.update.side_effect = UserNotFoundError
        response = self.user_factory.update_user(user)
        self.assertEqual(response, "User john@example.com updated successfully.")

    def test_delete_user_success(self):
        self.mock_repo.delete.return_value = None
        response = self.user_factory.delete_user("john@example.com")
        self.assertEqual(response, "User with email john@example.com deleted successfully.")

    def test_delete_user_not_found(self):
        self.mock_repo.delete.side_effect = UserNotFoundError
        response = self.user_factory.delete_user("john@example.com")
        self.assertEqual(response, "User with email john@example.com deleted successfully.")

    def test_list_all_users(self):
        self.mock_repo.list_all_users.return_value = []
        response = self.user_factory.list_all_users()
        self.assertEqual(response, [])

    def test_find_user_by_email_success(self):
        user = User(name="John", email="john@example.com")
        self.mock_repo.find_user_by_email.return_value = user
        response = self.user_factory.find_user_by_email("john@example.com")
        self.assertEqual(response, user)

    def test_find_user_by_email_not_found(self):
        self.mock_repo.find_user_by_email.side_effect = UserNotFoundError
        response = self.user_factory.find_user_by_email("john@example.com")
        self.assertEqual(response, "User not found.")

    def test_get_user(self):
        user = User(name="John", email="john@example.com")
        self.mock_repo.get_user.return_value = user
        response = self.user_factory.get_user({"name": "John"})
        self.assertEqual(response, user)

    def test_bulk_user_create_success(self):
        users = [User(name="John", email="john@example.com")]
        response = self.user_factory.bulk_user_create(users)
        self.assertEqual(response, "Bulk users added successfully.")

    def test_bulk_user_create_failure(self):
        users = [User(name="John", email="john@example.com")]
        self.mock_repo.bulk_user_create.side_effect = Exception("Bulk insert error")
        response = self.user_factory.bulk_user_create(users)
        self.assertEqual(response, "Bulk insert failed: Bulk insert error")

    def test_bulk_user_update_success(self):
        users = [User(name="John", email="john@example.com")]
        response = self.user_factory.bulk_user_update(users)
        self.assertEqual(response, "Bulk users updated successfully.")

    def test_bulk_user_update_failure(self):
        users = [User(name="John", email="john@example.com")]
        self.mock_repo.bulk_user_update.side_effect = Exception("Bulk update error")
        response = self.user_factory.bulk_user_update(users)
        self.assertEqual(response, "Bulk update failed: Bulk update error")

    def test_bulk_user_delete_success(self):
        emails = ["john@example.com"]
        response = self.user_factory.bulk_user_delete(emails)
        self.assertEqual(response, "Bulk users deleted successfully.")

    def test_bulk_user_delete_failure(self):
        emails = ["john@example.com"]
        self.mock_repo.bulk_user_delete.side_effect = Exception("Bulk delete error")
        response = self.user_factory.bulk_user_delete(emails)
        self.assertEqual(response, "Bulk delete failed: Bulk delete error")
