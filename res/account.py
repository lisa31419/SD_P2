from flask_restful import reqparse, Resource

from models.accounts import *
from res.order import Orders
from lock import lock


class Accounts(Resource):
    def get(self, username):
        account = AccountsModel.find_by_username(username)
        if account is not None:
            return {'account': account.json()}, 200
        else:
            return {'message': 'This account does not exist'}, 404

    def post(self):
        data = self.getData()
        username = data['username']
        password = data['password']
        with lock.lock:
            response = self.get(username)
            if response[1] == 404:
                try:
                    new_user = AccountsModel(username)
                    new_user.hash_password(password)
                    new_user.save_to_db()
                    return new_user.json()
                except:
                    return {"message": "An error occurred inserting the user."}, 500

            else:
                return {'message': "Error username introduced exists"}

    @auth.login_required(role='admin')
    def delete(self, username):
        with lock.lock:
            response = self.get(username)
            if username is None or response[1] == 404:
                return {'message': "Username must be in the list"}, 404
            user_to_delete = AccountsModel.find_by_username(username)

            try:
                orders_to_delete = Orders.get(user_to_delete)
                for order in orders_to_delete:
                    order.delete_from_db()

                user_to_delete.delete_from_db()
                return {'message': "User [{}] and its orders deleted correctly".format(username)}
            except:
                return {'message': "Error while deleting user or orders"}, 500

    def getData(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type

        parser.add_argument('username', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('password', type=str, required=True, help="This field cannot be left blanck")

        data = parser.parse_args()
        return data


class AccountsList(Resource):
    @auth.login_required(role='admin')
    def get(self):
        return {'accounts': [x.json() for x in AccountsModel.get_all()]}
