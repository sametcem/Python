import os
from datetime import datetime
#print(dir(os))
print(os.getcwd()) #pwd
#change dir
#os.chdir("path C:/Uers/Desktop")

print(os.listdir("C:/Users/CEM/Desktop"))
print(os.getcwd())

#os.mkdir("Deneme1")
#os.makedirs("Deneme2/Deneme3")

#os.rmdir("Deneme1")
#os.rmdir("Deneme2/Deneme3")

#os.mkdir("Deneme2/Deneme3")
#os.removedirs("Deneme2/Deneme3")

#os.rename("text.txt","test2.txt")

print(os.stat("test2.txt"))
# last changed time st_mtime=1576521248

print(os.stat("test2.txt").st_mtime)
print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime))


print("#")
print(os.walk("C:/Users/CEM/Desktop"))

iterator = iter(os.walk("D:\Cem-PJAIT\LECTURES\Source\Python\(42 Saat) Python  Sıfırdan İleri Seviye Programlama (2019)"))
for dir_path,dir_name,file_name in iterator:
    print("Directory Path",dir_path)
    print("Directory Name",dir_name)
    print("File Name",file_name)
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-")

for dir_path,dir_name,file_name in os.walk("C:/Users/CEM/Desktop"):
    for i in file_name:
        if(i.endswith(".txt")):
            print(i)