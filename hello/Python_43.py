import requests

from bs4 import BeautifulSoup

url="https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"

tumkelimeler = []

r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

for kelimegruplari in soup.find_all("p"):
   # print(kelimegruplari) #butun <p> etiketli olan herseyi bastırır.
    icerik = kelimegruplari.text #sadece text kısımlarını alıyoruz
    kelimeler = icerik.lower().split()

    for kelime in kelimeler:
        tumkelimeler.append(kelime)
        print(kelime)

