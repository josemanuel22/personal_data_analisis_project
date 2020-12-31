import pandas as pd

def getData(dateInit, dateEnd):
    path = "../../data/listado_de_movimientos.csv"
    df = pd.read_csv(path, delimiter=';')
    #ADD dateInit, dateEnd parsing
    return cleanData(df)

def cleanData(data):
    data.pop("Unnamed: 0")
    data.pop("Unnamed: 6")
    return df
