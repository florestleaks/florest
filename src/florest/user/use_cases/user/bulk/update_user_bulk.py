from florest.user.entities import User


class UpdateUsersBulk:
    def __init__(self, repository):
        """
        Initialize an UpdateUsersBulk instance.

        Parameters
        ----------
        repository : Repository
            The repository used for bulk user updates.

        Returns
        -------
        None
        """
        self.repository = repository

    def execute(self, users: list[User]) -> bool:
        """
        Execute a bulk user update operation.

        Parameters
        ----------
        users : list[User]
            A list of User objects containing updated user data.

        Returns
        -------
        bool
            True if the bulk update was successful, False otherwise.
        """
        # Add any business-specific validation or logic here
        return self.repository.bulk_user_update(users)
