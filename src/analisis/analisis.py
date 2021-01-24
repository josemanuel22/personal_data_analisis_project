import sys
sys.path.append('/Users/jose/Documents/GitHub/personal_data_analisis_project/src/extract')
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

categories = { "Supermercado" : ["ahorramas", "corte", "dia", "carrefour", "Aldi"],
            "transporte" : ["renfe", "metro"],
            "Ocio": ["Glovo", "Amazon", "Mcdonalds", "Ginos", "Rodilla", "Pizzeria", "Starbucks"],
            "transferencias": ["Transferencia"]
        }

def categorizeData(data, month, year=datetime.datetime.utcnow().year):
    df = data[data['month'] == month][data['year'] == year]
    df.groupby(['Concepto']).sum()
    dfResults = pd.DataFrame(columns=categories.keys())
    for category in categories:
        res = 0
        for categoryStr in categories[category]:
            print(df['Concepto'].str.contains(categoryStr))
            res+=df[df['Concepto'].str.contains(categoryStr)]['Importe'].sum()
        dfResults[category] = res
    return dfResults

if __name__ == "__main__":
    from extract import *
    data = getData()
    print(categorizeData(data, 4, 2020))
