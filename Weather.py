import requests

api_address='https://api.weatherapi.com/v1/current.json?key=feba87d6ed9c418691b191839242701&q=ghaziabad&aqi=yes'
json_data=requests.get(api_address).json()

def temp():
    temperature=round(json_data["current"]["temp_c"]-273,1)
    return temperature

def des():
    description=json_data["current"]["condition"]["text"]
    return description

