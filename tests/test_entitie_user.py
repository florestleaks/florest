import unittest

from florest.user.entities import User


class TestUserEntity(unittest.TestCase):
    def test_user_creation(self):
        user = User(name="John", email="john@example.com")
        self.assertEqual(user.name, "John")

    def test_repr(self):
        user = User(name="John", email="john@example.com")
        expected_repr = "User(name='John', email='john@example.com')"
        actual_repr = repr(user)
        self.assertEqual(actual_repr, expected_repr)
