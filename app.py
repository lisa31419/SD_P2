from flask import Flask
from flask_restful import Resource, Api, reqparse
from data import artists, shows, places

app = Flask(__name__)
api = Api(app)


class Artist(Resource):
    '''
    def __init__(self, data):
        self.id = id
        self.name = data['name']
        self.country = data['country']
        self.disciplines = data['disciplines']

    def dump(self):
        return {'id': self.id,
                'name': self.name,
                'country': self.country,
                'disciplines': self.disciplines}
    '''

    def get(self, id):
        artist = next(iter([x for x in artists if x["id"] == id]), None)
        if artist is not None:
            return {'artist': artist}, 200
        else:
            return 404

    def post(self, id=None):
        data = self.getData(id)

        if id is None:
            id = artists[len(artists) - 1]["id"] + 1

        if self.get(id) == 404:
            # new_artist
            artists.append({'id': id,
                            'name': data['name'],
                            'country': data['country'],
                            'disciplines': data['disciplines']})
            return {'message': "Artist with id [{}] added correctly".format(id)}
        else:
            return {'message': "Artist with id [{}] already exists".format(id)}

    def delete(self, id):
        if id is None or self.get(id) == 404:
            return {'message': "Id must be in the list"}, 404
        artists.pop(id)
        return {'message': "Artist with id [{}] deleted correctly".format(id)}

    def put(self, id=None):
        data = self.getData(id)

        if self.get(id) == 404:
            self.post(id)
            return {'message': "Artist with id [{}] will be created".format(id)}
        else:
            artists[id] = {'id': id,
                           'name': data['name'],
                           'country': data['country'],
                           'disciplines': data['disciplines']}
            return {'message': "Artist with id [{}] updated".format(id)}

    def getData(self, id):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type

        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('country', type=str)
        parser.add_argument('disciplines', type=str,
                            action="append")  # action = "append" is needed to determine that is a list of strings

        data = parser.parse_args()
        return data


api.add_resource(Artist, '/artist/<int:id>', '/artist')

if __name__ == '__main__':
    app.run(port=5000, debug=False)
