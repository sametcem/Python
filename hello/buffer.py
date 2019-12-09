# w write modu dosya yoksa yaratır ve içine yazmamızı saglar.
# eger var ise eskisini siler yenisini oluşturur 0'dan yazarız.
## read modu, olan bir dosyayı açıp okumamazı saglar
## a modu (append) olan bir dosyanın icindeki bilgileri degistirir.
## a modu da dosya yoksa olusturacaktır.
#dosya = open("C:/Users/CEM/Desktop/yazilim.txt","w") -> Masaustu

dosya = open("yazilim.txt","a")

dosya.write("Hello")
