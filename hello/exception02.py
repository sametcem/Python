# try - except - finally // finally blogu kesin çalışır.

try:
    dosya = open("yazilimbilimi.txt")
except IOError:
    print("Invalid file.")
finally:
    dosya.close()

#dosya kapandıgında bufferda gereksiz yer
#kaplamez ve güvenli olur.