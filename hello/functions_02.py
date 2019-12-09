def factorial(numara):
    factorial =1
    for i in range(1,numara+1):
        factorial *= i

    #print("Factorail:",numara," :",factorial)
    return factorial


sayi = int(input("Please input a number"))
a=factorial(sayi)

print(a)