from flask import jsonify

from res.data import places
from res.db import db

'''
class PlaceList:
    def placesList(self):
        return jsonify([str(x) for x in places])
'''

class PlaceModel(db.Model):
    __tablename__ = 'places'  # This is table name
    __table_args__ = (db.UniqueConstraint('name', 'city', 'country', 'capacity'),)  # Extracted comma

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    city = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(30), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    # show_id = db.Column(db.Integer, db.ForeignKey('shows.id'), nullable=False)

    def __init__(self, name, city, country, capacity):
        self.name = name
        self.city = city
        self.country = country
        self.capacity = capacity

    def json(self):
        return {'id': self.id, 'name': self.name, 'city': self.city,
                'country': self.country, 'capacity': self.capacity}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id)
