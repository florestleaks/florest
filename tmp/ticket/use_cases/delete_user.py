class DeleteUser:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user_id):
        # Add any business-specific validation or logic here
        return self.repository.delete_user(user_id)
