class DeleteUsersBulk:
    def __init__(self, repository):
        """
        Initialize a DeleteUsersBulk instance.

        Parameters
        ----------
        repository : Repository
            The repository used for bulk user deletion.

        Returns
        -------
        None
        """
        self.repository = repository

    def execute(self, emails: list[str]) -> bool:
        """
        Execute a bulk user deletion operation.

        Parameters
        ----------
        emails : list[str]
            A list of email addresses associated with users to be deleted.

        Returns
        -------
        bool
            True if the bulk deletion was successful, False otherwise.
        """
        # Add any business-specific validation or logic here
        return self.repository.bulk_user_delete(emails)
