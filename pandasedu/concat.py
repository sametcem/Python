import numpy as np
import pandas as pd

dataset1 = {
    "A": ["A1","A2","A3","A4"],
    "B": ["B1","B2","B3","B4"],
    "C": ["C1","C2","C3","C4"],
}

dataset2 = {
    "A": ["A5","A6","A7","A8"],
    "B": ["B5","B6","B7","B8"],
    "C": ["C5","C6","C7","C8"],
}

df1 = pd.DataFrame(dataset1,index = [1,2,3,4])
df2 = pd.DataFrame(dataset2,index = [5,6,7,8])

print(df1)
print("*")
print(df2)
print("*")

print(pd.concat([df1,df2]))
print("*")
print(pd.concat([df1,df2],axis=1))
print("*")

