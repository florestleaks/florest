class GetUser:
    def __init__(self, repository):
        """
        Initialize a GetUser instance.

        Parameters
        ----------
        repository : Repository
            The repository used for retrieving a user.

        Returns
        -------
        None
        """
        self.repository = repository

    def execute(self, criteria):
        """
        Execute the user retrieval operation.

        Parameters
        ----------
        criteria : any
            The criteria used to retrieve the user, such as an ID or other identifier.

        Returns
        -------
        User or None
            The User object if found based on the given criteria, or None if no user matches the criteria.
        """
        return self.repository.get_user(criteria)
