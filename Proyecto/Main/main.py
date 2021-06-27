import pandas as pd
import numpy as np

def valoresCSV(ruta):

    archivoCSV = pd.read_csv(ruta, header=0)
    print(archivoCSV)


valoresCSV("Archivos/simulacion_1k.csv")