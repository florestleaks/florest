from florest import User


class FindUserById:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user_id: int) -> User | None:
        # Add any business-specific validation or logic here
        return self.repository.find_by_id(user_id)
