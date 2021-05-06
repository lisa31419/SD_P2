from flask import Flask
from flask import render_template
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from res.login import Login
from res.account import Accounts, AccountsList
from res.artists import Artist, ArtistList, ArtistShowsList
from res.db import db, secret_key
from res.order import OrdersList, Orders
from res.places import Place, PlaceList, PlaceShowsList
from res.shows import Show, ShowList, ShowArtistsList, ShowArtist

app = Flask(__name__,
            static_folder="session3Vue/SDWebFrontEnd/dist/static",
            template_folder="session3Vue/SDWebFrontEnd/dist")

app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key

CORS(app, resources={r'/*': {'origins': '*'}})

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

api.add_resource(Artist, '/artist/<int:id>', '/artist')
api.add_resource(ArtistList, '/artists')
api.add_resource(ArtistShowsList, '/artist/<int:id>/shows')

api.add_resource(Show, '/show/<int:id>', '/show')
api.add_resource(ShowList, '/shows')
api.add_resource(ShowArtistsList, '/show/<int:id>/artists')
api.add_resource(ShowArtist, '/show/<int:id_show>/artist/<id_artist>', '/show/<int:id_show>/artist')

api.add_resource(Place, '/place/<int:id>', '/place')
api.add_resource(PlaceList, '/places')
api.add_resource(PlaceShowsList, '/place/<int:id>/shows')

api.add_resource(Orders, '/order/<string:username>')
api.add_resource(OrdersList, '/orders', '/orders/<string:username>/')

api.add_resource(Accounts, '/account/<string:username>', '/account')
api.add_resource(AccountsList, '/accounts')

api.add_resource(Login, '/login')

@app.route('/')
def render_vue():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=5000, debug=False)
