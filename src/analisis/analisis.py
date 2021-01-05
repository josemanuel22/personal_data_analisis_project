import pandas as pd
import datetime

def getMonthExpenses(data, month, year=datetime.datetime.utcnow().year):
    data = data[data['month'] == month & data['year'] == year]
    return data[data['Importe']<0]['Importe'].sum()

def getMonthIncome(data, month, year=datetime.datetime.utcnow().year):
    data = data[data['month'] == month & data['year'] == year]
    return data[data['Importe']>0]['Importe'].sum()

def getTotalOfMonth(data, month, year=datetime.datetime.utcnow().year):
    data = data[data['month'] == month & data['year'] == year]
    return data['Importe'].sum()

def categorizeData(data, month, year=datetime.datetime.utcnow().year):
    data = data[data['month'] == month & data['year'] == year]
    df.groupby(['Concepto']).sum()
    for category in categories:
        for categoryStr in category:
            df[df['Concepto'].str.contains(categoryStr)].sum()
            #TODO
