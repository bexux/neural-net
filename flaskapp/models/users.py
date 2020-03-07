from flaskapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

user_card_assoc = db.Table('user_card_assoc',
    db.Column('card_id', db.Integer, db.ForeignKey('card.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

# TODO: add deck assoc

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    cards = db.relationship('Card', secondary=user_card_assoc, backref=db.backref('owners', lazy='dynamic'))

    def __repr__(self):
        return 'User:' + self.username