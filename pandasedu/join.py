import numpy as np
import pandas as pd

dataset1 = {
    "A": ["A1","A2","A3","A4"],
    "B": ["B1","B2","B3","B4"],
}

dataset2 = {
    "X": ["X1","X2","X3"],
    "Y": ["Y1","Y2","Y3"],
}

df1 = pd.DataFrame(dataset1,index = [1,2,3,4])
df2 = pd.DataFrame(dataset2,index = [1,2,3])

print(df1)
print("*")
print(df2)
print("*")
print(df1.join(df2)) #left join
print("*")
print(df2.join(df1)) #right join