
open("info.txt","w")

"""
file = open("info.txt","w")
file.close()

file2 = open("C:/Users/CEM/Desktop/info2.txt","w",encoding="utf-8") # WRITE
file2.write("Samet Cem Habiboglu")
file2.close()


file2 = open("C:/Users/CEM/Desktop/info2.txt","a",encoding="utf-8") # APPEND
file2.write("\nCem 26")
file.close()
"""

try:
    file3 = open("C:/Users/CEM/Desktop/info2.txt", "r", encoding="utf-8")  # READ
    for i in file3:
        print(i,end="")
    file3.close()
except FileNotFoundError:
    print("No File")


file4 = open("C:/Users/CEM/Desktop/info2.txt", "r", encoding="utf-8")
content = file4.read()
print("\nContent ->")
print(content)

print("from readLine ->")
file5 = open("C:/Users/CEM/Desktop/info2.txt", "r", encoding="utf-8")
print(file5.readline(),end="")
print(file5.readline())
print(file5.readline())
print(file5.readline())
file5.close()

print("from List")
file6 = open("C:/Users/CEM/Desktop/info2.txt", "r", encoding="utf-8")
list = file6.readlines()
print(list)
file6.close()



