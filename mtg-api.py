import requests
import json

url = "https://api.magicthegathering.io/v1/cards"
JSONContent = requests.get(url).json()
cards = JSONContent['cards']  # Array

# save to json file
with open('mtgcard.json', 'w') as outfile:
    json.dump(cards, outfile)
