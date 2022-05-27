import requests
import json
url = "https://data.mongodb-api.com/app/data-pkmib/endpoint/data/beta/action/insertOne"
payload = json.dumps({
    "collection": "testea",
    "database": "teste",
    "dataSource": "Cluster0",
    "document": {
        "nome":"luis",
        "idade":"17"
    }
})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'bWdELScAUp4oSoDmVLyoOPIKosx0VqCpJpQdlgzuWq9HW2R8MqRXNDcyxLtpB59A'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)