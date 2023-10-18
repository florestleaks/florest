from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from florest import User
from florest.exceptions.user import UserAlreadyExistsError, UserNotFoundError
from florest.interface_adapters.user_repository import UserRepository


class MongodbUserRepository(UserRepository):
    def __init__(self, connection_string: str, database_name: str, collection_name: str):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

        # Create a unique index on the 'email' field
        self.collection.create_index([("email", 1)], unique=True)

    def list_all(self) -> list[User]:
        return [
            User(id=user_data["_id"], name=user_data["name"], email=user_data["email"])
            for user_data in self.collection.find()
        ]

    def add(self, user: User) -> None:
        try:
            result = self.collection.insert_one({"name": user.name, "email": user.email})
            user.id = result.inserted_id
        except DuplicateKeyError:
            raise UserAlreadyExistsError("Email address already exists.")

    def update(self, user: User) -> None:
        result = self.collection.replace_one({"_id": user.id}, user.__dict__)
        if result.modified_count == 0:
            raise UserNotFoundError("User not found or no changes made.")

    def delete(self, user_id: int) -> None:
        result = self.collection.delete_one({"_id": user_id})
        if result.deleted_count == 0:
            raise UserNotFoundError("User not found.")

    def find_by_id(self, user_id: int) -> User | None:
        user_data = self.collection.find_one({"_id": user_id})
        if user_data:
            user_data["id"] = user_data.pop("_id")
            return User(**user_data)
        return None

    def add_bulk(self, users: list[User]) -> None:
        try:
            self.collection.insert_many([user.__dict__ for user in users])
        except Exception as e:
            # Extract error message for duplicate key
            write_errors = e.details.get("writeErrors", [])
            duplicate_emails = [
                err["keyValue"]["email"] for err in write_errors if err["code"] == 11000
            ]
            if duplicate_emails:
                raise Exception(
                    f"Bulk insert failed: Duplicate emails found - {', '.join(duplicate_emails)}"
                )
            else:
                raise Exception(f"Bulk insert failed with error: {e!s}")

    def find_by_ids(self, user_ids: list[int]) -> list[User]:
        cursor = self.collection.find({"_id": {"$in": user_ids}})
        found_users = {user["_id"]: User(**user) for user in cursor}
        return [found_users.get(uid) for uid in user_ids]

    def update_bulk(self, users: list[User]) -> None:
        failed_updates = []
        successes = 0
        for user in users:
            result = self.collection.replace_one({"_id": user.id}, user.__dict__)
            if result.modified_count > 0:
                successes += 1
            else:
                failed_updates.append(user.id)

        if successes != len(users):
            raise Exception(
                f"Bulk update failed for user IDs: {', '.join(map(str, failed_updates))}."
            )

    def delete_bulk(self, user_ids: list[int]) -> None:
        result = self.collection.delete_many({"_id": {"$in": user_ids}})
        if result.deleted_count != len(user_ids):
            missing_count = len(user_ids) - result.deleted_count
            raise Exception(
                f"Expected to delete {len(user_ids)} users but only {result.deleted_count} were deleted. {missing_count} users not found."
            )
