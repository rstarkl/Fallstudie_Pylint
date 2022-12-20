# Die Teilnehmer sollten Pylint auf den folgenden Code anwenden und alle Probleme beheben, die gefunden werden. Sie sollten auch Regeln erstellen, um bestimmte Arten von Problemen zu ignorieren oder zu melden.

import requests

def fetchDataFromAPI(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("API request failed")

def processData(data):
    processed_data = []
    for item in data:
        processed_item = {}
        processed_item['name'] = item['name']
        processed_item['age'] = item['age']
        processed_data.append(processed_item)
    return processed_data

def writeDataToFile(data, filename):
    with open(filename, 'w') as f:
        for item in data:
            f.write(f"{item['name']},{item['age']}\n")

api_data = fetchDataFromAPI("https://example.com/api/v1/people")
processed_data = processData(api_data)
writeDataToFile(processed_data, "people.csv")
