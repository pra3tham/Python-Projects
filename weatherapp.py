import requests
import json
import os

city= input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=e456016eb42347da90e190109243101&q={city}"

r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])

#os.system("")