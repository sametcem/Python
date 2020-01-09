import pandas as pd
import numpy as np

dataset = pd.read_csv("USvideos.csv")
newdataset1 = dataset.drop(["video_id","trending_date"],axis = 1)
print(newdataset1)

newdataset1.to_csv("USVideosNew2.csv",index= False)

excelset = pd.read_excel("excelfile.xlsx")
print(excelset)

excelset["Column5"] = ["Samet","Cem","Habiboglu","Udemy"]
print(excelset)

excelset.to_excel("excelfilenew.xlsx")

new = pd.read_html("https://www.contextures.com/xlSampleData01.html",header=0) # First index is header
print(new)