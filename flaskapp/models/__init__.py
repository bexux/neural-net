from flaskapp import db
from flaskapp.models.cards import Card, CardType, CardSubType
from sqlalchemy.orm.exc import NoResultFound
import json

# created this folder (aka module)
# split it into users and cards
# all user tables are in the right file
# all card related things are in the card file

def get_or_create(type_name, ModelClass):
    try:
        return ModelClass.query.filter_by(name=type_name).one()
    except NoResultFound as e:
        card_type = ModelClass(name=type_name)
        db.session.add(card_type)
        return card_type

def upload_some_cards(mtgcardfile):
    json_file = open(mtgcardfile)
    carddata = json.load(json_file)
    # firstItem = carddata[0]
    # secondItem = carddata[1]
    # newListTest = []
    # newListTest.append(firstItem)
    # newListTest.append(secondItem)
    # print(firstItem['imageUrl'])
    
    cardList = []

    # temp set to verify if the card shows up twice in the json
    added = set()
    for card in carddata:
        if card['name'] in added:
            continue
        print(card['name'])
        added.add(card['name'])
        new_entry = Card(
            name=card['name'],
            power=card.get('power'),
            toughness=card.get('toughness'),
            manaCost=card['manaCost'],
            image=card.get('imageUrl'),
            card_types=[get_or_create(type_name, CardType) for type_name in card['types']],
            card_sub_types=[get_or_create(type_name, CardSubType) for type_name in card['subtypes']]
        )
        cardList.append(new_entry)

    db.session.add_all(cardList)
    db.session.commit()


if __name__ == '__main__':
    upload_some_cards()