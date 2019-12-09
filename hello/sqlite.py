# SQLite
# Sunucusuz yani internetsiz çalışabilir.
# MySql sunuculu çalışıyormuş mesela.

import sqlite3

# Yoksa oluşturacak,varsa baglanacak.
connection = sqlite3.connect("Dersler.db")

# Cursor
cursor = connection.cursor()

#SQL SORGUSU ÇALIŞTIRIR. -> cursor.execute
def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenci(ad TEXT,soyad TEXT,numara INT,ogrnot INT)")
   # connection.close()
def degerEkle():
    cursor.execute("INSERT INTO ogrenci VALUES('Mark','Gibbons',1670,93)")
    connection.commit() # 1 kere commit yapsan yeterli olur.
    connection.close()

tabloOlustur()
degerEkle()




