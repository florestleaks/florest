from abc import ABC, abstractmethod

from florest import User


class UserRepository(ABC):
    """
    Abstract base class for user repository.
    Defines the contract for user data operations.
    """

    # ==============================
    # Individual (Unitary) Operations
    # ==============================

    @abstractmethod
    def create(self, user: User) -> bool | None:
        """
        Add a user to the storage.
        :param user: The user object to be added.
        :return: True if successful, False if failed, None if user already exists.
        """

    @abstractmethod
    def update(self, user: User) -> bool:
        """
        Update a user's details.
        :param user: The updated user object.
        :return: True if successful, False otherwise.
        """

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        """
        Delete a user by their unique ID.
        :param user_id: The unique ID of the user.
        :return: True if successful, False otherwise.
        """

    @abstractmethod
    def find_by_id(self, user_id: int) -> User | None:
        """
        Find a user by their unique ID.
        :param user_id: The unique ID of the user.
        :return: User object if found, None otherwise.
        """

    # ==============================
    # Batch (Bulk) Operations
    # ==============================

    @abstractmethod
    def add_bulk(self, users: list[User]) -> bool:
        """
        Add multiple users to the storage.
        :param users: List of user objects to be added.
        :return: True if all users are added successfully, False otherwise.
        """

    @abstractmethod
    def find_by_ids(self, user_ids: list[int]) -> list[User | None]:
        """
        Find multiple users by their unique IDs.
        :param user_ids: List of unique IDs of the users.
        :return: List of User objects corresponding to the given IDs. If a user is not found, its position in the list will be None.
        """

    @abstractmethod
    def update_bulk(self, users: list[User]) -> bool:
        """
        Update multiple users' details.
        :param users: List of updated user objects.
        :return: True if all users are updated successfully, False otherwise.
        """

    @abstractmethod
    def delete_bulk(self, user_ids: list[int]) -> bool:
        """
        Delete multiple users by their unique IDs.
        :param user_ids: List of unique IDs of the users to be deleted.
        :return: True if all users are deleted successfully, False otherwise.
        """

    @abstractmethod
    def list_all(self) -> list[User]:
        """
        List all users in the storage.
        """
