class CreateUser:
    def __init__(self, repository):
        """
        Initialize a CreateUser instance.

        Parameters
        ----------
        repository : Repository
            The repository used for creating a user.

        Returns
        -------
        None
        """
        self.repository = repository

    def execute(self, user):
        """
        Execute the user creation operation.

        Parameters
        ----------
        user : User
            The user object to be created.

        Returns
        -------
        bool
            True if the user creation was successful, False otherwise.
        """
        # Add any business-specific validation or logic here
        return self.repository.create_user(user)
