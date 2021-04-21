import dateutil.parser

from res.db import db

artists_in_shows = db.Table('artists_in_shows',
                            db.Column('id', db.Integer, primary_key=True),
                            db.Column('artist_id', db.Integer, db.ForeignKey('artists.id')),
                            db.Column('show_id', db.Integer, db.ForeignKey('shows.id')))


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
        self.date = dateutil.parser.parse(date)
        self.price = price

    def json(self):
        formatted_datetime = self.date.isoformat()
        return {'id': self.id, 'name': self.name, 'date': formatted_datetime,
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

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def length(cls):
        return cls.query.count()

    @classmethod
    def getArtists(cls):
        return artists_in_shows
