from typing import Optional

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from florest.user.entities import User
from florest.user.exceptions import UserAlreadyExistsError, UserNotFoundError
from florest.user.interface_adapters.user.user_repository import UserRepository


class MongodbUserRepository(UserRepository):
    def __init__(self, connection_string: str, database_name: str, collection_name: str) -> None:
        """
        Initialize a MongoDB user repository.

        Parameters
        ----------
        connection_string : str
            The connection string for MongoDB.
        database_name : str
            The name of the MongoDB database.
        collection_name : str
            The name of the MongoDB collection.

        """
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

        # Create a unique index on the 'email' field
        self.collection.create_index([("email", 1)], unique=True)

    def get_user(self, criteria: dict) -> User | None:
        """
        Retrieve a user based on the provided criteria.

        Parameters
        ----------
        criteria : dict
            The criteria to use for the query.

        Returns
        -------
        Optional[User]
            The User object or None if not found.

        """
        user_data = self.collection.find_one(criteria)
        if user_data:
            return User(name=user_data["name"], email=user_data["email"])
        return None

    def list_all_users(self) -> list[User]:
        """
        List all users from the MongoDB collection.

        Returns
        -------
        List[User]
            List of all User objects.

        """
        return [
            User(name=user_data["name"], email=user_data["email"])
            for user_data in self.collection.find()
        ]

    def create_user(self, user: User) -> None:
        """
        Create a new user.

        Parameters
        ----------
        user : User
            The user to be created.

        Raises
        ------
        UserAlreadyExistsError
            If the user with the provided email already exists.

        """
        try:
            self.collection.insert_one({"name": user.name, "email": user.email})
        except DuplicateKeyError:
            raise UserAlreadyExistsError(message="Email address already exists.")

    def update_user(self, user: User) -> None:
        """
        Update an existing user.

        Parameters
        ----------
        user : User
            The user to be updated.

        Raises
        ------
        UserNotFoundError
            If the user with the provided email is not found or if no changes were made.

        """
        result = self.collection.replace_one({"email": user.email}, user.__dict__)
        if result.modified_count == 0:
            raise UserNotFoundError(message="User not found or no changes made.")

    def delete_user(self, email: str) -> None:
        """
        Delete a user based on their email.

        Parameters
        ----------
        email : str
            The email of the user to be deleted.

        Raises
        ------
        UserNotFoundError
            If the user with the provided email is not found.

        """
        result = self.collection.delete_one({"email": email})
        if result.deleted_count == 0:
            raise UserNotFoundError(message="User not found.")

    def find_user_by_email(self, email: str) -> Optional[User]:
        """
        Find a user based on their email.

        Parameters
        ----------
        email : str
            The email to search for.

        Returns
        -------
        Optional[User]
            The User object or None if not found.

        """
        user_data = self.collection.find_one({"email": email})
        if user_data:
            return User(name=user_data["name"], email=user_data["email"])
        return None

    def bulk_user_create(self, users: list[User]) -> None:
        """
        Create multiple users at once.

        Parameters
        ----------
        users : List[User]
            List of User objects to be created.

        Raises
        ------
        Exception
            If there are duplicate emails or any other issues during the bulk insert.

        """
        try:
            self.collection.insert_many([user.__dict__ for user in users])
        except Exception as e:
            write_errors = e.details.get("writeErrors", [])
            duplicate_emails = [
                err["keyValue"]["email"] for err in write_errors if err["code"] == 11000
            ]
            if duplicate_emails:
                raise Exception(
                    f"Bulk insert failed: Duplicate emails found - {', '.join(duplicate_emails)}"
                )
            else:
                raise Exception(f"Bulk insert failed with error: {e!s}")

    def bulk_user_update(self, users: list[User]) -> None:
        """
        Update multiple users at once.

        Parameters
        ----------
        users : List[User]
            List of User objects to be updated.

        Raises
        ------
        Exception
            If the updates for some users fail.

        """
        successes = 0
        failed_updates = []
        for user in users:
            result = self.collection.replace_one({"email": user.email}, user.__dict__)
            if result.modified_count > 0:
                successes += 1
            else:
                failed_updates.append(user.email)

        if successes != len(users):
            raise Exception(f"Bulk update failed for email addresses: {', '.join(failed_updates)}")

    def bulk_user_delete(self, emails: list[str]) -> None:
        """

        Delete multiple users based on their emails.

        Parameters
        ----------
        emails : List[str]
            List of email addresses of the users to be deleted.

        Raises
        ------
        Exception
            If the deletion for some users fail.

        """
        result = self.collection.delete_many({"email": {"$in": emails}})
        if result.deleted_count != len(emails):
            missing_count = len(emails) - result.deleted_count
            raise Exception(
                f"Expected to delete {len(emails)} users but only {result.deleted_count} were deleted. {missing_count} users not found."
            )
