from flask import jsonify
from flask_restful import reqparse, Resource

from models.place import PlaceModel
from models.show import ShowModel
from res.db import db


class Place(Resource):
    def get(self, id):
        place = PlaceModel.find_by_id(id)
        if place is not None:
            return {'place': place.json()}, 200
        else:
            return 404

    def post(self, id=None):
        data = self.getData()

        if id is None:
            id = PlaceModel.legth() + 1

        if self.get(id) == 404:
            new_place = PlaceModel(data['name'], data['city'], data['country'], data['capacity'])
            try:
                new_place.save_to_db()
                return {'message': "Place with id [{}] added correctly".format(id)}
            except:
                return {"message": "An error occurred inserting the place."}, 500

        else:
            return {'message': "Place with id [{}] already exists".format(id)}

    def delete(self, id):
        if id is None or self.get(id) == 404:
            return {'message': "Id must be in the list"}, 404
        place_to_delete = PlaceModel.find_by_id(id)
        place_to_delete.delete_from_db()
        return {'message': "Place with id [{}] deleted correctly".format(id)}

    def put(self, id):
        data = self.getData()

        if self.get(id) == 404:
            self.post(id)
            return {'message': "Place with id [{}] will be created".format(id)}
        else:
            place_to_update = PlaceModel.find_by_id(id)
            place_to_update.name = data['name']
            place_to_update.city = data['city']
            place_to_update.country = data['country']
            place_to_update.capacity = data['capacity']
            try:
                db.session.commit()
                return {'message': "Place with id [{}] updated".format(id)}
            except:
                return {'message': "Error while commiting changes"}

    def getData(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type

        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('city', type=str)
        parser.add_argument('country', type=str)
        parser.add_argument('capacity', type=int)

        data = parser.parse_args()
        return data


class PlaceList(Resource):
    def get(self):
        return jsonify([x.json() for x in PlaceModel.get_all()])


class PlaceShowsList(Resource):
    def get(self):
        shows = ShowModel.get_all()
        shows_in_place = []
        for show in shows:
            places_in_show = show.places
            for place in places_in_show:
                if place.id == id:
                    shows_in_place.append(place)

        if shows_in_place:
            return [x.json() for x in shows_in_place], 200
        else:
            return {"message": "There are no shows performed in this place."}, 404
