sozluk = {"Python":"Guzel bir dil","Php":"Script Dili","Java":"Compile edilen dil"}

print(type (sozluk))
print(sozluk["Python"])

for i in sozluk.items():
    print(i)
#Hepsi tuple şeklinde alt alta dizildi

for i in sozluk.items():
    print(i[0] + " -> " + i[1])

# MAPS - KEY and VALUE

for i,j in sozluk.items():
    print(i + " /*/ " + j)