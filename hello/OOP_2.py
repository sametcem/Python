# CONSTRUCTOR (__init__ self ) function
# Constructor içerisinde default value tanımlayabiliriz,Java'da olmayan bir ozellik

class Dusman:

    def __init__(self,isim ="Furkan",kalan_can=70,saldirigucu=300,mermi_sayisi=50):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldirigucu
        self.mermi_sayisi = mermi_sayisi
    def print(self):
        print("Basiliyor..........")
        print("İsim:",self.isim,"Kalan Can: ",self.kalan_can,"Saldiri gucu: ",self.saldiri_gucu,"Mermi sayisi: ",self.mermi_sayisi)

dusman1=Dusman("Ali",100,900,50)
dusman2=Dusman("Mustafa",80,600,30)
dusman3=Dusman()

print("Dusman1-------------------------- ")
dusman1.print()

print("Dusman2---------------------------")
dusman2.print()

print("Dusman3---------------------------")
dusman3.print()
