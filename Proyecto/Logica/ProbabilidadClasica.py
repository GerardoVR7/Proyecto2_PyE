from CreateCSV import rutaArchivo

import pandas as pd
import numpy as np


def arrayCreation(self):
       global play
       global arrayCofre
       global arrayCarta
       global arrayQuantity 
       
       df= pd.read_csv(rutaArchivo)
       play = np.array(df['Plays'].sort_values())
       arrayCofre = np.array(df['Chest'].sort_values())
       arrayCarta = np.array(df['Carts'].sort_values())
       arrayQuantity = np.array(df['Quantity'].sort_values())


def clasicProbability():
       winCases = 0
       for i in range(len(play)):

              if (play[i] == "win"):
                     winCases = winCases + 1

       winProbability = 

















