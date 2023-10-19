# web_server.py
from flask import Flask, jsonify, request

from florest import MongodbUserRepository
from florest.user.entities.user import User
from florest.user.factory.database.nosql.factory_user_mongo import UserFactoryMongodbRepository
from florest.user.interface_adapters.user.user_presenter import UserPresenter

app = Flask(__name__)

DATABASE_URL = "mongodb://localhost:27017/"
DATABASE_NAME = "user_database"
COLLECTION_NAME = "users_collection"
repo = MongodbUserRepository(DATABASE_URL, DATABASE_NAME, COLLECTION_NAME)
user_factory = UserFactoryMongodbRepository(repo)


@app.route("/users", methods=["GET"])
def list_users():
    users = user_factory.list_all_users()
    formatted_users = [UserPresenter.format(user) for user in users]
    return jsonify(formatted_users), 200


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    response = user_factory.create_user(name, email)
    return jsonify({"message": response}), 201


@app.route("/users/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = User(
        id=user_id, name=data.get("name"), email=data.get("email")
    )  # assuming the ID comes from the URL
    response = user_factory.update_user(user)
    return jsonify({"message": response}), 200


@app.route("/users/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    response = user_factory.delete_user(user_id)
    return jsonify({"message": response}), 200


@app.route("/users/bulk", methods=["POST"])
def add_bulk_users():
    data = request.get_json()
    users_data = data.get("users", [])
    users = [User(name=user_data["name"], email=user_data["email"]) for user_data in users_data]
    response = user_factory.add_bulk_users(users)
    return jsonify({"message": response}), 201


@app.route("/users/bulk", methods=["DELETE"])
def delete_bulk_users():
    response = user_factory.delete_bulk_users()
    return jsonify({"message": response}), 200


if __name__ == "__main__":
    app.run()
