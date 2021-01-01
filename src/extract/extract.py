import pandas as pd

def getData():
    path = "../../data/listado_de_movimientos.csv"
    df = pd.read_csv(path, delimiter=';')
    return cleanData(data)
def cleanData(data):
    data.pop("Unnamed: 0")
    data.pop("Unnamed: 6")
    df['year'] = pd.DatetimeIndex(df['Fecha']).year
    df['month'] = pd.DatetimeIndex(df['Fecha']).month
    return df
