#read() -> Hepsini alır
#readline() -> İlk Satır
#readlines() -> bütün satırlar liste seklinde
try:
    dosya = open("languages.txt", "r")
    #print(dosya.read())

    #print(dosya.readline())
    #print(dosya.readline())
    #print(dosya.readline())

    liste = dosya.readlines()
    print(liste[1])


except FileNotFoundError:
    print("Invalid File")

finally:
    dosya.close()

# PYTHON kendisi de dosyayı kapatıyor sonradan.