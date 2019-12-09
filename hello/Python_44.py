import requests
#Sembolleri çıkartalım
from bs4 import BeautifulSoup

def sembolleritemizle(tumkelimeler):
    sembolsuzkelimeler = []
    semboller = "!@$#θ^*()'_\"?,./-<>[]=" + chr(775)

    for kelime in tumkelimeler:
        for sembol in semboller:
            if sembol in kelime:
                kelime =kelime.replace(sembol,"")

        if(len(kelime)>0):
            sembolsuzkelimeler.append(kelime)
    return sembolsuzkelimeler

url="https://www.ntv.com.tr/teknoloji/aziz-sancar-nobel-kimya-odulunu-aldi,F10C10YMBEaCIMqnra3I2w"

tumkelimeler = []

r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

for kelimegruplari in soup.find_all("p"):
    icerik = kelimegruplari.text
    kelimeler = icerik.lower().split()

    for kelime in kelimeler:
        tumkelimeler.append(kelime)


tumkelimeler = sembolleritemizle(tumkelimeler)

for kelime in tumkelimeler:
    print(kelime)