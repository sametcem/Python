import  sqlite3
import time
import datetime
import random


con = sqlite3.connect("Dersler.db")
cursor = con.cursor()

def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Tablo1(zaman REAL,tarih TEXT,kelime TEXT,deger REAL)")

def queryShow():
    cursor.execute("SELECT * FROM Tablo1")
    data = cursor.fetchall()
    a=1
    for i in data:
        print(a,". satir ->",i)
        a+=1

def guncelle():
     cursor.execute("SELECT * FROM Tablo1")
     data = cursor.fetchall()
     a = 1
     print("İlk Degerler--------------------------------------")
     for i in data:
         print(a, ". satir ->", i)
         a += 1
     cursor.execute("UPDATE Tablo1 SET deger =99 WHERE deger=1")

     cursor.execute("SELECT * FROM Tablo1")
     data = cursor.fetchall()
     a = 1
     print("Güncelledikten sonra------------------------------")
     for i in data:
         print(a, ". satir ->", i)
         a += 1
     con.commit()

def sil():
    queryShow()
    cursor.execute("DELETE FROM Tablo1 WHERE deger=5")
    con.commit()
    print("\nSilindikten sonra")
    queryShow()

def updateParameter(kelime,deger):
    cursor.execute("UPDATE Tablo1 SET kelime=? where deger=?",(kelime, deger))
    con.commit()
    queryShow()

updateParameter('Samet',99)
con.close()
