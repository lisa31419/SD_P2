from flask import jsonify
from flask_restful import reqparse, Resource

from models.show import ShowModel
from res.db import db


class ShowList(Resource):
    def get(self):
        return jsonify([x.json() for x in ShowModel.get_all()])


class Show(Resource):
    def get(self, id):
        show = ShowModel.find_by_id(id)
        if show is not None:
            return {'show': show.json()}, 200
        else:
            return 404

    def post(self, id=None):
        data = self.getData()

        if id is None:
            id = ShowModel.length() + 1

        if self.get(id) == 404:
            print(data.keys())
            new_show = ShowModel(data['name'], data['date'], data['price'])
            try:
                new_show.save_to_db()
                return {'message': "Show with id [{}] added correctly".format(id)}
            except:
                return {"message": "An error occurred inserting the show."}, 500

        else:
            return {'message': "Show with id [{}] already exists".format(id)}

    def delete(self, id):
        if id is None or self.get(id) == 404:
            return {'message': "Id must be in the list"}, 404
        show_to_delete = ShowModel.find_by_id(id)
        show_to_delete.delete_from_db()
        return {'message': "Show with id [{}] deleted correctly".format(id)}

    def put(self, id):
        data = self.getData()

        if self.get(id) == 404:
            self.post(id)
            return {'message': "Show with id [{}] will be created".format(id)}
        else:
            show_to_update = ShowModel.find_by_id(id)
            show_to_update.name = data['name']
            show_to_update.date = data['date']
            show_to_update.price = data['price']
            # show_to_update.artist = data['artist']
            db.session.commit()
            return {'message': "Show with id [{}] updated".format(id)}

    def getData(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type

        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('date', type=str)
        parser.add_argument('price', type=float)
        parser.add_argument('place', type=str,
                            action="append")  # action = "append" is needed to determine that is a list of strings
        parser.add_argument('artist', type=str,
                            action="append")  # action = "append" is needed to determine that is a list of strings

        data = parser.parse_args()
        return data
