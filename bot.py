#---------------------------------------------------------------------------------------------------
#                                 Importando as bibliotecas utilizadas no codigo 
#---------------------------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
import schedule
from datetime import time, date, datetime
import json

#---------------------------------------------------------------------------------------------------

def googleFinance():
    #-----------------------------------------------------------------------------------------------
    #                                   Extraindo o preço do site
    #-----------------------------------------------------------------------------------------------
    url = requests.get('https://www.google.com/finance/quote/BTC-BRL?hl=pt')
    html = url.content
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', attrs={'class':'YMlKec fxKbKc'})
    price = div.text
    #-----------------------------------------------------------------------------------------------
    #                      Removendo caracteres de variavel a e salvando o preço
    #-----------------------------------------------------------------------------------------------
    a = "."
    price = ''.join(x for x in price if x not in a)
    price = price.replace(',','.')
    #-----------------------------------------------------------------------------------------------
    #                                   Salvando o preço no MongoDB
    #-----------------------------------------------------------------------------------------------
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
    responsePreco = requests.request("POST", url, headers=headers, data=payload)
    print()
    print(price, responsePreco)
    #-----------------------------------------------------------------------------------------------
    #                             Salvando o horario que o preço foi pego
    #-----------------------------------------------------------------------------------------------
    a = (datetime.now())
    hora = a.strftime('%H/%M/%S')
    url = "https://data.mongodb-api.com/app/data-pkmib/endpoint/data/beta/action/insertOne"
    payload = json.dumps({
        "collection": "tempo",
        "database": "teste",
        "dataSource": "Cluster0",
        "document": {
            "horario": hora,
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'bWdELScAUp4oSoDmVLyoOPIKosx0VqCpJpQdlgzuWq9HW2R8MqRXNDcyxLtpB59A'
    }
    responseHora = requests.request("POST", url, headers=headers, data=payload)
    print(hora, responseHora)

#---------------------------------------------------------------------------------------------------

def coinMarketcap():
    #-----------------------------------------------------------------------------------------------
    #                                     Extraindo o preço do site
    #-----------------------------------------------------------------------------------------------
    url = requests.get('https://coinmarketcap.com/pt-br/currencies/bitcoin/')
    html = url.content
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', attrs={'class':'priceValue smallerPrice'})
    tag = div.find('span')
    price = (tag.text)
    #-----------------------------------------------------------------------------------------------
    #                      Removendo caracteres de variavel a e salvando o preço
    #-----------------------------------------------------------------------------------------------
    a = "R$ ,"
    price = ''.join(x for x in price if x not in a)
    #-----------------------------------------------------------------------------------------------
    #                                  Salvando o preço no MongoDB
    #-----------------------------------------------------------------------------------------------
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
    responsePreco = requests.request("POST", url, headers=headers, data=payload)
    print('')
    print(price, responsePreco)
    #-----------------------------------------------------------------------------------------------
    #                             Salvando o horario que o preço foi pego
    #-----------------------------------------------------------------------------------------------
    a = (datetime.now())
    hora = a.strftime('%H/%M/%S')
    url = "https://data.mongodb-api.com/app/data-pkmib/endpoint/data/beta/action/insertOne"
    payload = json.dumps({
        "collection": "tempo",
        "database": "teste",
        "dataSource": "Cluster0",
        "document": {
            "horario": hora,
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'bWdELScAUp4oSoDmVLyoOPIKosx0VqCpJpQdlgzuWq9HW2R8MqRXNDcyxLtpB59A'
    }
    responseHora = requests.request("POST", url, headers=headers, data=payload)
    print(hora, responseHora)

#---------------------------------------------------------------------------------------------------

def data():
    a = (datetime.now())
    data = a.strftime('%m/%d/%Y')
    #-----------------------------------------------------------------------------------------------
    #                                Salvando a data no MongoDB
    #-----------------------------------------------------------------------------------------------
    url = "https://data.mongodb-api.com/app/data-pkmib/endpoint/data/beta/action/insertOne"
    payload = json.dumps({
        "collection": "data",
        "database": "teste",
        "dataSource": "Cluster0",
        "document": {
            "horario": data,
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': 'bWdELScAUp4oSoDmVLyoOPIKosx0VqCpJpQdlgzuWq9HW2R8MqRXNDcyxLtpB59A'
    }
    responseData = requests.request("POST", url, headers=headers, data=payload)
    print()
    print(data, responseData)

#---------------------------------------------------------------------------------------------------

schedule.every(1).minutes.do(googleFinance)
schedule.every(2).minutes.do(coinMarketcap)
schedule.every().day.at("00:00").do(data)

#---------------------------------------------------------------------------------------------------

while True:
    schedule.run_pending()
    #time.sleep(1)