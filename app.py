from flask import Flask, jsonify
from flask_restful import Api
from flask_migrate import Migrate

from res.data import artists, places, shows
from res.artists import Artist
from res.places import Place
from res.shows import Show
from models.artist import ArtistModel
from models.show import ShowModel  #also import table created with many-to-many relationship

from res.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

api.add_resource(Artist, '/artist/<int:id>', '/artist')
api.add_resource(Place, '/place/<int:id>', '/place')
api.add_resource(Show, '/show/<int:id>', '/show')


@app.route('/artists')
def artistsList():
    return jsonify([str(x) for x in artists])


@app.route('/places')
def placesList():
    return jsonify([str(x) for x in places])


@app.route('/shows')
def showsList():
    return jsonify([str(x) for x in shows])


if __name__ == '__main__':
    app.run(port=5000, debug=False)
