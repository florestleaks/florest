from typing import Any, Union

from florest.user.drivers.database.nosql.mongodb_driver import (
    MongodbUserRepository,
    UserAlreadyExistsError,
    UserNotFoundError,
)
from florest.user.entities import User
from florest.user.interface_adapters.user.user_repository import UserRepository
from florest.user.use_cases.create_user import CreateUser
from florest.user.use_cases.delete_user import DeleteUser
from florest.user.use_cases.find_user_byemail import FindUserByEmail
from florest.user.use_cases.get_user import GetUser
from florest.user.use_cases.list_all_users import ListAllUsers
from florest.user.use_cases.update_user import UpdateUser
from florest.user.use_cases.user.bulk.create_user_bulk import CreateUserBulk
from florest.user.use_cases.user.bulk.delete_user_bulk import DeleteUsersBulk
from florest.user.use_cases.user.bulk.update_user_bulk import UpdateUsersBulk


class UserFactoryMongodbRepository(UserRepository):
    """
    Factory repository for user management using MongoDB as the backend database.

    Attributes
    ----------
    repo : MongodbUserRepository
        The MongoDB user repository instance.
    """

    def __init__(self, repository: MongodbUserRepository):
        """
        Initialize the repository.

        Parameters
        ----------
        repository : MongodbUserRepository
            The MongoDB user repository instance.
        """
        self.repo = repository

    def create_user(self, name: str, email: str) -> str:
        """
        Create a new user.

        Parameters
        ----------
        name : str
            The user's name.
        email : str
            The user's email.

        Returns
        -------
        str
            Message indicating the result of the operation.
        """
        user = User(name=name, email=email)
        try:
            CreateUser(self.repo).execute(user)
            return f"User {user.name} added successfully with email: {user.email}"
        except UserAlreadyExistsError:
            return "A user with this email already exists."

    def update_user(self, user: User) -> str:
        """
        Update an existing user.

        Parameters
        ----------
        user : User
            The user instance with updated details.

        Returns
        -------
        str
            Message indicating the result of the operation.
        """
        try:
            UpdateUser(self.repo).execute(user)
            return f"User {user.email} updated successfully."
        except UserNotFoundError:
            return "User not found. Couldn't update."

    def delete_user(self, email: str) -> str:
        """
        Delete a user by email.

        Parameters
        ----------
        email : str
            The user's email.

        Returns
        -------
        str
            Message indicating the result of the operation.
        """
        try:
            DeleteUser(self.repo).execute(email)
            return f"User with email {email} deleted successfully."
        except UserNotFoundError:
            return "User not found. Couldn't delete."

    def list_all_users(self) -> list[User]:
        """
        List all users.

        Returns
        -------
        List[User]
            A list of all users.
        """
        return ListAllUsers(self.repo).execute()

    def find_user_by_email(self, email: str) -> Union[User, str]:
        """
        Find a user by email.

        Parameters
        ----------
        email : str
            The user's email.

        Returns
        -------
        Union[User, str]
            The found user or a message if not found.
        """
        try:
            user = FindUserByEmail(self.repo).execute(email)
            return user
        except UserNotFoundError:
            return "User not found."

    def get_user(self, criteria: Any) -> User:
        """
        Get a user based on a certain criteria.

        Parameters
        ----------
        criteria : Any
            The criteria for searching the user.

        Returns
        -------
        User
            The found user.
        """
        return GetUser(self.repo).execute(criteria)

    def bulk_user_create(self, users: list[User]) -> str:
        """
        Create multiple users in bulk.

        Parameters
        ----------
        users : List[User]
            A list of users to be created.

        Returns
        -------
        str
            Message indicating the result of the operation.
        """
        try:
            CreateUserBulk(self.repo).execute(users)
            return "Bulk users added successfully."
        except Exception as e:
            return f"Bulk insert failed: {e}"

    def bulk_user_update(self, users: list[User]) -> str:
        """
        Update multiple users in bulk.

        Parameters
        ----------
        users : List[User]
            A list of users to be updated.

        Returns
        -------
        str
            Message indicating the result of the operation.
        """
        try:
            UpdateUsersBulk(self.repo).execute(users)
            return "Bulk users updated successfully."
        except Exception as e:
            return f"Bulk update failed: {e}"

    def bulk_user_delete(self, emails: list[str]) -> str:
        """
        Delete multiple users in bulk based on their emails.

        Parameters
        ----------
        emails : List[str]
            A list of emails of users to be deleted.

        Returns
        -------
        str
            Message indicating the result of the operation.
        """
        try:
            DeleteUsersBulk(self.repo).execute(emails)
            return "Bulk users deleted successfully."
        except Exception as e:
            return f"Bulk delete failed: {e}"
