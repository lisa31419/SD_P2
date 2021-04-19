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

    place = db.relationship("PlaceModel", backref='shows')  # Revisar el Many to One

    def __init__(self, name, date, price):
        self.name = name
        self.date = date
        self.price = price
