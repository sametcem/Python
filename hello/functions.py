def merhaba():
    print("Hello World")

#merhaba()

def factorial(numara):
    factorial =1
    for i in range(1,numara+1):
        factorial *= i

    print("Factorail:",numara," :",factorial)


sayi = int(input("Lütfen sayıyı giriniz"))

factorial(sayi)