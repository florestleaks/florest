import unittest
from unittest.mock import Mock
from florest.user.entities import User
from florest.user.use_cases.user.bulk.update_user_bulk import UpdateUsersBulk


class TestUpdateUsersBulk(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.update_users_bulk = UpdateUsersBulk(self.repository_mock)

    def test_execute_calls_repository_bulk_user_update(self):
        # Create mock users
        user1 = User(
            name="ali", email="dsa@dsa.com"
        )  # Assuming User has a default constructor or can be set up with necessary attributes
        user2 = User(name="ali", email="dsa@dsa.csom")
        users_mock = [user1, user2]

        # Set up the mock repository to return True when `bulk_user_update` is called, indicating successful update
        self.repository_mock.bulk_user_update.return_value = True

        # Execute the function
        result = self.update_users_bulk.execute(users_mock)

        # Ensure that the repository's bulk_user_update function was called with the correct list of users
        self.repository_mock.bulk_user_update.assert_called_with(users_mock)

        # Ensure that the result matches what we expect (True for success)
        self.assertTrue(result)
