from CreateCSV import rutaArchivo, valoresCSV
from fractions import Fraction
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

       comunCartCases = 0
       especialCartCases = 0
       epicCartCases = 0
       legendaryCartCases = 0

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

                     if (arrayCarta[i] == "Comun"):
                            comunCartCases = comunCartCases + 1
                     if (arrayCarta[i] == "Especial"):
                            especialCartCases = especialCartCases + 1
                     if (arrayCarta[i] == "Epica"):
                            epicCartCases = epicCartCases + 1
                     if (arrayCarta[i] == "Legendaria"):
                            legendaryCartCases = legendaryCartCases + 1

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

       comunCartProbability = comunCartCases / len(play)
       especialCartProbability = especialCartCases / len(play)
       epicCartProbability = epicCartCases / len(play)
       legendaryCartProbability = legendaryCartCases / len(play)

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

<<<<<<< HEAD
       print('Casos cartas comunes: ' , comunCartCases)
       print('P: ' , comunCartProbability)
       print('Casos cartas especiales: ' , especialCartCases)
       print('P: ' , especialCartProbability)
       print('Casos cartas epicas: ' , epicCartCases)
       print('P: ' , epicCartProbability)
       print('Casos cartas legendarias: ' , legendaryCartCases)
       print('P: ' , legendaryCartProbability)

arrayCreation()
empiricalProbability()
=======
>>>>>>> 230ae64f98dd028ce91592f3ba9226b1e4f4baca

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
Probability()














