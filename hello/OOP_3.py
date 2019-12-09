import random

class Dusman:

    def __init__(self,isim ="Furkan",kalan_can=70,saldirigucu=300,mermi_sayisi=50):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldirigucu
        self.mermi_sayisi = mermi_sayisi

    def saldir(self):
        print(self.isim + " Saldiriyor!")
        harcananmermi = random.randrange(0,10)
        print(str(harcananmermi) + " kadar mermi harcandi...")
        self.mermi_sayisi -= harcananmermi

        return (harcananmermi,self.saldiri_gucu)

    def saldiriyaugra(self,harcanan_mermi,saldiri_gucu):
        print(self.isim + " saldiriya ugradi")
        self.kalan_can -= (harcanan_mermi* saldiri_gucu)

    def mermi_bitti(self):
        if(self.mermi_sayisi <= 0):
            print(self.isim + " 'in mermisi bitti..")
            return True
        return False

    def hayatta_mi(self):
        if(self.kalan_can <= 0):
            print("Ölüyorum laaaaaan!")

    def print(self):
        print("Basiliyor..........")
        print("İsim:",self.isim,"Kalan Can: ",self.kalan_can,"Saldiri gucu: ",self.saldiri_gucu,"Mermi sayisi: ",self.mermi_sayisi)

dusmanlar= []
i=0

while(i<10):
    randomcan = random.randrange(100,200)
    randomsaldiriguc= random.randrange(10,20)
    randommermi = random.randrange(20,30)
    yeniDusman =Dusman("Dusman" + str(i+1),randomcan,randomsaldiriguc,randommermi)
    dusmanlar.append(yeniDusman)

    i+=1

#for dusman in dusmanlar:
 #   dusman.print()

j=0
while (j<3):
    randomdusman1=random.randrange(0,10)
    randomdusman2 = random.randrange(0,10)

    donendeger = dusmanlar[randomdusman1].saldir() #(15,5) Bir tuple döndürecek

    dusmanlar[randomdusman2].saldiriyaugra(donendeger[0],donendeger[1])

    print("Round Bitti....")

    j+=1