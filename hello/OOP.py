class Dusman:
    kalan_can =3
    def saldir(self): #self -> Kendi nesnemizi ifade ediyor
        print("Hücummmmmmmmmm!")
        self.kalan_can -= 1
    def hayattami(self):
        if(self.kalan_can <=0):
            print("Öldü")
        else:
            print(str(self.kalan_can) + " canı kaldi")

dusman1 = Dusman()
dusman2 = Dusman()

dusman1.saldir()
dusman1.saldir()
dusman1.hayattami()
print("????")
dusman2.saldir()
dusman2.saldir()
dusman2.saldir()
dusman2.hayattami()