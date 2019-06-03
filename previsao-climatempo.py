# scraping for weather
import json
import requests
from bs4 import BeautifulSoup as bs
#sunbehindcloudwithrain = 🌦️
#sunbehindlargecloud = 🌥️
#sunsmallcloud = 🌤️
#rain = 🌧️
#rainthunder = ⛈️

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

for item in cityList:
    print(item.city + " ️️️️⬆️ " + item.tempmax + " ️⬇️ " + item.tempmin)
'''
SEList = (x for x in cityList if x.region == "Sudeste")
for item in SEList:
    print(item.city + " ️️️️⬆️ " + item.tempmax + " ️⬇️ " + item.tempmin + " " + item.descr)
'''