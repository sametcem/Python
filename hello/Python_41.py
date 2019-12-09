# Internetten bilgi cekmek
# Requests bir HTTP kütüphanesi,bilgileri çekmeye yarar
# BeautifulSoup ile de çektigimiz bilgileri işlemeyi yapacagız

"""
Microsoft Windows [Version 10.0.17134.590]
(c) 2018 Microsoft Corporation. Tüm hakları saklıdır.

C:\Users\CEM>python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> from bs4 import BeautifulSoup
>>> r = requests.get("https://yellowpages.com.tr/ara?q=cafe+Ankara") sayfa kaynagı istemi
>>> r.content içerigi görmemizi yarar
>>> soup = BeautifulSoup(r.content) Soup nesnesi ürettik,bunun içerisinde sayfa kaynağı var
>>> print(soup.prettify()) ->  güzelleştir:

    Bu sayfada biz linkleri çekmek istiyoruz
    Bir şeye basıyorsun başka bir sayfa acılıyor,bir şeye basıyorsun başka bir sayfa

    soup.find_all("a") -> bütün etiketleri çektik  (a href) kavramı
    Fakat bu linkleri tek tek nasıl çekeriz?

    linkler = soup.find_all("a")
    for link in linkler:
        print(link) 2 defa Enter!

    Kaç tane linkim var bu sayfada?
    for link in linkler:
        print(link.get("href")) -> Benim gerçek internet sayfalarım hangisi görmüs olacagım.

    Hangi tusa basıldıgında hangi linke gidiyor?
        for link in linkler:
            print(link.text) -> Hangi yazıya basınca hangi linke gittiğini görebiliyoruz.

        for link in linkler:
            print(link.text, link.get("href"))
                nereye basılcagını gösteren yer ve linki


    













"""