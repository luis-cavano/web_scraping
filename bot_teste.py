import requests
import schedule
import json
import time
from datetime import datetime
from bs4 import BeautifulSoup

def job(): 

    urlMongo = "https://data.mongodb-api.com/app/data-pkmib/endpoint/data/beta/action/findOne"

    url = requests.get('https://coinmarketcap.com/pt-br/currencies/bitcoin/')
    htmlBruto = url.content
    site = BeautifulSoup(htmlBruto, 'html.parser')
    tagPreco = site.find('div', attrs={'class':'priceValue smallerPrice'})
    preco = tagPreco.find('span')
    time = datetime.now()
    salvar = [preco.text, str(time)]

    payload = json.dumps({
    "collection": "routes",
    "database": "sample_training",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1
    }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'bWdELScAUp4oSoDmVLyoOPIKosx0VqCpJpQdlgzuWq9HW2R8MqRXNDcyxLtpB59A'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

schedule.every(2).minutes.do(job)
    
while True:
    schedule.run_pending()
    #time.sleep(0)