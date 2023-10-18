# get_user.py


class GetUser:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user_id):
        # Add any business-specific validation or logic here
        return self.repository.find_by_id(user_id)
