class ListAllUsers:
    def __init__(self, repository):
        """
        Initialize a ListAllUsers instance.

        Parameters
        ----------
        repository : Repository
            The repository used for listing all users.

        Returns
        -------
        None
        """
        self.repository = repository

    def execute(self):
        """
        Execute the operation to list all users.

        Returns
        -------
        list[User]
            A list of User objects representing all the users in the system.
        """
        # Add any business-specific logic here
        return self.repository.list_all_users()
