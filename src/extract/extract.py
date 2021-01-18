import pandas as pd

def getData():
    path = "../../data/listado_de_movimientos.csv"
    df = pd.read_csv(path, delimiter=';', dtype = {'Importe':float}, decimal=",")
    return cleanData(data)
def cleanData(data):
    data.pop("Unnamed: 0")
    df['year'] = pd.DatetimeIndex(data['Fecha']).year
    df['month'] = pd.DatetimeIndex(data['Fecha']).month
    return df
