from res.db import db


class ShowModel(db.Model):
    __tablename__ = 'shows'  # This is table name
    __table_args__ = (db.UniqueConstraint('name', 'date', 'price'),)  # Extracted comma

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, date, price):
        self.name = name
        self.country = date
        self.discipline = price
