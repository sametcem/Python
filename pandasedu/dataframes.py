#columns and indexes like database

import numpy as np
import pandas as pd

from numpy.random import randn
randn(3,3)

df = pd.DataFrame(data= randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])
print(df)
print("**")

print(df["Column1"])
print("**")
print(df["Column2"])
print("**")
print(df.loc["A"])
print("**")

df_ver2 = df [["Column1","Column3"]]
print(df_ver2)

df["Column4"] = pd.Series(randn(3),["A","B","C"])
print("*")
print(df)
print("*")

df["Column5"] = df["Column1"] + df["Column2"] + df["Column3"]
print(df)
print("*")
df.drop("Column5",axis=1,inplace=True) # updating df with inflace
print(df)


print("*")
print(df.iloc[0])
print("*")
print(df.loc["A","Column1"])
print(df.loc["B","Column2"])
print(df.loc[["A","B"],["Column1","Column2"]])