from CreateCSV import rutaArchivo, valoresCSV
from fractions import Fraction
import pandas as pd
import numpy as np


ruta = "Proyecto/Archivos/simulacion_1k.csv"
shots = 1000


def arrayCreation(rutaArchivo,shots):
       global play
       global arrayChest1
       global arrayChest2
       global arrayQuantity 
       valoresCSV(rutaArchivo, shots)
       df= pd.read_csv(rutaArchivo)
       play = np.array(df['Plays'].sort_values())
       arrayChest1 = np.array(df['Chest1'].sort_values())
       arrayChest2 = np.array(df['Chest2'].sort_values())
       arrayQuantity = np.array(df['Quantity'].sort_values())
       print(len(arrayChest1))
       print(arrayQuantity)

def empiricalProbability():
       winCases = 0
       loseCases = 0
       #tipos de cofres
       plataChestCases = 0
       oroChestCases = 0
       giganteChestCases = 0
       magicoChestCases = 0
       superMagicoChestCases = 0
       superEspecialChestCases = 0
       legendarioChestCases = 0
       #salidas en cartas (las sumas)
       s1 = 2
       s2 = 4
       s3 = 6
       s4 = 8
       s5 = 10
       s6 = 12
       s7 = 14
       s8 = 16
       s9 = 17
       s10 = 18
       s11 = 19
       s12 = 20
       s1Case = 0
       s2Case = 0
       s3Case = 0
       s4Case = 0
       s5Case = 0
       s6Case = 0
       s7Case = 0
       s8Case = 0
       s9Case = 0
       s10Case = 0
       s11Case = 0
       s12Case = 0
       quantityEmpity = 0

       for i in range(len(play)):

              if (play[i] == "win"):
                     winCases = winCases + 1
              if (arrayChest1[i] == "Plata"):
                     plataChestCases = plataChestCases + 1
              if (arrayChest1[i] == "Oro"):
                     oroChestCases = oroChestCases + 1
              if (arrayChest1[i] == "Gigante"):
                     giganteChestCases = giganteChestCases + 1
              if (arrayChest1[i] == "Magico"):
                     magicoChestCases = magicoChestCases + 1
              if (arrayChest1[i] == "SuperMagico"):
                     superMagicoChestCases = superMagicoChestCases + 1
              if (arrayChest1[i] == "SuperEspecial"):
                     superEspecialChestCases = superEspecialChestCases + 1
              if (arrayChest1[i] == "Legendario"):
                     legendarioChestCases = legendarioChestCases + 1

              if (arrayChest2[i] == "Plata"):
                     plataChestCases = plataChestCases + 1
              if (arrayChest2[i] == "Oro"):
                     oroChestCases = oroChestCases + 1
              if (arrayChest2[i] == "Gigante"):
                     giganteChestCases = giganteChestCases + 1
              if (arrayChest2[i] == "Magico"):
                     magicoChestCases = magicoChestCases + 1
              if (arrayChest2[i] == "SuperMagico"):
                     superMagicoChestCases = superMagicoChestCases + 1
              if (arrayChest2[i] == "SuperEspecial"):
                     superEspecialChestCases = superEspecialChestCases + 1
              if (arrayChest2[i] == "Legendario"):
                     legendarioChestCases = legendarioChestCases + 1

              if (arrayQuantity[i] == str(s1)):
                     s1Case+= 1
              if (arrayQuantity[i] == str(s2)):
                     s2Case+=1
              if (arrayQuantity[i] == str(s3)):
                     s3Case+=1
              if (arrayQuantity[i] == str(s4)):
                     s4Case+=1
              if (arrayQuantity[i] == str(s5)):
                     s5Case+=1
              if (arrayQuantity[i] == str(s6)):
                     s6Case+=1
              if (arrayQuantity[i] == str(s7)):
                     s7Case+=1
              if (arrayQuantity[i] == str(s8)):
                     s8Case+=1
              if (arrayQuantity[i] == str(s9)):
                     s9Case+=1
              if (arrayQuantity[i] == str(s10)):
                     s10Case+=1
              if (arrayQuantity[i] == str(s11)):
                     s11Case+=1
              if (arrayQuantity[i] == str(s12)):
                     s12Case+=1
              if (arrayQuantity[i] == 'vacio'):
                     quantityEmpity += 1

              else:
                     loseCases = loseCases + 1

       winProbability = winCases / len(play)
       loseProbability = loseCases / len(play)

       plataProbability = plataChestCases / winCases
       oroProbability = oroChestCases / winCases
       giganteProbability = giganteChestCases / winCases
       magicoProbability = magicoChestCases / winCases
       superMagicoProbability = superMagicoChestCases / winCases
       superEspecialProbability = superEspecialChestCases / winCases
       legendarioProbability =  legendarioChestCases / winCases

       s1Probability = s1Case / 139
       s2Probability = s2Case / 139
       s3Probability = s3Case / 139
       s4Probability = s4Case / 139
       s5Probability = s5Case / 139
       s6Probability = s6Case / 139
       s7Probability = s7Case / 139
       s8Probability = s8Case / 139
       s9Probability = s9Case / 139
       s10Probability = s10Case / 139
       s11Probability = s11Case / 139
       s12Probability = s12Case / 139

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

       print('S1 Cases: ' , s1Case)
       print(round(s1Probability,4))
       print('S2 Cases: ' , s2Case)
       print(round(s2Probability,4))
       print('S3 Cases: ' , s3Case)
       print(round(s3Probability,4))
       print('S4 Cases: ' , s4Case)
       print(round(s4Probability,4))
       print('S5 Cases: ' , s5Case)
       print(round(s5Probability,4))
       print('S6 Cases: ' , s6Case)
       print(round(s6Probability,4))
       print('S7 Cases: ' , s7Case)
       print(round(s7Probability,4))
       print('S8 Cases: ' , s8Case)
       print(round(s8Probability,4))
       print('S9 Cases: ' , s9Case)
       print(round(s9Probability,4))
       print('S10 Cases: ' , s10Case)
       print(round(s10Probability, 4))
       print('S11 Cases: ' , s11Case)
       print(round(s11Probability,4))
       print('S12 Cases: ' , s12Case)
       print(round(s12Probability ,4))
       print('Empty Case: ' , quantityEmpity)
       

arrayCreation( ruta, shots )
empiricalProbability()
