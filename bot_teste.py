import requests
from bs4 import BeautifulSoup
import schedule
from datetime import time, date, datetime
import json

def googleFinance():
    url = requests.get('https://www.google.com/finance/quote/BTC-BRL?hl=pt')
    html = url.content
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', attrs={'class':'YMlKec fxKbKc'})
    price = div.text
    print(price)

    url = "https://data.mongodb-api.com/app/data-pkmib/endpoint/data/beta/action/insertOne"
    payload = json.dumps({
        "collection": "preco",
        "database": "teste",
        "dataSource": "Cluster0",
        "document": {
            "preço": price,
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'bWdELScAUp4oSoDmVLyoOPIKosx0VqCpJpQdlgzuWq9HW2R8MqRXNDcyxLtpB59A'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

def coinMarketcap():
    url = requests.get('https://coinmarketcap.com/pt-br/currencies/bitcoin/')
    html = url.content
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', attrs={'class':'priceValue smallerPrice'})
    tag = div.find('span')
    a = (tag.text)
    
    #Removendo caracteres de variavel a e salvando o preço
    b = "R$ ,"
    a = ''.join(x for x in a if x not in b)
    price = float(a)
    print(price)
    #print(type(price))

    #Salvando o preço no MongoDB
    url = "https://data.mongodb-api.com/app/data-pkmib/endpoint/data/beta/action/insertOne"
    payload = json.dumps({
        "collection": "preco",
        "database": "teste",
        "dataSource": "Cluster0",
        "document": {
            "preço": price,
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'bWdELScAUp4oSoDmVLyoOPIKosx0VqCpJpQdlgzuWq9HW2R8MqRXNDcyxLtpB59A'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

def tempo():
    a = (datetime.now())
    time = a.strftime('%m:%d:%Y %H:%M:%S')
    print(time)

    #Salvando o horario no MongoDB
    url = "https://data.mongodb-api.com/app/data-pkmib/endpoint/data/beta/action/insertOne"
    payload = json.dumps({
        "collection": "tempo",
        "database": "teste",
        "dataSource": "Cluster0",
        "document": {
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


schedule.every(25).seconds.do(googleFinance)
schedule.every(25).seconds.do(coinMarketcap)
schedule.every(25).seconds.do(tempo)

while True:
    schedule.run_pending()
    #time.sleep(0)