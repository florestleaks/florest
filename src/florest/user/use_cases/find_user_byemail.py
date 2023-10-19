from florest.user.entities import User


class FindUserByEmail:
    def __init__(self, repository):
        """
        Initialize a FindUserByEmail instance.

        Parameters
        ----------
        repository : Repository
            The repository used for finding a user by email.

        Returns
        -------
        None
        """
        self.repository = repository

    def execute(self, email: str) -> User | None:
        """
        Execute the user retrieval operation by email.

        Parameters
        ----------
        email : str
            The email address of the user to be found.

        Returns
        -------
        User or None
            The User object if found, or None if no user with the provided email exists.
        """
        # Add any business-specific validation or logic here
        return self.repository.find_user_by_email(email)
