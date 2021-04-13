from flask import Flask, jsonify
from flask_restful import Api

from res.data import artists, places, shows
from res.artists import Artist
from res.places import Place
from res.shows import Show

app = Flask(__name__)
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
