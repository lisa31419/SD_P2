from flask_restful import reqparse, Resource

from res.data import shows


class Show(Resource):
    def get(self, id):
        show = next(iter([x for x in shows if x["id"] == id]), None)
        if show is not None:
            return {'show': show}, 200
        else:
            return 404

    def post(self, id=None):
        data = self.getData()

        if id is None:
            id = shows[len(shows) - 1]["id"] + 1

        if self.get(id) == 404:
            # new_show
            shows.append({'id': id,
                          'name': data['name'],
                          'date': data['date'],
                          'place': data['place'],
                          'artist': data['artist']})
            return {'message': "Show with id [{}] added correctly".format(id)}
        else:
            return {'message': "Show with id [{}] already exists".format(id)}

    def delete(self, id):
        if id is None or self.get(id) == 404:
            return {'message': "Id must be in the list"}, 404
        shows.pop(id)
        return {'message': "Show with id [{}] deleted correctly".format(id)}

    def put(self, id):
        data = self.getData()

        if self.get(id) == 404:
            self.post(id)
            return {'message': "Show with id [{}] will be created".format(id)}
        else:
            shows[id] = {'name': data['name'],
                         'date': data['date'],
                         'place': data['place'],
                         'artist': data['artist']}
            return {'message': "Show with id [{}] updated".format(id)}

    def getData(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type

        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('date', type=str)
        parser.add_argument('place', type=str,
                            action="append")  # action = "append" is needed to determine that is a list of strings
        parser.add_argument('artist', type=str,
                            action="append")  # action = "append" is needed to determine that is a list of strings

        data = parser.parse_args()
        return data
