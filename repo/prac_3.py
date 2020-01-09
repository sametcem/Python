# LIST

liste = [1,2,3,4,5,6,7]
liste.append(34)
print(liste)

liste.append("Python")
print(liste)

liste.extend([10,11,12])
print(liste)

liste.insert(2,"PythonXXX")
print(liste)

liste.pop()
print(liste)
liste.pop(2) # 2.indeksteki eleman siliniyor.
print(liste)

liste = ["Python","Php","Java","C"]
liste.remove("Python") # Python'ı siliyoruz.
print(liste)

liste = [1,2,3,4,3,3,5,6,7,8,9]
print(liste.index(3))
print(liste.index(3,3))

liste = [1,2,3,4,5,6,1,1,1,1,1,1,1,1,8]
print(liste.count(1))

liste = [12,-2,3,1,34,100]
liste.sort()
print(liste)

liste2 = ["Python","Php","C","Java"]
liste2.sort()
print(liste2)

liste = [12,-2,3,1,34,100]
liste.sort(reverse = True)

print(liste)

liste2 = ["Python","Php","C","Java"]
liste2.sort(reverse = True)
print(liste2)