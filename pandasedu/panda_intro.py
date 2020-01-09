
# Pandas is a module that is based on Series and Data Frames.

import numpy as np
import  pandas as pd

labels_list= ["Mustafa","Kemal","Murat","Kadir","Zeynep"]
data_list = [10,20,30,40,50]
print(pd.Series(data=data_list, index=labels_list)) #(data_list,label_lsit)
print(pd.Series(data_list))

npArray = np.array([10,20,30,40,50])
print(pd.Series(npArray,labels_list))

print(pd.Series(data= npArray,index=["A","B","C","D","E"]))

dataDict = {"Kadir":30,"Kemal":80,"Kamuran":60}
print(pd.Series(dataDict))

ser2017 = pd.Series([5,10,14,20]
                    ,["Bugday","Misir","Kiraz","Erik"])

print(ser2017)

ser2018 = pd.Series([2,12,12,6]
                    ,["Bugday","Misir","Cilek","Erik"])

print(ser2018)

print(ser2017 + ser2018)
total = ser2017 + ser2018
print(total["Erik"])