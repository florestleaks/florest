class User:
    """
    Represents a user with a name and email address.

    Attributes
    ----------
    name : str
        Name of the user.
    email : str
        Email address of the user.

    """

    def __init__(self, name: str, email: str):
        """
        Initializes the User with the given name and email.

        Parameters
        ----------
        name : str
            Name of the user.
        email : str
            Email address of the user.
        """
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        """
        Return a string representation of the User.

        Returns
        -------
        str
            A string representation of the User in the format:
            "User(name='name', email='email')"
        """
        return f"User(name='{self.name}', email='{self.email}')"
