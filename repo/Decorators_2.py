import time

def getTime(func):
    def wrapper(numbers):
        start = time.time()
        res = func(numbers)
        end = time.time()
        print(func.__name__  + " " + str(end-start) + " sn")
        return res
    return wrapper

@getTime
def getSquare(numbers):
    res = list()
    for i in numbers:
        res.append(i**2)
    return res

@getTime
def getCube(numbers):
    res = list()

    for i in numbers:
        res.append(i ** 3)

    return res


getSquare(range(100000))
getCube(range(100000))



