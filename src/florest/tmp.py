from florest import MongodbUserRepository, User
from florest.factory.user.factory_user_mongo import UserFactoryMongodbRepository

if __name__ == "__main__":
    repo = MongodbUserRepository("mongodb://localhost:27017/", "user_database", "users_collection")
    user_factory = UserFactoryMongodbRepository(repo)

    print(user_factory.create_user("John Doe", "johndoe@example.com"))
    user = User(name="John D.", email="johndoe@example.com")

    print(user_factory.update_user(user))
    for user in user_factory.list_all_users():
        print(user.id, user.name, user.email)

    print(user_factory.delete_user(user.id))

    users = [
        User(name="Alice", email="alice@example.com"),
        User(name="Bob", email="bob@example.com"),
    ]

    print(user_factory.add_bulk_users(users))

    # print(user_factory.delete_bulk_users())
