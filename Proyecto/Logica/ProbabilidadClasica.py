from CreateCSV import rutaArchivo, valoresCSV

import pandas as pd
import numpy as np


def arrayCreation():
       global play
       global arrayCofre
       global arrayCarta
       global arrayQuantity 
       valoresCSV(rutaArchivo)
       df= pd.read_csv(rutaArchivo)
       play = np.array(df['Plays'].sort_values())
       arrayCofre = np.array(df['Chest'].sort_values())
       arrayCarta = np.array(df['Carts'].sort_values())
       arrayQuantity = np.array(df['Quantity'].sort_values())
       len(play)

def Probability():
       winCases = 0
       loseCases = 0
       plataChestCases = 0
       oroChestCases = 0
       giganteChestCases = 0
       magicoChestCases = 0
       superMagicoChestCases = 0
       superEspecialChestCases = 0
       legendarioChestCases = 0

       for i in range(len(play)):

              if (play[i] == "win"):
                     winCases = winCases + 1
                     if (arrayCofre[i] == "Plata"):
                            plataChestCases = plataChestCases + 1
                     if (arrayCofre[i] == "Oro"):
                            oroChestCases = oroChestCases + 1
                     if (arrayCofre[i] == "Gigante"):
                            giganteChestCases = giganteChestCases + 1
                     if (arrayCofre[i] == "Magico"):
                            magicoChestCases = magicoChestCases + 1
                     if (arrayCofre[i] == "SuperMagico"):
                            superMagicoChestCases = superMagicoChestCases + 1
                     if (arrayCofre[i] == "SuperEspecial"):
                            superEspecialChestCases = superEspecialChestCases + 1
                     if (arrayCofre[i] == "Legendario"):
                            legendarioChestCases = legendarioChestCases + 1
              else:
                     loseCases = loseCases + 1

       winProbability = winCases / len(play)
       loseProbability = loseCases / len(play)
       plataProbability = plataChestCases / len(play)
       oroProbability = oroChestCases / len(play)
       giganteProbability = giganteChestCases / len(play)
       magicoProbability = magicoChestCases / len(play)
       superMagicoProbability = superMagicoChestCases / len(play)
       superEspecialProbability = superEspecialChestCases / len(play)
       legendarioProbability =  legendarioChestCases / len(play)
       print('Casos ganados: ' , winCases)
       print(winProbability)
       print(loseProbability)

       print('Casos plata: ' , plataChestCases)
       print(plataProbability)
       print('Casos Oro: ' , oroChestCases)
       print(oroProbability)
       print('Casos Gigante: ' , giganteChestCases)
       print(giganteProbability)
       print('Casos Magicos: ' , magicoChestCases)
       print(magicoProbability)
       print('Casos Super Magico: ' , superMagicoChestCases)
       print(superMagicoProbability)
       print('Casos Super especial: ' , superEspecialChestCases)
       print(superEspecialProbability)
       print('Casos Legendarios: ' , legendarioChestCases)
       print(legendarioProbability)

arrayCreation()
Probability()
















