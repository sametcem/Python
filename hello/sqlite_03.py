import  sqlite3
import time
import datetime
import random

con =sqlite3.connect("Dersler.db")
cursor = con.cursor()

def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1(zaman REAL,tarih TEXT,kelime TEXT,deger REAL)")

def rastgeledegerekle():
    zaman = time.time()
    tarih = str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    kelime="Python Sqlite3"
    deger=random.randrange(0,10)
    cursor.execute("INSERT INTO Tablo1(zaman,tarih,kelime,deger) VALUES (?,?,?,?)",(zaman,tarih,kelime,deger))
    con.commit()

def queryShow():
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    a=1
    for i in data:
        print(a,". satir ->",i)
        a+=1

def queryZamanTarih():
    cursor.execute("SELECT zaman,tarih FROM Tablo1")
    data = cursor.fetchall()
    a=1
    for i in data:
        print(a,". satir ->",i)
        a+=1

def queryWhere():
    cursor.execute("SELECT * FROM Tablo1 WHERE deger =5.0 or deger=1.0")
    data = cursor.fetchall()
    a=1
    for i in data:
        print(a,". satir ->",i)
        a+=1

#queryShow()
#queryZamanTarih()
queryWhere()