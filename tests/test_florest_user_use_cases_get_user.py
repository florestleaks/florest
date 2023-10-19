import unittest
from unittest.mock import Mock

from florest.user.use_cases.get_user import GetUser


class TestGetUser(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.get_user = GetUser(self.repository_mock)

    def test_execute_calls_repository_get_user_criteria_user(self):
        # Create a mock criteria
        criteria_mock = {"name": "Alice"}

        # Create a mock user to be returned based on the criteria
        user_mock = {"name": "Alice", "email": "alice@example.com"}

        # Set up the mock repository to return the user when `get_user` is called with the criteria
        self.repository_mock.get_user.return_value = user_mock

        # Execute the function
        result = self.get_user.execute(criteria_mock)

        # Ensure that the repository's get_user function was called with the right criteria
        self.repository_mock.get_user.assert_called_with(criteria_mock)

        # Ensure that the result matches what we expect
        self.assertEqual(result, user_mock)

    def test_execute_calls_repository_get_user_criteria_mail(self):
        # Create a mock criteria
        criteria_mock = {"mail": "alice@example.com"}

        # Create a mock user to be returned based on the criteria
        user_mock = {"name": "Alice", "email": "alice@example.com"}

        # Set up the mock repository to return the user when `get_user` is called with the criteria
        self.repository_mock.get_user.return_value = user_mock

        # Execute the function
        result = self.get_user.execute(criteria_mock)

        # Ensure that the repository's get_user function was called with the right criteria
        self.repository_mock.get_user.assert_called_with(criteria_mock)

        # Ensure that the result matches what we expect
        self.assertEqual(result, user_mock)

    # Add more tests to cover other scenarios, edge cases or business-specific validations
