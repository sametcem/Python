def fonksiyon(name,*args):
    print("Name:",name)
    for i in args:
        print(i)

print(fonksiyon("Cem",1,2,3,4,5,6,7,8))

def fun2(**kwargs):
    print(kwargs)

print(fun2(isim = "Murat", soyisim = "Coşkun", numara = 12345))

def fun3(**kwargs):
    for i,j in kwargs.items():
        print("Argüman İsmi:",i,"Argüman Değeri:",j)

print(fun3(isim = "Cem", soyisim = "Habiboglu", numara = 12345))

def fun4(*args,**kwargs):
    for i in args:
        print("Argümanlar:",i)
    print("------------------------------")
    for i ,j in kwargs.items():
        print("Argüman İsmi:",i,"Argüman Değeri:",j)

print("////////////////")
print(fun4(1,2,3,4,5,6,7,isim = "Murat",soyisim = "Coşkun", numara = 12345))


# INNER FUNCTIONS

def sayHi(name):
    print("Hi",name)

sayHi("Samet")

hello = sayHi

hello("Maria")

del sayHi
#sayHi

hello("Kemal")

print("/////////////////////")
def fonksiyon():
    def fonksiyon2():
        print("Küçük fonksiyondan Merhaba")
    print("Büyük fonksiyondan Merhaba")
    fonksiyon2() # Tanımladığım fonksiyonu kullanabilirim.

fonksiyon()
#fonksiyon2()  # Lokal bir değişken olduğu için fonksiyon() çağrısından sonra yok oldu.

def suma(*args):  # args : (1,2,3,4,5,6)
    def topla(args):  # (1,2,3,4,5,6)
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    print(topla(args))

suma(12,13,14)


