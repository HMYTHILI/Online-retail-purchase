import numpy as np
import pandas as pd

# read the data

features= pd.read_csv('Features data set.csv')
#print(features)
sales=pd.read_csv('sales data-set.csv')
#print(sales)
stores=pd.read_csv('stores data-set.csv')
#print(stores)

# DIAGNOSE DATA FOR CLEANING

#print(type(features))

# HEAD- TO GET TOP 5 DATA

#print(features.head())
#print(sales.head())
#print(stores.head())

# TAIL - TO GET BOTTOM 5 DATA

# print(features.tail())
# print(sales.tail())
# print(stores.tail())

# TO_DATETIME
features['Date']=pd.to_datetime(features['Date'])
#print(features['Date'])
sales['Date']=pd.to_datetime(sales['Date'])
#print(sales['Date'])

# NUMBER OF ROWS AND COLUMNS IN DATASET
# print("no of rows and columns in features:",features.shape)
# print("no of rows and columns in sales:",sales.shape)
# print("no of rows and columns in stores:",stores.shape)

# INFO- IT GIVES INFORMATION ABOUT DATAFRAME INCLUDING NON NULL VAUES, INDEX DTTYPE, COLUMN DTTYPE AND MEMORY STORAGE
# print(features.info())
# print(sales.info())
# print(stores.info())

#COLUMNS- TO EXACT HEADING
# print("\n column in features table",features.columns)
# print("\n column in sales table",sales.columns)
# print("\n column in stores table",stores.columns)

# MERGE THE DATA IN A UNIQUE DATAFRAME
# mergefeatures=pd.read_csv('merge features dataset.csv')
# mergesales=pd.read_csv('merge sales dataset.csv')
# mergestores=pd.read_csv('merge stores dataset.csv')

# ss= mergesales.sort_values(['Weekly_Sales'],ascending=[False])
# print(ss)

# df=pd.merge( mergefeatures,mergesales,on=['Date','Store','IsHoliday'],how='left')
# # #print(df)
# df=pd.merge(df,mergestores,on=['Store'],how='left')
# # #print(df)
# # df=df.fillna(0)
# # #print(df)
# df=df.sort_values(['Date',"Weekly_Sales"],ascending=[True,False],inplace=True)
#print(df)
#print(df)
# # print(df.head(7))
# #print(df.shape)
# #print(df.columns)
# #print(df.describe())
# #print(df.index)
# #print(df.values)

# MERGE THE DATA IN A UNIQUE DATAFRAME

# left merge using sales and features

df=pd.merge(sales,features,on=['Date','Store','IsHoliday'],how='left')
#print(df)

# left merge using sales,features and also store

df=pd.merge(df,stores,on=['Store'],how='left')
#print(df)

df=df.fillna(0)
#print(df)

# SORT_VALUES USING DATE AND WEEKLY_SALES

# s=sales.sort_values(['Date','Weekly_Sales'],ascending=[True,False], inplace= True)
# print(s)

# ss=sales.sort_values(['Date'],ascending=[False])
# print(ss.head(7))

#print(df.shape)
#print(df.columns)
#print(df.describe())

s=df.index
#print(s)

v=df.values
#print(v)

# SUBSETTING

subset=df[['Store','Date','Weekly_Sales','Fuel_Price','CPI','Unemployment']]
#print(subset)
#print(subset.head())
#print(df.head())

# LOC PROPERTY- to access a group of rows and columns by labels

#print(df.loc[0])
#print(df.loc[[0,99]])

# ILOC PROPERTY - INTERGER LOCATION BASED INDEXING FOR SELECTION BY POSITION

# print(df.iloc[0])
# print(df.iloc[[0,99]])

# ILOC using reversing 
# print(df.iloc[-1])


#subset using loc

# subset=df.loc[:,['Store','Date','Weekly_Sales']]
# print(subset.head())


# IX - indexing can be done by both position and name using ix.

# k=df.ix[0]
# print(k)

# SUBSET USING ILOC

# subset=df.iloc[:,[2,4]]
# print(subset.head())

#SUBSET USING ILOC

# subset=df.iloc[-5::2,:]
# print(subset.head())

# GROUPED CALCULATION

# print(df.head())

# m=df.groupby(['Date'])['CPI'].mean().head(10)
# print(m)

# n=df.groupby(['Store','Date'])[['Weekly_Sales','Unemployment']].mean()
# print(n)

# c=df.groupby(['Store','Date'])[['Weekly_Sales','Unemployment']].mean().reset_index().head(10)
# print(c)

# VISUALIZATION

import matplotlib.pyplot as plt

# MATPLOTLIB USING INLINE GRAPH

# z=df.groupby(['Store'])[['Weekly_Sales']].mean().plot()
# plt.show()

# MATPLOTLIB USING SCATTER

# x=df.plot(kind='scatter',x='Store',y='Weekly_Sales',rot=70)
# plt.show()

# MATPLOTLIB USING BOXPLOT

df.boxplot(column='Weekly_Sales',by='Store')
plt.show()
