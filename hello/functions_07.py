# LOCAL AND GLOBAL VARIABLES

a=10

def fonksiyon():
    global a
    a=2

    print(a)

fonksiyon()
print(a)