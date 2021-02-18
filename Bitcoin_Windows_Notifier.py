import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

def Bitcoin_Price_Scraper(country):
    while True:
        url = 'https://www.google.com/search?&q=bitcoin price in '+ country
        req = requests.get(url)
        scrap = BeautifulSoup(req.text, 'html.parser')
        bitcoin_price = scrap.find("div",class_="BNeawe iBp4i AP7Wnd").text
        print(bitcoin_price)
        notification.notify(
            title="Bitcoin Price Notifier",
            message=str(bitcoin_price),
            app_icon='Currency.ico',
            timeout=10
        )
        time.sleep(300)

Bitcoin_Price_Scraper('USA')