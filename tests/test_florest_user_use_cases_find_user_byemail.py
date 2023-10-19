import unittest
from unittest.mock import Mock
from florest.user.entities import User
from florest.user.use_cases.find_user_byemail import FindUserByEmail


class TestFindUserByEmail(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.find_user_by_email = FindUserByEmail(self.repository_mock)

    def test_execute_calls_repository_find_user_by_email(self):
        # Create a mock email
        email_mock = "alice@example.com"

        # Create a mock user
        user_mock = User(
            name="alice", email=email_mock
        )  # Populate as needed based on the User entity definition

        # Set up the mock repository to return the user when `find_user_by_email` is called
        self.repository_mock.find_user_by_email.return_value = user_mock

        # Execute the function
        result = self.find_user_by_email.execute(email_mock)

        # Ensure that the repository's find_user_by_email function was called with the right email
        self.repository_mock.find_user_by_email.assert_called_with(email_mock)

        # Ensure that the result matches what we expect
        self.assertEqual(result, user_mock)
