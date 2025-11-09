import pandas as pd

def cargar_datos(ruta):
    return pd.read_csv(ruta)

def eliminar_nulos(df):
    return df.dropna()

def normalizar(df):
    return (df - df.mean()) / df.std()

def guardar_datos(df, ruta_salida):
    df.to_csv(ruta_salida, index=False)
