from flask import jsonify

from res.data import shows
from res.db import db
import dateutil.parser

artists_in_shows = db.Table('artists_in_shows',
                            db.Column('id', db.Integer, primary_key=True),
                            db.Column('artist_id', db.Integer, db.ForeignKey('artists.id')),
                            db.Column('show_id', db.Integer, db.ForeignKey('shows.id')))

'''
class ShowList:
    def showsList(self):
        return jsonify([str(x) for x in shows])
'''

class ShowModel(db.Model):
    __tablename__ = 'shows'  # This is table name
    __table_args__ = (db.UniqueConstraint('name', 'date', 'price'),)  # Extracted comma

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    price = db.Column(db.Float, nullable=False)

    artists = db.relationship("ArtistModel", secondary=artists_in_shows, backref=db.backref('shows'))

    # place_id = db.Column(db.Integer, db.ForeignKey('places.id'))
    # place = db.relationship("PlaceModel")

    def __init__(self, name, date, price):
        self.name = name
        self.date = date
        self.price = price

    def json(self):
        formatted_datetime = self.date.isoformat()
        jsondate = dateutil.parser.parse(formatted_datetime)
        return {'id': self.id, 'name': self.name, 'date': jsondate,
                'price': self.price}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)
