y =  set() # Boş küme
type(y)

liste = [1,2,3,3,1,1,2,2,2]
x = set(liste)
print(x)

t = {"Python","Php","Python"}
print(t)

r = {"Python","Php","Java","C","Javascript"}
for i in r:
    print(i)

# Cannot access as x[0] or x["Python"]

g = {1,2,3}
g.add(4)
print(g)
g.add(4)
print(g)

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

print(küme1.difference(küme2))
print(küme2.difference(küme1))
print(küme1)


küme1.difference_update(küme2)
print(küme1)

küme1 = {1,2,3,4,5,6}
küme1.discard(2)
print(küme1)

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

print(küme1.intersection(küme2))


küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme1.intersection_update(küme2)
print(küme1)

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
küme3 = {30,40,50}

print(küme1.isdisjoint(küme2)) # eğer iki kümenin kesişim kümesi boş ise True, değilse False döner.
print(küme1.isdisjoint(küme3))

küme1 = {1,2,3}
küme2 = {1,2,3,4}
küme3 = {5,6,7}

print(küme1.issubset(küme2))
print(küme1.issubset(küme3))

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}
print(küme1.union(küme2))

# Update => Bu birinci kümeyle ikinci kümenin birleşim kümesini döner ve birinci kümeyi buna göre günceller.

küme1 = {1,2,3,10,34,100,-2}
küme2 = {1,2,23,34,-1}

küme1.update(küme2)
print(küme1)

