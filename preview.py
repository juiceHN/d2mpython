# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:28:59 2021

@author: hugon
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb
import datetime

data = pd.read_csv('sales.csv')

# print(data.head())

############
# change column names to delete spaces
############
# data.info()

col_names = data.columns
new_names = []

for col in col_names:
    new_names.append(col.replace(" ", "_"))
data.columns = new_names
data.info()
data['Order_Date']=pd.to_datetime(data['Order_Date'])

# print(data.Sales.mean())

# meanCategorySales = data.groupby('Category').Quantity.mean()
# print(meanCategorySales)

# sb.barplot(data=data, x = "Category", y='Quantity')


users = pd.unique(data['Customer_ID'])
ed, rd, dd, yd = [], [], [], []

for user in users:
    temp = data.loc[data['Customer_ID'] == user]
    avg_Sales = temp.Sales.mean()
    ed.append(temp.Order_Date.min())
    rd.append(temp.Order_Date.max())
    yd.append(temp.Order_Year.max())
# users['first_order'] = ed
# users['last_order'] = rd
for i in range(len(ed)):
    dd.append(pd.to_datetime(rd[i])-pd.to_datetime(ed[i]))

user_data = pd.DataFrame(
    {'User_ID':users, 
     'First_Order':ed, 
     'Last_Order':rd, 
     'Date_Difference':dd,
     'Year_Last_Order':yd})

sb.histplot(user_data, x="Year_Last_Order")