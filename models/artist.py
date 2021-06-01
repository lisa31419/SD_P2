from db import db

disciplines = ('THEATRE', 'MUSIC', 'DANCE', 'CIRCUS', 'OTHER')


class DisciplineModel(db.Model):
    __tablename__ = 'disciplines'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    discipline = db.Column(db.Enum(*disciplines, name='disciplines_types'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship("ArtistModel")

    def __init__(self, discipline):
        self.discipline = discipline

    def json(self):
        return {'discipline': self.discipline}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter(DisciplineModel.artist_id == id).all()


class ArtistModel(db.Model):
    __tablename__ = 'artists'  # This is table name

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    country = db.Column(db.String(30), nullable=False)

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def json(self):
        disciplineList = DisciplineModel.find_by_id(self.id)
        disciplineList = [d.discipline for d in disciplineList]
        return {'id': self.id, 'name': self.name, 'country': self.country,
                'disciplines': disciplineList}

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
    def find_by_name(cls, name):
        return cls.query.filter(ArtistModel.name == name).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def length(cls):
        return cls.query.count()
