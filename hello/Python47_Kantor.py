# JSON datası veri alışverişinde en çok kullanılan datalardan biri.

import requests
import json

access_key="88341d426273f8ebd9fe6dd93a9ffdad"

url = "http://data.fixer.io/api/latest"


birinci = input("Birinci Doviz: ")
ikinci = input("Input Doviz: ")

miktar = float(input("Miktar: "))

response = requests.get(url + birinci,access_key)

print(response)

json_verisi = response.json()

print(json_verisi)

#Daha sonra!...