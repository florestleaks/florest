from florest import User


class UpdateUsersBulk:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, users: list[User]) -> bool:
        # Add any business-specific validation or logic here
        return self.repository.update_bulk(users)
