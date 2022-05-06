import requests
import schedule
import json
import time
from datetime import datetime
from bs4 import BeautifulSoup

def job(): 

    url1 = requests.get('https://coinmarketcap.com/pt-br/currencies/bitcoin/')
    htmlBruto = url1.content
    site = BeautifulSoup(htmlBruto, 'html.parser')
    tagPreco = site.find('div', attrs={'class':'priceValue smallerPrice'})
    preco = tagPreco.find('span')
    time = str(datetime.now())
    
    url = "https://data.mongodb-api.com/app/data-pkmib/endpoint/data/beta/action/insertOne"
    payload = json.dumps({
        "collection": "testea",
        "database": "teste",
        "dataSource": "Cluster0",
        "document": {
            "preço": preco.text,
            "horario": time
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
    time.sleep(0)