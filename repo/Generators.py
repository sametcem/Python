
def getSquares():
    res = []
    for i in range(1,6):
        res.append(i**2)
    return res

print(getSquares())


def getMySquaresGenerator():
    for i in range(1,7):
        yield i ** 2

generator = getMySquaresGenerator()
print(generator)

iterator = iter(generator)
print(next(generator))
for i in iterator:
    print(i)

alist = [ i * 3 for i in range(5)]
print(alist)

gener2 =  ( i * 3 for i in range(5))
it = iter(gener2)
for i in it:
    print(i)

def carpimtablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)

for i in carpimtablosu():
    print(i)