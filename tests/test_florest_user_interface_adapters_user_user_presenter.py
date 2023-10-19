import unittest

from florest.user.entities import User
from florest.user.interface_adapters.user.user_presenter import UserPresenter


class TestUserPresenter(unittest.TestCase):
    def test_format(self):
        # Create a mock user
        user_mock = User(name="Alice", email="alice@example.com")

        # Format the user data using UserPresenter
        formatted_data = UserPresenter.format(user_mock)

        # Check if the formatted data is as expected
        expected_data = {"name": "Alice", "email": "alice@example.com"}
        self.assertEqual(formatted_data, expected_data)

    # Add more tests to cover other scenarios or edge cases if needed
