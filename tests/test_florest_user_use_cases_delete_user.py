import unittest
from unittest.mock import Mock

from florest.user.use_cases.delete_user import DeleteUser


class TestDeleteUser(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.delete_user = DeleteUser(self.repository_mock)

    def test_execute_calls_repository_delete_user(self):
        # Create a mock user_id
        user_id_mock = 1

        # Set up the mock repository to return True when `delete_user` is called, indicating successful deletion
        self.repository_mock.delete_user.return_value = True

        # Execute the function
        result = self.delete_user.execute(user_id_mock)

        # Ensure that the repository's delete_user function was called with the right user_id
        self.repository_mock.delete_user.assert_called_with(user_id_mock)

        # Ensure that the result matches what we expect
        self.assertTrue(result)
