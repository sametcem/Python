import numpy as np
import pandas as pd

from numpy.random import randn

outerIndex = ["Group1","Group1","Group1","Group2","Group2","Group2","Group3","Group3","Group3"]
innderIndex = ["Index1","Index2","Index3","Index1","Index2","Index3","Index1","Index2","Index3"]

hierarchy = list(zip(outerIndex,innderIndex))
hierarchy = pd.MultiIndex.from_tuples(hierarchy)
print(hierarchy)

df = pd.DataFrame(randn(9,3),hierarchy,columns = ["Column1","Column2","Column3"])
print(df)
print("*")
print(df["Column1"])
print("*")
print(df.loc["Group1"])
print("*")
print(df.loc[["Group1","Group2"]])
print("*")
print(df.loc["Group1"].loc["Index1"]["Column1"])
print("*")

df.index.names =["Groups","Indexes"]
print(df)
print("*")
print(df.xs("Group1").xs("Index1").xs("Column1"))
print("*")

print(df.xs("Index1", level="Indexes"))