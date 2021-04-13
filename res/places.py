from flask_restful import reqparse, Resource

from res.data import places


class Place(Resource):
    def get(self, id):
        place = next(iter([x for x in places if x["id"] == id]), None)
        if place is not None:
            return {'place': place}, 200
        else:
            return 404

    def post(self, id=None):
        data = self.getData()

        if id is None:
            id = places[len(places) - 1]["id"] + 1

        if self.get(id) == 404:
            # new_place
            places.append({'id': id,
                           'name': data['name'],
                           'city': data['city'],
                           'country': data['country'],
                           'capacity': data['capacity']})
            return {'message': "Place with id [{}] added correctly".format(id)}
        else:
            return {'message': "Place with id [{}] already exists".format(id)}

    def delete(self, id):
        if id is None or self.get(id) == 404:
            return {'message': "Id must be in the list"}, 404
        places.pop(id)
        return {'message': "Place with id [{}] deleted correctly".format(id)}

    def put(self, id):
        data = self.getData()

        if self.get(id) == 404:
            self.post(id)
            return {'message': "Place with id [{}] will be created".format(id)}
        else:
            places[id] = {'id': id,
                          'name': data['name'],
                          'city': data['city'],
                          'country': data['country'],
                          'capacity': data['capacity']}
            return {'message': "Place with id [{}] updated".format(id)}

    def getData(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type

        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('city', type=str)
        parser.add_argument('country', type=str)
        parser.add_argument('capacity', type=int)

        data = parser.parse_args()
        return data
