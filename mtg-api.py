import numpy as np
import pandas as pd
import requests
import json

url = "https://api.magicthegathering.io/v1/cards?set=GRN"
JSONContent = requests.get(url).json()
cards = JSONContent['cards']  # Array
newCardList = []
for card in cards:
  newCardList.append({
    'name': card['name'],
    'image': card['imageUrl'],
    'colors': card['colors'],
    'types': card['types'],
    'manaCost': card['manaCost']
    })
content = json.dumps(cards, indent=4, sort_keys=True)

dataset = pd.DataFrame(newCardList)
# dataset.to_csv('mtg.csv') # this is not working
