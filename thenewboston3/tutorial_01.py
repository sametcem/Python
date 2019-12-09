for i in range(0,50,5):
    if i is 0:
        continue
    print(i)

myname ="Habiboglu"

if (myname=="Cem"):
    print("Merhaba Cem")
elif(myname=="Habiboglu"):
    print("Merhaba Habiboglu")
else:
    print("Merhaba Samet")

i=0
while i<9:
    print(i)
    i+=1

liste = ["Ali","Veli","Ayse","Fatma","Kadir","Adali"]

for i in liste:
    print(i)
    if i is "Kadir":
        break


print(liste + [1,2,3])