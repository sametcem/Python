sayi1=input("Please input a number")
sayi2=input("Please input another number")

try:
    sayi1=int(sayi1)
    sayi2=int(sayi2)
    print(sayi1/sayi2)

except ValueError:
    print("Uyusmayan deger hatası.")

except ZeroDivisionError:
    print("Bir sayi sıfıra bölunemez")

#except (ValueError,ZeroDivisionError):
    #print("Bir Hata olustu")

