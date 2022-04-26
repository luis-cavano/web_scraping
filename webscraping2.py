import requests
import schedule
import time
from bs4 import BeautifulSoup

def job(): 
    url1 = requests.get('https://coinmarketcap.com/pt-br/currencies/bitcoin/')
    #print(url1.status_code)

    htmlBruto1 = url1.content
    site = BeautifulSoup(htmlBruto1, 'html.parser')
    tagPreco = site.find('div', attrs={'class':'priceValue smallerPrice'})
    #print(tagPreco)
    preco = tagPreco.find('span')

    print()
    print(preco.text)
    print()

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)