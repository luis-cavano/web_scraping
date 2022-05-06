import requests
import schedule
import csv
from datetime import datetime
from bs4 import BeautifulSoup


def job(): 
    url1 = requests.get('https://coinmarketcap.com/pt-br/currencies/bitcoin/')
    #print(url1.status_code)
    htmlBruto1 = url1.content
    site = BeautifulSoup(htmlBruto1, 'html.parser')
    tagPreco = site.find('div', attrs={'class':'priceValue smallerPrice'})
    #print(tagPreco)
    preco = tagPreco.find('span')

    time = datetime.now()

    dict_1 = {
    "preco" : preco.text,
    "data" : time,
    }
       
    print()
    print(dict_1)
    print()

#schedule.every(2).minutes.do(job)
schedule.every(5).seconds.do(job)
    
while True:
    schedule.run_pending()
    #time.sleep(0)
