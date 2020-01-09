
#Map function
def double(x):
    return x*2


a = map(double,[1,2,3,4,5,6])
lista = list(a)
print(lista)


#Lambda function
b = map(lambda x : x**2,[1,2,3,4,5,6,7,8,9,10])
listb = list(b)
print(listb)


listx = [1,2,3,4]
listy = [5,6,7,8]
listz= [8,9,10,11]

c = list(map(lambda x,y,z: x*y*z,listx,listy,listz))
print(c)



#Reduce function
from functools import reduce

def summ(x,y):
    return x+y

print(reduce(summ,[12,18,20,10]))
print(reduce(lambda x,y: x*y,[1,2,3,4,5,6]))


def getMax(x,y):
    if(x > y):
        return x
    else:
        return y


print(getMax(3,4))
print(reduce(getMax,[2,3,4,5]))

#Filter Function

a = filter(lambda x : x % 2 == 0,[1,2,3,4,5,6,7,8])
print(list(a))

def prime(x):
    i = 2
    if(x == 1):
        return False
    elif(x == 2):
        return True
    else:

        while(i<x):
            if(x%i == 0):
                return False
            i+=1
        return True

listA= filter(prime,range(1,100))
print(list(listA))


#Zip Function

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10,11]

y = 0
result = list()
while( y < len(l1) and y < len(l2)):
    result.append((l1[y],l2[y]))
    y += 1

print(result)
print("or")

z = list(zip(l1,l2))
print(z)


l3 = ["Python","PHP","Java","C#"]

zp = list(zip(l1,l2,l3))
print(zp)


for k,n in zip(l1,l3):
    print(k,n)

dict1 = {"Apple":1,"Watermelon":2,"Pineapple":3}
dict2 = {"Zero": 0 ,"One":1, "Two":2}

print(list(zip(dict1.values(),dict2.values())))


#Enumerate Function ( indexing )

listF= ["Apple","Banana","Cherry","Orange"]
t = 0
res = list()
while(t < len(listF)):
    res.append((t, listF[t]))
    t +=1

print(res)

a = enumerate(listF)
print(list(a))

for p,l in enumerate(listF):
    print(p,l)

listK = ["a","b","c","d","e","f","g"]
for m,b in enumerate(listK):
    if(m % 2 == 0):
        print(b)



# ALL and ANY

def allT(listeY):
    for i in listeY:
        if not i:
            return False
    return True

listeY = [True,False,True,False,True]
print(allT(listeY))

listC = [1,2,3,4,5]
print(allT(listC))


def fun(list):
    for i in list:
        if i:
            return True
    return False

print(fun([0,0,0,0,0]))



print(all(listeY))
print(all([True,True]))

print(any(listeY))
print(any([0,0,0,0]))