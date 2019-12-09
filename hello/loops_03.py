factorial =1

while True:
    sayi = int(input("Lütfen Non-Negative bir sayı giriniz.."))

    if(sayi<= 0):
        print("Lütfen negative olmayan bir sayi giriniz")
    else:
        for i in range(1,sayi+1):
            factorial *=i

        print("Factorial",sayi,": ",factorial)
        break