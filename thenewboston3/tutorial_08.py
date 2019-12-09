# Downloading Files from the WEB CSV file indiriyoruz.
# CSV (Virgülle Ayrılan Değerler) dosyası, Excel'de oluşturabileceğiniz veya düzenleyebileceğiniz özel bir dosya türüdür.
#Different way of importing
from urllib import request

csv_url ="https://people.sc.fsu.edu/~jburkardt/data/csv/ford_escort.csv"
csv_hurricanes = "https://people.sc.fsu.edu/~jburkardt/data/csv/hurricanes.csv"
csv_oscar ="https://people.sc.fsu.edu/~jburkardt/data/csv/oscar_age_female.csv"

def download_csv_stock_data(csv_url):
    response = request.urlopen(csv_url) # Connection to web page parameter should be URL
    csv = response.read()
    csv_str = str(csv) # to guarantee put it in a string
    #Buraya kadar komple bir string halinde data.
    lines = csv_str.split("\\n") # Simdi parcalıyoruz
    dest_url=r'ornek.csv' #File path kullanırken r kullanırsan daha iyi.bilgisayarda dosya olustur ve icine yaz islemi olacak
    fx = open(dest_url,"w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_csv_stock_data(csv_hurricanes)

