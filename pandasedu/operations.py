import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Column1": [1,2,3,4,5,6],
    "Column2": [100,100,200,300,300,100],
    "Column3": ["Mustafa","Kamil","Emre","Ayşe","Murat","Zeynep"]
})

print(df.head(n = 3))
print("*")
print(df["Column2"].nunique())
print("*")
print(df["Column2"].value_counts())
print(df[(df["Column1"] >= 4) & (df["Column2"] == 300)])

def times3(x):
    return x * 3

print("*")
print(df["Column2"].apply(times3))
print("*")
print(df["Column2"].apply(lambda x : x*2))
print("*")
print(df["Column3"].apply(len))
print("*****")
print(df)
df.drop("Column3",axis = 1,inplace = True)
print(df)

print(df.columns)
print("**")
print(len(df.index))
print(df.index.names)
print("********")

print(df.sort_values("Column2",ascending=False))

dFr = pd.DataFrame({
    "Ay": ["Mart","Nisan","Mayis","Mart","Nisan","Mayis","Mart","Nisan","Mayis"],
    "Şehir": ["Ankara","Ankara","Ankara","Istanbul","Istanbul","Istanbul","Izmir","Izmir","Izmir"],
    "Nem": [10,25,50,21,67,80,30,70,75]
})

print(dFr)
print("********")
print(dFr.pivot_table(index="Ay",columns="Şehir",values="Nem"))
print("---")
print(dFr.pivot_table(index="Şehir",columns="Ay",values="Nem"))

