import unittest
from unittest.mock import Mock

from florest.user.use_cases.create_user import CreateUser


class TestCreateUser(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.create_user = CreateUser(self.repository_mock)

    def test_execute_calls_repository_create_user(self):
        # Create a mock user
        user_mock = {"id": 1, "name": "Alice"}

        # Set up the mock repository to return the same user when `create_user` is called
        self.repository_mock.create_user.return_value = user_mock

        # Execute the function
        result = self.create_user.execute(user_mock)

        # Ensure that the repository's create_user function was called with the right user
        self.repository_mock.create_user.assert_called_with(user_mock)

        # Ensure that the result matches what we expect
        self.assertEqual(result, user_mock)
