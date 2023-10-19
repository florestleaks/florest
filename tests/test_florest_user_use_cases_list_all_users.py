import unittest
from unittest.mock import Mock

from florest.user.use_cases.list_all_users import ListAllUsers


class TestListAllUsers(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.list_all_users = ListAllUsers(self.repository_mock)

    def test_execute_calls_repository_list_all_users(self):
        # Create a mock list of users
        users_mock = [
            {"name": "Alice", "email": "alice@example.com"},
            {"name": "Bob", "email": "bob@example.com"},
        ]

        # Set up the mock repository to return the list of users when `list_all_users` is called
        self.repository_mock.list_all_users.return_value = users_mock

        # Execute the function
        result = self.list_all_users.execute()

        # Ensure that the repository's list_all_users function was called
        self.repository_mock.list_all_users.assert_called_once()

        # Ensure that the result matches what we expect
        self.assertEqual(result, users_mock)

    # Add more tests to cover other scenarios, edge cases or business-specific validations
