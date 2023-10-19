class UpdateUser:
    def __init__(self, repository):
        """
        Initialize an UpdateUser instance.

        Parameters
        ----------
        repository : Repository
            The repository used for updating a user.

        Returns
        -------
        None
        """
        self.repository = repository

    def execute(self, user):
        """
        Execute the user update operation.

        Parameters
        ----------
        user : User
            The user object containing updated information.

        Returns
        -------
        bool
            True if the user update was successful, False otherwise.
        """
        # Add any business-specific validation or logic here
        return self.repository.update_user(user)
