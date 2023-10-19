# update_user.py


class UpdateUser:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user):
        # Add any business-specific validation or logic here
        return self.repository.update(user)
