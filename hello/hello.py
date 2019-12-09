print("Oyuncu Kaydetme Programi")

ad=input("Oyuncunun ismini giriniz")
soyad=input("Oyuncunun soyismini giriniz")
takim=input("Oyuncunun takimini giriniz")

bilgiler =[ad,soyad,takim]

print("Database'e kaydediliyor.....")

print("Oyuncunun adi:",ad,
      "Oyuncunun soyadi",soyad,
      "Oynadıgı takimi",takim)

print("Kaydedildi......")

#print(bilgiler[0],bilgiler[1],bilgiler[2])

print("Oyuncunun adi:{} \nOyuncunun Soyadi:{} \nOyuncunun oynadıgı takim: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))
