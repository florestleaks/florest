import unittest
from unittest.mock import Mock
from florest.user.entities import User
from florest.user.use_cases.user.bulk.create_user_bulk import CreateUserBulk


class TestCreateUserBulk(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.create_user_bulk = CreateUserBulk(self.repository_mock)

    def test_execute_calls_repository_bulk_user_create(self):
        # Create mock users
        user1 = User(
            name="ali", email="dsa@dsa.com"
        )  # Assuming User has a default constructor or can be set up with necessary attributes
        user2 = User(name="ali", email="dsa@dsa.csom")
        users_mock = [user1, user2]

        # Set up the mock repository to return True when `bulk_user_create` is called, indicating successful creation
        self.repository_mock.bulk_user_create.return_value = True

        # Execute the function
        result = self.create_user_bulk.execute(users_mock)

        # Ensure that the repository's bulk_user_create function was called with the correct list of users
        self.repository_mock.bulk_user_create.assert_called_with(users_mock)

        # Ensure that the result matches what we expect (True for success)
        self.assertTrue(result)
