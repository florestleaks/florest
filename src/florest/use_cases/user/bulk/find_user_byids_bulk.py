from florest import User


class FindUsersByIds:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user_ids: list[int]) -> list[User | None]:
        # Add any business-specific validation or logic here
        return self.repository.find_by_ids(user_ids)
