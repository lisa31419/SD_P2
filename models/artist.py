from res.db import db

disciplines = ('THEATRE', 'MUSIC', 'DANCE', 'CIRCUS', 'OTHER')


class ArtistModel(db.Model):
    __tablename__ = 'artists'  # This is table name
    __table_args__ = (db.UniqueConstraint('name', 'country', 'discipline'),)  # Extracted comma

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    country = db.Column(db.String(30), nullable=False)
    discipline = db.Column(db.Enum(*disciplines), nullable=False)

    def __init__(self, name, country, discipline):
        self.name = name
        self.country = country
        self.discipline = discipline
