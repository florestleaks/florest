class DeleteUsersBulk:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user_ids: list[int]) -> bool:
        # Add any business-specific validation or logic here
        return self.repository.delete_bulk(user_ids)
