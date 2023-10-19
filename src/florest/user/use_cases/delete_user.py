class DeleteUser:
    def __init__(self, repository):
        """
        Initialize a DeleteUser instance.

        Parameters
        ----------
        repository : Repository
            The repository used for deleting a user.

        Returns
        -------
        None
        """
        self.repository = repository

    def execute(self, user_id):
        """
        Execute the user deletion operation.

        Parameters
        ----------
        user_id : int
            The unique identifier of the user to be deleted.

        Returns
        -------
        bool
            True if the user deletion was successful, False otherwise.
        """
        # Add any business-specific validation or logic here
        return self.repository.delete_user(user_id)
