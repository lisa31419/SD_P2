from flask import jsonify
from flask_restful import reqparse, Resource

from models.artist import ArtistModel
from models.show import ShowModel
from models.accounts import *
from res.db import db


class Artist(Resource):

    def get(self, id):
        artist = ArtistModel.find_by_id(id)
        if artist is not None:
            return {'artist': artist.json()}, 200
        else:
            return 404

    @auth.login_required(role='admin')
    def post(self, id=None):
        data = self.getData()

        if id is None:
            id = ArtistModel.length() + 1

        if self.get(id) == 404:
            new_artist = ArtistModel(data['name'], data['country'], data['disciplines'])
            try:
                new_artist.save_to_db()
                return id, 200
            except:
                return {"message": "An error occurred inserting the artist."}, 500

        else:
            return id, 409

    @auth.login_required(role='admin')
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
            # artist_to_update.disciplines = data['disciplines']
            try:
                db.session.commit()
                return {'message': "Artist with id [{}] updated".format(id)}
            except:
                return {'message': "Error while commiting changes"}

    def getData(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type

        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('country', type=str)
        parser.add_argument('disciplines', type=str,
                            action="append")  # action = "append" is needed to determine that is a list of strings

        data = parser.parse_args()
        return data


class ArtistList(Resource):
    def get(self):
        return jsonify([x.json() for x in ArtistModel.get_all()])


class ArtistShowsList(Resource):
    def get(self, id):
        shows = ShowModel.get_all()
        shows_played_by_artist = []
        for show in shows:
            artists_in_show = show.artists
            for artist in artists_in_show:
                if artist.id == id:
                    shows_played_by_artist.append(show)

        if shows_played_by_artist:
            return [x.json() for x in shows_played_by_artist], 200
        else:
            return {"message": "There are no shows played by this artist."}, 404
