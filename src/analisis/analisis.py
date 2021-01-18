import sys
sys.path.append('../extract')

import pandas as pd
import datetime

def getMonthExpenses(data, month, year=datetime.datetime.utcnow().year):
    data = data[data['month'] == month][data['year'] == year]
    return data[data['Importe']<0]['Importe'].sum()

def getMonthIncome(data, month, year=datetime.datetime.utcnow().year):
    data = data[data['month'] == month][data['year'] == year]
    return data[data['Importe']>0]['Importe'].sum()

def getTotalOfMonth(data, month, year=datetime.datetime.utcnow().year):
    data = data[data['month'] == month][data['year'] == year]
    return data['Importe'].sum()

def categorizeData(data, month, year=datetime.datetime.utcnow().year):
    df = data[data['month'] == month][data['year'] == year]
    df.groupby(['Concepto']).sum()
    dfResults = pd.DataFrame(columns=categories.keys())
    for category in categories:
        res = 0
        for categoryStr in category:
            res+=df[df['Concepto'].str.contains(categoryStr)]['Importe'].sum()
        dfResults[category] = res

