from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from res.artists import Artist, ArtistList
from res.db import db
from res.places import Place, PlaceList
from res.shows import Show, ShowList, ShowArtistsList, ShowArtist

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

api.add_resource(Artist, '/artist/<int:id>', '/artist')
api.add_resource(ArtistList, '/artists')
#api.add_resource(ArtistShowsList, '/artist/<int:id>/shows')

api.add_resource(Show, '/show/<int:id>', '/show')
api.add_resource(ShowList, '/shows')
api.add_resource(ShowArtistsList, '/show/<int:id>/artists')
api.add_resource(ShowArtist, '/show/<int:id_show>/artist/<id_artist>','/show/<int:id_show>/artist')

api.add_resource(Place, '/place/<int:id>', '/place')
api.add_resource(PlaceList, '/places')
#api.add_resource(PlaceShowsList, '/place/<int:id>/shows')

if __name__ == '__main__':
    app.run(port=5000, debug=False)
