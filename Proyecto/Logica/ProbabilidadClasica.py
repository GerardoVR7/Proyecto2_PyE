from CreateCSV import *

import pandas as pd
import numpy as np

class Prop:
 def openFile(self):
        global play
        global arrayCofre
        global arrayCarta
        global arrayQuantity 
        
        df= pd.read_csv(self.buscado)
        play = np.array(df['Plays'].sort_values())
        arrayCofre = np.array(df['Chest'].sort_values())
        arrayCarta = np.array(df['Carts'].sort_values())
        arrayQuantity = np.array(df['Quantity'].sort_values())
    