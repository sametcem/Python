class Ogrenci():
    def derscalis(self):
        print("Ogrenci su an ders calisiyor")


class Calisan():
    def calis(self):
        print("Personal su anda calisiyor")


class Yazilimci(Ogrenci,Calisan):
    def derscalis(self): # @Override
        print("Yazilimci su an ders calisiyor")


yazilimci = Yazilimci()
yazilimci.derscalis()
yazilimci.calis()