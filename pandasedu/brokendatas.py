import numpy as np
import pandas as pd

arr = np.array([[10,20,np.nan],[5,np.nan,np.nan],[21,np.nan,10]])
#print(arr)

df = pd.DataFrame(arr,index=["Index1","Index2","Index3"], columns= ["Column1","Column2","Column3"])
#df.dropna(axis=1,inplace=True)
#df.dropna(thresh=2, inplace=True) # min 2 NaN
#print(df)

#df.fillna(value=1,inplace=True) # fill na with value
print(df)
print("*")

def calculateMean(df):
    totalSum = df.sum().sum()
    totalNum = df.size - df.isnull().sum().sum()
    return totalSum / totalNum

mean = df.fillna(value=calculateMean(df))
print(mean)