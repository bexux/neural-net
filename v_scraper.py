from bs4 import BeautifulSoup
import requests
import pandas as pd

# TODO: Need to add user input for url to scrape
page = requests.get("https://www.ebay.com/b/MTG-Individual-Cards/38292?Card%2520Type=Creature&Color=White&Language=English&Set=Guilds%2520of%2520Ravnica&rt=nc")
page2 = requests.get("https://www.ebay.com/b/MTG-Individual-Cards/38292?Card%2520Type=Creature&Color=White&Language=English&Set=Guilds%2520of%2520Ravnica&rt=nc&_pgn=2")
greenCreatures = requests.get("https://www.ebay.com/b/MTG-Individual-Cards/38292?Card%2520Type=Creature&Color=Green&Language=English&Set=Guilds%2520of%2520Ravnica&rt=nc")
greenCreatures2 = requests.get("https://www.ebay.com/b/MTG-Individual-Cards/38292?Card%2520Type=Creature&Color=Green&Language=English&Set=Guilds%2520of%2520Ravnica&rt=nc&_pgn=2")
greenCreatures3 = requests.get("https://www.ebay.com/b/MTG-Individual-Cards/38292?Card%2520Type=Creature&Color=Green&Language=English&Set=Guilds%2520of%2520Ravnica&rt=nc&_pgn=3")

soup = BeautifulSoup(page.content, 'html.parser')
soup_page2 = BeautifulSoup(page2.content, 'html.parser')
green_soup = BeautifulSoup(greenCreatures.content, 'html.parser')
green_soup_page2 = BeautifulSoup(greenCreatures2.content, 'html.parser')
green_soup_page3 = BeautifulSoup(greenCreatures3.content, 'html.parser')

# These comments are left here to show previous steps - and help with debugging
# Guarantee the page call works
# print(page.status_code)

# This returns an array ['html', '\n', 'actual html']
# print(list(soup.children))

# This will tell you the types:
# print([type(item) for item in list(soup.children)])

# html = list(soup.children)[2]
# print(list(soup.children))

# Now find the children in the html - returns Array
# ['\n', <head><title></title></head>, '\n', <body>] etc
# print(list(html.children))

# body = list(html.children)[3]

# Now find the children in the body - returns Array
# ['\n', <p>Here is some simple content.</p>, '\n']
# print(list(body.children))

# p = list(body.children)[1]
# text = p.get_text()
# print(text)

whiteCreatureList = soup.find_all(class_="s-item__link")
whiteCreatureList2 = soup_page2.find_all(class_="s-item__link")
greenCreatureList = green_soup.find_all(class_="s-item__link")
greenCreatureList2 = green_soup_page2.find_all(class_="s-item__link")
greenCreatureList3 = green_soup_page3.find_all(class_="s-item__link")

urlList = []
nameList = []
colorList = []
for item in whiteCreatureList:
    urlList.append(item['href'])
    nameList.append(item.get_text())
    colorList.append("white")

for wht in whiteCreatureList2:
    urlList.append(wht['href'])
    nameList.append(wht.get_text())
    colorList.append("white")

for grn in greenCreatureList:
    urlList.append(grn['href'])
    nameList.append(grn.get_text())
    colorList.append("green")

for grn in greenCreatureList2:
    urlList.append(grn['href'])
    nameList.append(grn.get_text())
    colorList.append("green")

for grn in greenCreatureList3:
    urlList.append(grn['href'])
    nameList.append(grn.get_text())
    colorList.append("green")

cards = pd.DataFrame({
  "name": nameList,
  "image_url": urlList,
  "color": colorList
})

print(len(cards))
print(cards)
