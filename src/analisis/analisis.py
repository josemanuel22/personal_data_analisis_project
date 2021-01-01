import pandas as pd
import datetime

def getMonthExpenses(data, month):
    df = getData()
    year = datetime.datetime.utcnow().year
    df = df[df['month'] == month & df['year'] == year]
    return df['Importe'].sum()

def getTotalMonthExpenses(data, month):
    #TODO

def getMonthIncome(data, month):
    #TODO

def getTotalMonthIncome(data, month):
    #TODO

