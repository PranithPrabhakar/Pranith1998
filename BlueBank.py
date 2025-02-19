# -*- coding: utf-8 -*-
"""
Created on Fri May 24 01:11:16 2024

@author: Pranith Prabhakar
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method to read json data 
json_file = open ('loan_data_json.json')
data = json.load (json_file)

#transforming list to dataframe

loandata = pd.DataFrame(data)

#finding unique values in a column

loandata_unique = loandata['purpose'].unique()

#describe the data

loandata.describe ()

#using exp() to get the annual income 

income = np.exp(loandata['log.annual.inc'])

loandata['annualincome'] = income 

#working with ifs

#FICO scores

# fico >= 300 and < 400:
# 'Very Poor'
# fico >= 400 and ficoscore < 600:
# 'Poor'
# fico >= 601 and ficoscore < 660:
# 'Fair'
# fico >= 660 and ficoscore < 780:
# 'Good'
# fico >=780:
# 'Excellent'


#for loops

fruits = ['aaple', 'pear', 'banana']
    
for x in range(0,3):
    y= fruits[x] + ' for sale'
    print (y)

    
length = len(loandata)

ficoCategory = []
for x in range (0,length):
    category = loandata['fico'][x]
    
    try:
        
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 780:
            cat = 'Good'
        elif category >= 780:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
        ficoCategory.append(cat)   
    except:
        cat = 'Error- unknown'
    
    
#adding to loandata
ficoCategory = pd.Series(ficoCategory)

loandata['ficoCategory'] = ficoCategory


#using conditional statements using i.loc

loandata.loc[loandata['int.rate'] > 0.12 , 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12 , 'int.rate.type'] = 'Low'


#number of rows against a category (group by)

catplot = loandata.groupby (['ficoCategory']).size()
catplot.plot.bar()
plt.show

#scatter plot



xpoint = loandata['annualincome']
ypoint = loandata['dti']
plt.scatter(xpoint,ypoint)
plt.show()

#loandata to csv


xpoint = loandata['annualincome']
ypoint = loandata['dti']
plt.scatter(xpoint,ypoint)
plt.show()

