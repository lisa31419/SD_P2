from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models.artist import ArtistModel
from models.show import ShowModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

# ADD DATA FOR TESTING

new_artist1 = ArtistModel('La Calòrica', 'Spain', 'THEATRE')
new_artist2 = ArtistModel('Txarango', 'Spain', 'MUSIC')

db.session.add(new_artist1)
db.session.add(new_artist2)
db.session.commit()

new_show1 = ShowModel('El gran Circ', datetime.strptime('2021-07-04', "%Y-%m-%d"), '50.0')
db.session.add(new_show1)
db.session.commit()
