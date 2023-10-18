from florest.entities.user import User
from florest.interface_adapters.user_presenter import UserPresenter


class UserController:
    def __init__(self, use_cases):
        self.use_cases = use_cases

    # ==============================
    # Individual (Unitary) Operations
    # ==============================

    def create(self, request):
        user = User(request["id"], request["name"], request["email"])
        result = self.use_cases["create_user"].execute(user)
        return UserPresenter.format(result)

    def read(self, user_id):
        result = self.use_cases["get_user"].execute(user_id)
        return UserPresenter.format(result)

    def update(self, request):
        user = User(request["id"], request["name"], request["email"])
        result = self.use_cases["update_user"].execute(user)
        return UserPresenter.format(result)

    def delete(self, user_id):
        result = self.use_cases["delete_user"].execute(user_id)
        return (
            {"status": "success", "message": "User deleted successfully"}
            if result
            else {"status": "failure", "message": "Error deleting user"}
        )

    # ==============================
    # Batch (Bulk) Operations
    # ==============================

    def create_bulk(self, request_list):
        users = [User(req["id"], req["name"], req["email"]) for req in request_list]
        result = self.use_cases["create_users_bulk"].execute(users)
        return UserPresenter.format(result)

    def read_bulk(self, user_ids):
        result = self.use_cases["get_users_bulk"].execute(user_ids)
        return UserPresenter.format(result)

    def update_bulk(self, request_list):
        users = [User(req["id"], req["name"], req["email"]) for req in request_list]
        result = self.use_cases["update_users_bulk"].execute(users)
        return UserPresenter.format(result)

    def delete_bulk(self, user_ids):
        result = self.use_cases["delete_users_bulk"].execute(user_ids)
        return (
            {"status": "success", "message": "Users deleted successfully"}
            if result
            else {"status": "failure", "message": "Error deleting users"}
        )
