from flaskapp import db, login_manager
from flask_login import UserMixin
import json

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def upload_some_cards():
    print('hello')
    json_file = open('mtgcard.json')
    carddata = json.load(json_file)
    firstItem = carddata[0]
    secondItem = carddata[1]
    newListTest = []
    newListTest.append(firstItem)
    newListTest.append(secondItem)
    print(firstItem['imageUrl'])
    cardList = []
    for card in newListTest:
        new_entry = Card(
            name=card['name'],
            power=card['power'],
            toughness=card['toughness'],
            manaCost=card['manaCost']
            # image=card['imageUrl']
            # card_types=card['types'],
            # card_sub_type=card['subtypes']
        )
        cardList.append(new_entry)

    db.session.add_all(cardList)
    db.session.commit()

user_card_assoc = db.Table('card_user_assoc',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('card_id', db.Integer, db.ForeignKey('card.id'))
)

card_type_assoc = db.Table('card_type_assoc',
    db.Column('card_id', db.Integer, db.ForeignKey('card.id')),
    db.Column('card_type', db.Integer, db.ForeignKey('card_type.id'))
)

card_sub_type_assoc = db.Table('card_sub_type_assoc',
    db.Column('card_id', db.Integer, db.ForeignKey('card.id')),
    db.Column('card_type', db.Integer, db.ForeignKey('card_sub_type.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    cards = db.relationship('Card', secondary=user_card_assoc, backref=db.backref('owners'), lazy='dynamic')

    def __repr__(self):
        return 'User:' + self.username

class Card(db.Model):
    __tablename__ = 'card'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    power = db.Column(db.Integer)
    toughness = db.Column(db.Integer)
    manaCost = db.Column(db.String(10))
    image = db.Column(db.String(80), nullable=False, default='default_card.jpg')
    card_types = db.relationship('CardType', secondary=card_type_assoc, backref=db.backref('cards'), lazy='dynamic')
    card_sub_types = db.relationship('CardSubType', secondary=card_sub_type_assoc, backref=db.backref('cards'), lazy='dynamic')
 
    def __repr__(self):
        return 'Card:' + self.name

class CardType(db.Model):
    __tablename__ = 'card_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

class CardSubType(db.Model):
    __tablename__ = 'card_sub_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)