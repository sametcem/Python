dersler={"Ahmet":["Veritabanı","Isletim Sistemleri"],
         "Oguz":["Script Dersi","OOP Programming"],
         "Mehmet" :["Linear Algebra"]}

isim =input("Isim giriniz...")

print("{}'in aldıgı dersler: ".format(isim))

for i in (dersler[isim]):
    print(i)