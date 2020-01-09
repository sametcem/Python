import numpy as np

data_list = [1,2,3]

arr = np.array(data_list)
print(arr)

data_list2 = [[10,20,30],[40,50,60],[70,80,90]]
arr2 = np.array(data_list2)
print(arr2)

arr3 = np.array([1,2,3,4,5])
print(arr3)

print(arr3[0])
print(arr3[4])

print(arr2[2][2])
print(np.arange(10,20))
print(np.arange(0,100,3))
print(np.zeros(10))
print(np.ones(10))
print(np.zeros((3,4)))

print(np.linspace(0,100,5))
print(np.eye(6)) # birim matrix

print(np.random.randint(0,10,5))
print(np.random.randn(5)) # Gaussian Distribution

arr4 = np.arange(25)
print(arr4)

arr4.reshape(5,5)
print(arr4)

newArray = np.random.randint(1,100,10)
print(newArray)
print(newArray.max())
print(newArray.min())
print(newArray.sum())
print(newArray.mean())
print(newArray.argmax()) #Max number index / argmin()

detArr = np.random.randint(1,100,25)
print(detArr)

detArr = detArr.reshape(5,5)
print(detArr)

print(np.linalg.det(detArr))


detArr2 = np.array([[1,2],[3,4]])
print(detArr2)

print(round(np.linalg.det(detArr2)))


#####################################



ar = np.arange(1,10)
print(ar)
print(ar[1:5])
print(ar[:4])
print(ar[::2])

ar[:3] = 25
print(ar)
# arr2 = arr.copy()


# MULTI DIMENSIONAL

nArr = np.arange(1,21)
print(nArr)

nArr = nArr.reshape(5,4)
print(nArr)

print(nArr[:,:2])
print(nArr[:3,:3])
print(nArr[:2,:])
print(nArr[:2])

print(nArr > 3)
#booleanArray = arr > 3
#arr[booleanArray]  -> only True values
# arr[arr > 5]

###########################
arrt = np.array([10,20,30,40,50,60])
arrt2 = np.array([2,3,4,5,6,7])

newr = arrt + arrt2 # *
print(newr)
print(arrt + 10)
print(arrt2 - 2)
print(arrt / 3)
print(arrt)

aro = np.sqrt(arrt)
print(aro)

# Numpy Documentation...