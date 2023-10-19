import unittest

from florest.user.exceptions import UserAlreadyExistsError, UserNotFoundError


class TestUserExceptions(unittest.TestCase):
    def test_user_already_exists_error(self):
        # Test that UserAlreadyExistsError is raised
        with self.assertRaises(UserAlreadyExistsError):
            raise UserAlreadyExistsError("User already exists")

    def test_user_not_found_error(self):
        # Test that UserNotFoundError is raised
        with self.assertRaises(UserNotFoundError):
            raise UserNotFoundError("User not found")
