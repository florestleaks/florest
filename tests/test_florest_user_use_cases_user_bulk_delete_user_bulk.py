import unittest
from unittest.mock import Mock

from florest.user.use_cases.user.bulk.delete_user_bulk import DeleteUsersBulk


class TestDeleteUsersBulk(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.delete_users_bulk = DeleteUsersBulk(self.repository_mock)

    def test_execute_calls_repository_bulk_user_delete(self):
        # Create a mock list of emails
        emails_mock = ["alice@example.com", "bob@example.com"]

        # Set up the mock repository to return True when `bulk_user_delete` is called, indicating successful deletion
        self.repository_mock.bulk_user_delete.return_value = True

        # Execute the function
        result = self.delete_users_bulk.execute(emails_mock)

        # Ensure that the repository's bulk_user_delete function was called with the correct list of emails
        self.repository_mock.bulk_user_delete.assert_called_with(emails_mock)

        # Ensure that the result matches what we expect (True for success)
        self.assertTrue(result)
