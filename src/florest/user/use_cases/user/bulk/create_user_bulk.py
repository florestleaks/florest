from florest.user.entities import User


class CreateUserBulk:
    def __init__(self, repository):
        """
        Initialize a CreateUserBulk instance.

        Parameters
        ----------
        repository : Repository
            The repository used for user creation.

        Returns
        -------
        None
        """
        self.repository = repository

    def execute(self, users: list[User]) -> bool:
        """
        Execute a bulk user creation operation.

        Parameters
        ----------
        users : list[User]
            A list of User objects to create.

        Returns
        -------
        bool
            True if the bulk creation was successful, False otherwise.
        """
        # Add any business-specific validation or logic here
        return self.repository.bulk_user_create(users)
