import unittest
from unittest.mock import Mock

from florest.user.use_cases.update_user import UpdateUser


class TestUpdateUser(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.update_user = UpdateUser(self.repository_mock)

    def test_execute_calls_repository_update_user(self):
        # Create a mock user
        user_mock = {"id": 1, "name": "Alice"}

        # Set up the mock repository to return the same user when `update_user` is called
        self.repository_mock.update_user.return_value = user_mock

        # Execute the function
        result = self.update_user.execute(user_mock)

        # Ensure that the repository's update_user function was called with the right user
        self.repository_mock.update_user.assert_called_with(user_mock)

        # Ensure that the result matches what we expect
        self.assertEqual(result, user_mock)
