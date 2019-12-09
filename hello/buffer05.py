
liste = [1,2,3,4,5]

liste.insert(1,15)
print(liste)

with open("languages.txt","r+") as dosya:
    data = dosya.readlines()
    data.insert(1,"Eklenecek 1. sentence\n")
    dosya.seek(0)
    dosya.writelines(data)