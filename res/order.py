from flask_restful import Resource, reqparse

from models.accounts import AccountsModel
from models.orders import OrdersModel
from models.show import ShowModel
from res.db import db


class Orders(Resource):
    def get(self, username):
        order = OrdersModel.find_by_username(username)
        if order is not None:
            return {'order': order.json()}, 200
        else:
            return 404

    def post(self, username):
        data = self.getData()
        id_show = data['id_show']
        tickets_bought = data['tickets_bought']

        if self.get(username) == 404:
            user = AccountsModel.find_by_username(username)
            show = ShowModel.find_by_id(id_show)
            shows_price = show.price
            users_money = user.available_money
            available_tickets = show.total_available_tickets

            if shows_price < users_money and available_tickets > 0:
                try:
                    available_tickets -= 1
                    users_money -= (shows_price * tickets_bought)
                    new_order = OrdersModel(id_show, tickets_bought)
                    user.orders.append(new_order)
                    # es posible que falte un db.session.add(self) cambiando self por algo
                    db.session.commit()
                    return {'order': new_order}
                except:
                    db.session.rollback()
                    return {"message": "An error occurred inserting the order."}, 500

        else:
            return {'message': "Order already exists"}

    def getData(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument('id_show', type=int, required=True)
        parser.add_argument('tickets_bought', type=int, required=True)

        data = parser.parse_args()
        return data


class OrdersList(Resource):
    def get(self):
        return [x.json() for x in OrdersModel.get_all()]
