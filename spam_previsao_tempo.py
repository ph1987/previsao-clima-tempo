# -*- coding: utf-8 -*-
# spammer-bot
import json
import requests
import tweepy as tp
import time
import os

from datetime import datetime
from bs4 import BeautifulSoup as bs
from credentials import *

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth, wait_on_rate_limit=True)

class City:
    def __init__(self, city, tempmin, tempmax, descr, region, url):
        self.city = city
        self.tempmin = tempmin
        self.tempmax = tempmax
        self.descr = descr
        self.region = region
        self.url = "https://www.climatempo.com.br/previsao-do-tempo/" + url

cityList = []
with open('climatempo_maincities.json', 'r') as f:
    data = json.load(f)
    for c in data['cities']:
        cityList.append(City(c['name'],'','','',c['region'],c['url']))

for cl in cityList: 
    page = requests.get(cl.url)
    soup = bs(page.text, 'html.parser')
    try:
        cl.tempmax = soup.find(id="tempMax0").get_text()
    except:
        pass

    try:
        cl.tempmin = soup.find(id="tempMin0").get_text()
    except:
        pass

    try:
        cl.descr = soup.find(class_="left top5 mobile-columns font14 txt-black").get_text()
    except:
        pass

with open('temp.txt', 'w') as f:
    for item in cityList:
        f.write(item.city + " " + "⬆️" + item.tempmax + "⬇️" + item.tempmin + '\n')
        print(item.city + " ️️️️⬆️ " + item.tempmax + " ️⬇️ " + item.tempmin)

with open('temp.txt','r') as f:
   api.update_status(f.read())
