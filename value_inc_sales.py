# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:20:31 2024

@author: Pranith Prabhakar
"""

import pandas as pd

data = pd.read_csv('transaction2.csv')

data = pd.read_csv('transaction2.csv',sep= ';')  

data.info()

#wokring with calculations

costperitem = 11
sp =21
numberOfitems = 6
profitperitem   = 21 - 11

profitpertransaction = numberOfitems*profitperitem
costpertransaction = numberOfitems*costperitem
sellingpriceperitem = numberOfitems*sp

#adding column

data['costpertransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']
data['sellpertransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profitpertransaction

data['profitpertransaction'] = data ['sellpertransaction'] - data['costpertransaction']
data['Markup']= (data['profitpertransaction']) / data['costpertransaction']
data['Markup']= round(data['Markup'],2)

#converting datatype

day = data['Day'].astype(str)
year = data['Year'].astype(str)
my_date = day+'-'+data['Month']+'-'+ year

data['date'] = my_date

#iloc
data.iloc[0] #views the 1st row
data.iloc[0:3] #first 3 rows
data.iloc[4:2] #fourth column 2nd row

print(data.head())

#splitting columns

split = data['ClientKeywords'].str.split(',' , expand=True)

data['clientAge'] = split[0]
data['clienttype'] = split[1]
data['lengthofcontract'] = split[2]

#using the replace fn

data['clientAge'] = data['clientAge'].str.replace('[' , '')

data['lengthofcontract'] = data['lengthofcontract'].str.replace(']' , '')

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files 

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files

data = pd.merge(data, seasons, on='Month')

#dropping data

columns_to_drop = ['ClientKeywords']
data = data.drop(columns=columns_to_drop)

data = data.drop ('Year', axis = 1)
data = data.drop ('Day', axis = 1)
data = data.drop ('Month', axis = 1)

#exporting file back to CSV

data.to_csv('valueInc_cleaned.csv' , index = False)








