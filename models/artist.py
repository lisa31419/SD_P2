from res.db import db

disciplines = ('THEATRE', 'MUSIC', 'DANCE', 'CIRCUS', 'OTHER')


class DisciplineModel(db.Model):
    __tablename__ = 'disciplines'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    discipline = db.Column(db.Enum(*disciplines), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship("ArtistModel")

    def __init__(self, discipline):
        self.discipline = discipline

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class ArtistModel(db.Model):
    __tablename__ = 'artists'  # This is table name

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    country = db.Column(db.String(30), nullable=False)

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def json(self):
        return {'id': self.id, 'name': self.name, 'country': self.country}#,
                #'disciplines': [discipline.json() for discipline in self.disciplines]}

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
