import pandas as pd

def getData():
    path = "../../data/listado_de_movimientos.csv"
    data = pd.read_csv(path, delimiter=';', dtype = {'Importe':float, 'Concepto': str}, decimal=",")
    return cleanData(data)

def cleanData(data):
    data.pop("Unnamed: 0")
    data['year'] = pd.DatetimeIndex(data['Fecha']).year
    data['month'] = pd.DatetimeIndex(data['Fecha']).month
    return data
