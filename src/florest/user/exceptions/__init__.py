class UserAlreadyExistsError(Exception):
    """
    Exception raised for errors in the operation when a user already exists.

    Attributes
    ----------
    message : str, optional
        Explanation of the error. Default is 'User already exists.'


    """

    def __init__(self, message: str = "User already exists."):
        self.message = message
        super().__init__(self.message)


class UserNotFoundError(Exception):
    """
    Exception raised for errors in the operation when a user is not found.

    Attributes
    ----------
    message : str, optional
        Explanation of the error. Default is 'User not found.'


    """

    def __init__(self, message: str = "User not found."):
        self.message = message
        super().__init__(self.message)
