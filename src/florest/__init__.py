from florest.entities.user import User
from florest.frameworks_and_drivers.database_driver import (
    MongodbUserRepository,
    UserAlreadyExistsError,
    UserNotFoundError,
)
from florest.use_cases.create_user import CreateUser
from florest.use_cases.delete_user import DeleteUser
from florest.use_cases.get_user import GetUser
from florest.use_cases.list_all_users import ListAllUsers
from florest.use_cases.update_user import UpdateUser
from florest.use_cases.user.bulk.create_user_bulk import CreateUserBulk
from florest.use_cases.user.bulk.delete_user_bulk import DeleteUsersBulk
from florest.use_cases.user.bulk.find_user_byids_bulk import FindUsersByIds
from florest.use_cases.user.bulk.update_user_bulk import UpdateUsersBulk

if __name__ == "__main__":
    # Initialize the repository
    repo = MongodbUserRepository("mongodb://localhost:27017/", "user_database", "users_collection")

    # Create a new user and add them
    new_user = User(name="John Doe", email="johndoe@example.com")
    try:
        repo.add(new_user)
        print(f"User {new_user.name} added successfully with ID: {new_user.id}")
    except UserAlreadyExistsError:
        print("A user with this email already exists.")

    # Update the user
    new_user.name = "dsa D."
    try:
        repo.update(new_user)
        print(f"User {new_user.id} updated successfully.")
    except UserNotFoundError:
        print("User not found. Couldn't update.")

    # List all users
    all_users = repo.list_all()
    for user in all_users:
        print(user.id, user.name, user.email)

    # Delete the user
    try:
        repo.delete(new_user.id)
        print(f"User {new_user.id} deleted successfully.")
    except UserNotFoundError:
        print("User not found. Couldn't delete.")

    # Use the bulk operations
    users_to_add = [
        User(name="Alice", email="alice@example.com"),
        User(name="Bob", email="bob@example.com"),
    ]
    try:
        repo.add_bulk(users_to_add)
        print("Bulk users added successfully.")
    except Exception as e:
        print(f"Bulk insert failed: {e}")

    user_ids_to_delete_l = repo.list_all()
    user_ids_to_delete = [user.id for user in user_ids_to_delete_l]
    # Example usage:
    try:
        repo.delete_bulk(user_ids_to_delete)
        print("Bulk users deleted successfully.")
    except Exception as e:
        print(f"Bulk delete failed: {e}")
