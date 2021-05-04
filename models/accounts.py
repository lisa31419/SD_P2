from res.db import db


class AccountsModel(db.Model):
    __tablename__ = 'accounts'

    username = db.Column(db.String(30), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    is_admin = db.Column(db.Integer, nullable=False)  # 0 not admin / 1 is admin
    available_money = db.Column(db.Integer)
    orders = db.relationship('OrdersModel', backref='orders', lazy=True)

    def __init__(self, username, available_money=200, is_admin=0):
        self.username = username
        self.available_money = available_money
        self.is_admin = is_admin
        self.password = 'test'

    def json(self):
        return {'username': self.username,
                'available money': self.available_money,
                'is admin?': self.is_admin}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.get(username)