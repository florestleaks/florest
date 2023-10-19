from abc import ABC, abstractmethod

from florest.user.entities import User


class UserRepository(ABC):
    """
    Abstract base class for user repository.
    Defines the contract for user data operations.

    Methods
    -------
    create_user(user: User) -> bool | None
        Add a user to the storage.

    get_user(criteria: dict) -> User | None
        Retrieve a user based on specified criteria.

    update_user(user: User) -> bool
        Update a user's details.

    delete_user(user_id: int) -> bool
        Delete a user by their unique ID.

    find_user_by_email(user_mail: str) -> User | None
        Find a user by their email.

    bulk_user_create(users: list[User]) -> bool
        Add multiple users to the storage.

    bulk_user_update(users: list[User]) -> bool
        Update multiple users' details.

    bulk_user_delete(user_ids: list[int]) -> bool
        Delete multiple users by their unique IDs.

    list_all_users() -> list[User]
        List all users in the storage.
    """

    @abstractmethod
    def create_user(self, user: User) -> bool | None:
        """
        Add a user to the storage.

        Parameters
        ----------
        user : User
            The user object to be added.

        Returns
        -------
        bool | None
            True if successful, False if failed, None if user already exists.
        """

    @abstractmethod
    def get_user(self, criteria: dict) -> User | None:
        """
        Retrieve a user based on specified criteria.

        Parameters
        ----------
        criteria : dict
            A dictionary containing criteria for user retrieval.

        Returns
        -------
        User | None
            User object if found, None otherwise.
        """

    @abstractmethod
    def update_user(self, user: User) -> bool:
        """
        Update a user's details.

        Parameters
        ----------
        user : User
            The updated user object.

        Returns
        -------
        bool
            True if successful, False otherwise.
        """

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        """
        Delete a user by their unique ID.

        Parameters
        ----------
        user_id : int
            The unique ID of the user.

        Returns
        -------
        bool
            True if successful, False otherwise.
        """

    @abstractmethod
    def find_user_by_email(self, user_mail: str) -> User | None:
        """
        Find a user by their email.

        Parameters
        ----------
        user_mail : str
            The email address of the user.

        Returns
        -------
        User | None
            User object if found, None otherwise.
        """

    @abstractmethod
    def bulk_user_create(self, users: list[User]) -> bool:
        """
        Add multiple users to the storage.

        Parameters
        ----------
        users : list[User]
            List of user objects to be added.

        Returns
        -------
        bool
            True if all users are added successfully, False otherwise.
        """

    @abstractmethod
    def bulk_user_update(self, users: list[User]) -> bool:
        """
        Update multiple users' details.

        Parameters
        ----------
        users : list[User]
            List of updated user objects.

        Returns
        -------
        bool
            True if all users are updated successfully, False otherwise.
        """

    @abstractmethod
    def bulk_user_delete(self, user_ids: list[int]) -> bool:
        """
        Delete multiple users by their unique IDs.

        Parameters
        ----------
        user_ids : list[int]
            List of unique IDs of the users to be deleted.

        Returns
        -------
        bool
            True if all users are deleted successfully, False otherwise.
        """

    @abstractmethod
    def list_all_users(self) -> list[User]:
        """
        List all users in the storage.

        Returns
        -------
        list[User]
            A list of User objects representing all the users in the system.
        """
