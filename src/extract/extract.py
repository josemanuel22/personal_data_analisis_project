import pandas as pd

def getData(dateInit, dateEnd):
    path = "../../data/listado_de_movimientos.csv"
    df = pd.read_csv(path, delimiter=';')
    cleanData(df)
    df = df[df['Fecha'] >= dateInit & df['Fecha']<= dateEnd]
    return
def cleanData(data):
    data.pop("Unnamed: 0")
    data.pop("Unnamed: 6")
    return df
