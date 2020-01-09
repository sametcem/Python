try:
    a = int(input("Sayi1: "))
    b = int(input("Sayi2: "))
    print(a/b)

except ValueError: # (ValueError, ZeroDivisionError):
    print("Value error is occured")
except ZeroDivisionError:
    print("Zero Div Error is oocurred")
finally:
    print("Blocks finished")



# Verilen string'i ters çevirmek
def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen doğru bir input girin.")
    else:
        return s[::-1]


print(terscevir("Python"))







