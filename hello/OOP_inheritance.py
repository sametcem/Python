class Calisan(): # İci bos parantez kalitimda kullanilmali(Normal zamanda da kullanabilirsin)

    def __init__(self,isim,maas,departman):
        print("Calisan sınıfının Constructor'i islem görüyor")
        self.isim = isim
        self.maas = maas
        self.departman =departman

    def showInfo(self):
        print("Calisan sınıfının bilgileri gösteriliyor")
        print("İsim:", self.isim, "Maaş:", self.maas, "Calıstıgı Departman:", self.departman)

    def maasazamyap(self,zammiktari):
        print(self.isim + " in maasina zam yapıldı")
        self.maas += zammiktari

    def changeDept(self,yeni_department):
        print(self.isim + " in departmani degistiriliyor")
        self.departman = yeni_department
#Overriding
class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,supervise):
        print("Yonetici sınıfının Constructor'i islem görüyor")
        super().__init__(isim,maas,departman)
        self.supervise = supervise


    def showInfo(self):
        print("Yonetici sınıfının bilgileri gösteriliyor")
        print("İsim:", self.isim, "Maaş:", self.maas, "Calıstıgı Departman:", self.departman,"Supervise:",self.supervise)

    def addEmployee(self,arttir):
        print("Kisi sayisi arttırılıyor")
        self.supervise += arttir


yonetici = Yonetici("Yamac BEYAZ",12000,"HR",5)
yonetici.showInfo()
yonetici.addEmployee(10)
yonetici.showInfo()


