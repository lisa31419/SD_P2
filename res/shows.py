import dateutil
from flask_restful import reqparse, Resource

from models.artist import ArtistModel
from models.show import ShowModel
from models.accounts import *
from res.db import db


class Show(Resource):
    def get(self, id):
        show = ShowModel.find_by_id(id)
        if show is not None:
            return {'show': show.json()}, 200
        else:
            return 404

    @auth.login_required(role='admin')
    def post(self, id=None):
        data = self.getData()

        if id is None:
            id = ShowModel.length() + 1

        if self.get(id) == 404:
            new_show = ShowModel(data['name'], data['date'], data['price'], data['total_available_tickets'])
            try:
                new_show.save_to_db()
                return {'message': "Show with id [{}] added correctly".format(id)}
            except:
                return {"message": "An error occurred inserting the show."}, 500

        else:
            return {'message': "Show with id [{}] already exists".format(id)}

    @auth.login_required(role='admin')
    def delete(self, id):
        if id is None or self.get(id) == 404:
            return {'message': "Id must be in the list"}, 404
        show_to_delete = ShowModel.find_by_id(id)

        try:
            show_to_delete.delete_from_db()
            return {'message': "Show with id [{}] deleted correctly".format(id)}
        except:
            return {'message': "Error while deleting the show"}, 500

    @auth.login_required(role='admin')
    def put(self, id):
        print("he entrado en el put")
        data = self.getData()
        print("he pasado el data")

        if self.get(id) == 404:
            self.post(id)
            return {'message': "Show with id [{}] will be created".format(id)}
        else:
            print("estoy en el else")
            show_to_update = ShowModel.find_by_id(id)
            show_to_update.name = data['name']
            print(data['date'])
            show_to_update.date = dateutil.parser.parse(data['date'])
            show_to_update.price = data['price']
            print(data['total_available_tickets'])
            show_to_update.total_available_tickets = data['total_available_tickets']
            db.session.commit()
            return {'message': "Show with id [{}] updated".format(id)}

    def getData(self):
        parser = reqparse.RequestParser()  # create parameters parser from request

        # define all input parameters need and its type

        parser.add_argument('name', type=str, required=True, help="This field cannot be left blanck")
        parser.add_argument('date', type=str)
        parser.add_argument('price', type=float)
        parser.add_argument('total_available_tickets', type=int)
        parser.add_argument('place', type=str,
                            action="append")  # action = "append" is needed to determine that is a list of strings
        parser.add_argument('artist', type=str,
                            action="append")  # action = "append" is needed to determine that is a list of strings

        data = parser.parse_args()
        return data


class ShowList(Resource):
    def get(self):
        return {'shows': [x.json() for x in ShowModel.get_all()]}


class ShowArtistsList(Resource):
    def get(self, id):
        artists_in_show = ShowModel.find_by_id(id).artists
        if artists_in_show:
            return [x.json() for x in artists_in_show], 200
        else:
            return {"message": "There are no artists in this show."}, 404


class ShowArtist(Resource):
    def get(self, id_show, id_artist):
        artists_in_show = ShowModel.find_by_id(id_show).artists
        artist_found = [x.json() for x in artists_in_show if str(x.id) == id_artist]
        if artist_found:
            return {'artist': artist_found}, 200
        else:
            return {"message": "There are no artists with id [{}] in this show.".format(id_artist)}, 404

    def post(self, id_show, id_artist=None):
        # data = Artist.getData(self)
        show_found = ShowModel.find_by_id(id_show)
        artists_in_show = show_found.artists
        if id_artist is None:
            id_artist = ArtistModel.length() + 1

        if ArtistModel.find_by_id(id_artist) is None:
            # new_artist = ArtistModel(data['name'], data['country'], data['disciplines'])
            try:
                # new_artist.save_to_db()
                # artists_in_show.append(new_artist)
                # show_found.save_to_db()
                return {'message': "Artist with id [{}] created and added correctly to the show.".format(
                    id_artist)}, 200
            except:
                return {"message": "An error occurred inserting the new artist into the show."}, 500

        else:
            artist_found = ArtistModel.find_by_id(id_artist)
            try:
                artists_in_show.append(artist_found)
                show_found.save_to_db()
                return {'message': "Artist with id [{}] added correctly to the show.".format(id_artist)}, 200
            except:
                return {"message": "An error occurred inserting the artist into the show."}, 500

    def delete(self, id_show, id_artist):
        show_found = ShowModel.find_by_id(id_show)
        artists_in_show = show_found.artists
        artist_to_delete = [x for x in artists_in_show if str(x.id) == id_artist]
        if artist_to_delete:
            artist_to_delete = ArtistModel.find_by_id(id_artist)
            artists_in_show.remove(artist_to_delete)
            show_found.save_to_db()
            return {'message': "Artist with id [{}] deleted correctly from the show".format(id_artist)}, 200
        else:
            return {'message': "Artist must be in the show"}, 404
