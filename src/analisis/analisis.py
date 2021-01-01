import pandas as pd
import datetime

def getMonthExpenses(data, month, year=datetime.datetime.utcnow().year):
    df = getData()
    df = df[df['month'] == month & df['year'] == year]
    return df[df['Importe']<0]['Importe'].sum()

def getMonthIncome(data, month, year=datetime.datetime.utcnow().year):
    df = getData()
    df = df[df['month'] == month & df['year'] == year]
    return df[df['Importe']>0]['Importe'].sum()

def getTotalOfMonth(data, month, year=datetime.datetime.utcnow().year):
    df = getData()
    df = df[df['month'] == month & df['year'] == year]
    return df['Importe'].sum()


