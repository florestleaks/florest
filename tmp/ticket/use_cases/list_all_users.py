class ListAllUsers:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        # Add any business-specific logic here
        return self.repository.list_all()
