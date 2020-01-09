#Auto-Closing File
with open("C:/Users/CEM/Desktop/info2.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i,end="")

print("\n###")
with open("C:/Users/CEM/Desktop/info2.txt","r",encoding="utf-8") as file:
    file.seek(5) # Skip 5 bytes
    content = file.read(11)
    print(content)
    print(file.tell())

print("# R+ both read and write")
with open("C:/Users/CEM/Desktop/info3.txt","r+",encoding="utf-8") as file:
    file.seek(10)
    file.write("Hello")


print("# R+ both read and write")
with open("C:/Users/CEM/Desktop/info3.txt","r+",encoding="utf-8") as file:
    print(file.read())

#append will add last

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Mehmet Keper\n")
    file.seek(0)
    for satır in liste:
        file.write(satır)

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    print(icerik)


with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Ahmet Baltacı\n")
    file.seek(0)
    file.writelines(liste)

with open("bilgiler.txt","r+",encoding = "utf-8") as file:
    icerik = file.read()
    print(icerik)
