import numpy as np
import pandas as pd

dataset1 = {
    "A": ["A1","A2","A3"],
    "B": ["B1","B2","B3"],
    "anahtar": ["K1","K2","K3"],
}

dataset2 = {
    "X": ["X1","X2","X3","X4"],
    "Y": ["Y1","Y2","Y3","Y4"],
    "anahtar": ["K1","K2","K5","K4"],
}

df1 = pd.DataFrame(dataset1,index = [1,2,3])
df2 = pd.DataFrame(dataset2,index = [1,2,3,4])
print(df1)
print("*")
print(df2)
print("*") #MERGE INNER JOIIN COMMON VALUES
print(pd.merge(df1,df2, on="anahtar"))