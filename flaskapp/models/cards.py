from flaskapp import db

card_type_assoc = db.Table('card_type_assoc',
    db.Column('card_id', db.Integer, db.ForeignKey('card.id')),
    db.Column('card_type', db.Integer, db.ForeignKey('card_type.id'))
)

card_sub_type_assoc = db.Table('card_sub_type_assoc',
    db.Column('card_id', db.Integer, db.ForeignKey('card.id')),
    db.Column('card_type', db.Integer, db.ForeignKey('card_sub_type.id'))
)

class CardType(db.Model):
    __tablename__ = 'card_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

class CardSubType(db.Model):
    __tablename__ = 'card_sub_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

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