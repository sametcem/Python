def fun(oper):
    def suma(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def multi(*args):
        çarpım = 1
        for i in args:
            çarpım *= i
        return çarpım

    if oper == "suma":
        return suma
    else:
        return multi

a = fun("suma")
print(a)
print(a(1,2,3,4,5))
b = fun("ole")
print(b(1,2,3,4))


def toplama(a,b):
    return a + b
def çıkarma(a,b):
    return a-b
def çarpma(a,b):
    return a * b
def bölme(a,b):
    return a / b

def anafonksiyon(func1,func2,func3,func4,işlem_adı): # Tanımladığımız 4 fonksiyonu da argüman olarak göndereceğiz.
    if (işlem_adı == "toplama"):
        print(func1(3,4))
    elif (işlem_adı == "çıkarma"):
        print(func2(10,3))
    elif (işlem_adı == "çarpma"):
        print(func3(10,3))
    elif (işlem_adı == "bölme"):
        print(func4(10,4))
    else:
        print("Geçersiz işlem adı...")

print(anafonksiyon(toplama,çıkarma,çarpma,bölme,"toplama"))
print(anafonksiyon(toplama,çıkarma,çarpma,bölme,"bölme"))