from flask_restful import Resource, reqparse

from lock import lock
from models.accounts import AccountsModel
from res.db import db


class Login(Resource):
    def post(self):
        data = self.getData()
        with lock.lock:
            username = data['username']
            password = data['password']

            username_found = AccountsModel.find_by_username(username)

            if username_found is None:
                return {"message": "An error occurred with username's search"}, 404

            if not username_found.verify_password(password):
                return {"message": "An error occurred inserting the user."}, 400

            token = AccountsModel.generate_auth_token(username_found)
            return {'token': token.decode('ascii')}, 200

    def getData(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type

        parser.add_argument('username', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        return data
