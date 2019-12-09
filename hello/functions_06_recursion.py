# RECURSION

def topla(liste):
    toplam=0

    for i in liste:
        toplam += i

    return toplam

#print(topla([1,2,3,4]))

def toplarec(liste):
    if(len(liste) ==0):
        return 0
    else:
        return liste[0] + (topla(liste[1:]))

#1.return 1 + topla([2,3,4])
#2.return 2 + topla([3,4])  ...

#1 + (2 + (3 + (4 + 0)))

liste=[1,2,3,4,5,6]
print(toplarec(liste))