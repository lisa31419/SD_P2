from res.db import db


class OrdersModel(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), db.ForeignKey('accounts.username'), nullable=False)
    id_show = db.Column(db.Integer, nullable=False)
    tickets_bought = db.Column(db.Integer, nullable=False)

    def __init__(self, id_show, tickets_bought):
        self.id_show = id_show
        self.tickets_bought = tickets_bought

    @classmethod
    def find_by_username(cls, username):
        return cls.query.get(username)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def length(cls):
        return cls.query.count()



