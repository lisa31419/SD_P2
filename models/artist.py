from res.db import db

disciplines = ('THEATRE', 'MUSIC', 'DANCE', 'CIRCUS', 'OTHER')


class DisciplineModel(db.Model):
    __tablename__ = 'disciplines'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    discipline = db.Column(db.Enum(*disciplines), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)


class ArtistModel(db.Model):
    __tablename__ = 'artists'  # This is table name

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    country = db.Column(db.String(30), nullable=False)
    disciplines = db.relationship("DisciplineModel", backref='artists')

    def __init__(self, name, country, discipline):
        self.name = name
        self.country = country
        self.discipline = discipline
