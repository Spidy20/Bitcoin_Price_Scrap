import requests
from bs4 import BeautifulSoup
from plyer import notification

url = 'https://www.google.com/search?&q=bitcoin price in india'
req = requests.get(url)
scrap = BeautifulSoup(req.text, 'html.parser')
#BNeawe iBp4i AP7Wnd
bitcoin_price = scrap.find("div", class_="BNeawe iBp4i AP7Wnd").text
print(bitcoin_price)