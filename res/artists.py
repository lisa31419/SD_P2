from flask_restful import reqparse, Resource

from res.db import db
from models.artist import ArtistModel


class Artist(Resource):
    def artistas(self):
        return db.session.query_property(ArtistModel)

    def get(self, id):
        artist = ArtistModel.find_by_id(id)
        if artist is not None:
            return {'artist': artist.json()}, 200
        else:
            return 404

    def post(self, id=None):
        data = self.getData()

        if self.get(id) == 404:
            new_artist = ArtistModel(data['name'], data['country'], data['disciplines'])
            new_artist.save_to_db()
            return {'message': "Artist added correctly"}
        else:
            return {'message': "Artist with id [{}] already exists".format(id)}

    def delete(self, id):
        if id is None or self.get(id) == 404:
            return {'message': "Id must be in the list"}, 404
        artists_to_delete = ArtistModel.find_by_id(id)
        artists_to_delete.delete_from_db()
        return {'message': "Artist with id [{}] deleted correctly".format(id)}

    def put(self, id=None):
        data = self.getData()

        if self.get(id) == 404:
            self.post(id)
            return {'message': "Artist with id [{}] will be created".format(id)}
        else:
            artist_to_update = ArtistModel.find_by_id(id)
            artist_to_update.name = data['name']
            artist_to_update.country = data['country']
            #artist_to_update.disciplines = data['disciplines']
            db.session.commit()
            return {'message': "Artist with id [{}] updated".format(id)}

    def getData(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type

        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('country', type=str)
        parser.add_argument('disciplines', type=str,
                            action="append")  # action = "append" is needed to determine that is a list of strings

        data = parser.parse_args()
        return data
