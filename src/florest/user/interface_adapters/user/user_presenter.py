class UserPresenter:
    @staticmethod
    def format(data):
        """
        Format user data into a dictionary.

        Parameters
        ----------
        data : User
            The user data to be formatted.

        Returns
        -------
        dict
            A dictionary containing formatted user data with 'name' and 'email' fields.
        """
        return {"name": data.name, "email": data.email}
