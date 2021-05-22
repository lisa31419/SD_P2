from flask_restful import Resource, reqparse

from models.accounts import *
from models.orders import OrdersModel
from models.show import ShowModel
from res.db import db


class Orders(Resource):
    def get(self, username):
        orders = [x.json() for x in OrdersModel.get_all() if x.username == username]
        if orders is not None:
            return {'orders': orders}, 200
        else:
            return 404

    @auth.login_required(role='user')
    def post(self, username):
        data = self.getData()
        with lock.lock:
            id_show = data['id_show']
            tickets_bought = data['tickets_bought']
            user = AccountsModel.find_by_username(username)
            if user.username is g.user.username:
                show = ShowModel.find_by_id(id_show)
                shows_price = show.price
                available_tickets = show.total_available_tickets
                users_money = user.available_money

                if shows_price < users_money and available_tickets > 0:
                    try:
                        show.total_available_tickets = available_tickets - 1
                        users_money -= (shows_price * tickets_bought)
                        user.available_money = users_money
                        new_order = OrdersModel(id_show, tickets_bought)
                        user.orders.append(new_order)
                        db.session.add(new_order)
                        db.session.commit()
                        return {'order': new_order.json()}
                    except:
                        db.session.rollback()
                        return {"message": "An error occurred inserting the order."}, 500
                else:
                    return {"message": "You don't have enough money or there aren't tickets left."}, 400
            else:
                return {'message': "User error in username."}, 400

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

    @auth.login_required(role='user')
    def post(self, username):
        data = self.getData()
        with lock.lock:
            orders = data['orders']
            user = AccountsModel.find_by_username(username)
            if user.username is g.user.username:
                for order in orders:
                    id_show = order['id_show']
                    tickets_bought = order['tickets_bought']
                    if tickets_bought == 0:
                        continue

                    show = ShowModel.find_by_id(id_show)
                    shows_price = show.price
                    available_tickets = show.total_available_tickets
                    users_money = user.available_money
                    if shows_price < users_money and available_tickets > 0:
                        try:
                            show.total_available_tickets = available_tickets - 1
                            users_money -= (shows_price * tickets_bought)
                            user.available_money = users_money
                            new_order = OrdersModel(id_show, tickets_bought)

                            user.orders.append(new_order)
                            db.session.add(new_order)
                        except:
                            db.session.rollback()
                            return {"message": "An error occurred inserting the order."}, 500
                    else:
                        return {"message": "You don't have enough money or there aren't tickets left."}, 400
                try:
                    db.session.commit()
                    return {'order': orders}, 200

                except:
                    db.session.rollback()
                    return {"message": "An error occurred committing the order."}, 500
            else:
                return {'message': "User error in username."}, 400

    def getData(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type
        parser.add_argument('orders', action='append', type=dict)

        data = parser.parse_args()
        return data
