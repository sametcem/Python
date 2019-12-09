# IMDB ÇEK.

import requests

from bs4 import BeautifulSoup

imdburl = "https://www.imdb.com/chart/top"

r = requests.get(imdburl) # Sayfanın bütün kaynagı bu r'nin icerisinde su an.

soup = BeautifulSoup(r.content,"html.parser")

gelen_veri = soup.find_all("table", {"class":"chart full-width"})

#print(gelen_veri[0].contents)
#print(len(gelen_veri[0].contents))

# 0 \n 1 colgroup vs thead oldugu icin 7 çıktı.
#Contents listesini içerisindeki tbodyi alacağız.
#en alt satır bak tbody (5)ve \n(6) yazıyor demek ki tbody 5te yani len -2

#(gelen_veri[0].contents) table in 3 contentini verecej bu.
filmtablosu = (gelen_veri[0].contents)[len(gelen_veri[0].contents)-2]
#print(filmtablosu)
#tbocy içerisindeki trler her bir filmi temsil ediyor

filmtablosu = filmtablosu.find_all(["tr"])

#Her bir filmin baslıgı icin titleColumn'u alacagız
for film in filmtablosu:
    filmbasliklari = film.find_all("td", {"class":"titleColumn"})
    filmismi = filmbasliklari[0].text
    filmismi = filmismi.replace("\n","")

    print(filmismi)
    print("************************")







