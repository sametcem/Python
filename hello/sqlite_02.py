import  sqlite3
import random
import time
import datetime

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


tabloOlustur()

i=0
while(i<10):
    rastgeledegerekle()
    time.sleep(1)
    i +=1

con.close()
