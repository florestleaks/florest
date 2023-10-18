# user_presenter.py


class UserPresenter:
    @staticmethod
    def format(data):
        return {"id": data.id, "name": data.name, "email": data.email}
