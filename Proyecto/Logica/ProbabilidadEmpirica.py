from CreateCSV import rutaArchivo, valoresCSV
from fractions import Fraction
import pandas as pd
import numpy as np


def arrayCreation():
       global play
       global arrayChest1
       global arrayChest2
       global arrayQuantity 
       valoresCSV(rutaArchivo)
       df= pd.read_csv(rutaArchivo)
       play = np.array(df['Plays'].sort_values())
       arrayChest1 = np.array(df['Chest1'].sort_values())
       arrayChest2 = np.array(df['Chest2'].sort_values())
       arrayQuantity = np.array(df['Quantity'].sort_values())
       print(len(arrayChest1))
       print(arrayChest2[1])

def empiricalProbability():
       winCases = 0
       loseCases = 0

       plataChestCases = 0
       oroChestCases = 0
       giganteChestCases = 0
       magicoChestCases = 0
       superMagicoChestCases = 0
       superEspecialChestCases = 0
       legendarioChestCases = 0
       print(arrayChest1)

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

def ClassicProbability():
       probWin= Fraction(1,2) 
       probChestComun= Fraction(1,4)
       probChestEspec= Fraction(1,14)
       probCard = Fraction(1,4)
       ChestPlat = 0
       ChestGold = 0
       ChestGigant = 0
       ChestMagic = 0 
       ChestSuperMagic = 0
       ChestSuperEspecial = 0
       ChestLegedary = 0
       
       probPrimercaso = probWin * probChestComun * probCard
       probSegundoCaso = probWin * probChestEspec * probCard	

       ChestPlat = probPrimercaso
       ChestGold = probPrimercaso
       ChestGigant = probPrimercaso
       ChestMagic = probPrimercaso
       ChestSuperMagic = probSegundoCaso
       ChestSuperEspecial = probSegundoCaso
       ChestLegedary = probSegundoCaso 
       
       print("Cofre Plata:" , ChestPlat)
       print("Cofre de Oro" , ChestGold)
       print("Cofre de Gigante" , ChestGigant)
       print("Cofre de Magico" , ChestMagic)
       print("Cofre de Super Magico" , ChestSuperMagic)
       print("Cofre de Super Especial" , ChestSuperEspecial)
       print("Cofre de Legendario" , ChestLegedary)

arrayCreation()
empiricalProbability()
