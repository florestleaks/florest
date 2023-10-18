from florest import User


class CreateUserBulk:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, users: list[User]) -> bool:
        # Add any business-specific validation or logic here
        return self.repository.add_bulk(users)
