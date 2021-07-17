from numpy import NAN, dtype
import pandas as pd

df2 = pd.read_csv("data/csv2/Aachen1868.csv")

#["Black","BlackElo",	"Date",	"ECO", "Event", "Result", "Round", "Site",	"White", "WhiteElo"]
#Things 2 do
#'??' to 01 in date column
#Jan-00 to 1-0
#Make 2 more columns White_Result and Black_result
#Make other ? as NAN
#Blank as NAN
#Create a game id column as primary key
#Convert the numeric columns to numeric

df2 = df2.fillna(NAN)
df2[["Date"]] = df2.Date.str.replace('\?\?','01')
df2['Date']= pd.to_datetime(df2['Date'])
df2.replace(to_replace =["\?", "\?\?"],value =NAN)
df2[["Result"]] = df2[["Result"]].replace("Jan-00","1-0")
df2[["Result"]] = df2[["Result"]].replace("1/2-1/2","0.5-0.5")
df2[["White_Result", "Black_result"]] = df2.Result.astype(str).str.split('-',expand = True)
df2[['BlackElo', 'WhiteElo', 'Black_result', 'White_Result']] = df2[['BlackElo', 'WhiteElo', 'Black_result', 'White_Result']].apply(pd.to_numeric)










#def preprocess(df2):
