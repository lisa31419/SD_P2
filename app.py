from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from res.artists import Artist, ArtistList
from res.db import db
from res.places import Place, PlaceList
from res.shows import Show, ShowList

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

api.add_resource(Artist, '/artist/<int:id>', '/artist')
api.add_resource(ArtistList, '/artists')

api.add_resource(Show, '/show/<int:id>', '/show')
api.add_resource(ShowList, '/shows')

api.add_resource(Place, '/place/<int:id>', '/place')
api.add_resource(PlaceList, '/places')

if __name__ == '__main__':
    app.run(port=5000, debug=False)
