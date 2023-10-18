# create_user.py


class CreateUser:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user):
        # Add any business-specific validation or logic here
        return self.repository.add(user)
