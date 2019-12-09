import requests
import operator
#Sembolleri çıkartalım
from bs4 import BeautifulSoup

def sozlukOlustur(tumkelimeler):
    kelimesayisi={}

    for kelime in tumkelimeler:
        if kelime in kelimesayisi:
            kelimesayisi[kelime] += 1 #Kelime append
        else:
            kelimesayisi[kelime] = 1 #Kelime ilk defa geliyorsa
    return kelimesayisi

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

kelimesayisi = sozlukOlustur(tumkelimeler)

for anahtar,deger in sorted(kelimesayisi.items(),key = operator.itemgetter(1)): #0 dersek kelimeye göre,1 dersek sayisina göre siralar.
    print(anahtar,deger)