import pandas as pd
import numpy as np
import math

global superPlay
superPlay = False

global rutaArchivo
rutaArchivo = None
rutaArchivo = "Proyecto/Archivos/simulacion_1k.csv"

def valoresCSV(ruta):
    archivoCSV = pd.read_csv(ruta, header=0)
    
    print(archivoCSV)
    totalPlays, totalChest, totalCarts, totalQuantity = calculateSamples(1000)
    archivoCSV ["Plays"] = totalPlays
    archivoCSV ["Chest"] = totalChest
    archivoCSV ["Carts"] = totalCarts
    archivoCSV ["Quantity"] = totalQuantity
    archivoCSV.to_csv(ruta, index=False)

def generateWins():
    thePlay = ""
    randomWin = np.random.uniform(1,2)
    if ( round(randomWin) == 1):
        thePlay = "win"
    else:
        thePlay = "lose"    
    return thePlay

def generateChest(play, especialCase):
    typeChest = ""    
    print(play)
    print(especialCase)
    if (play == especialCase):
        randomChest = np.random.uniform(1,3)
        if round(randomChest) == 1:
            typeChest = 'SuperMagico'

        elif round(randomChest) == 2:
            typeChest = 'SuperEspecial'

        elif round(randomChest) == 3:
            typeChest = 'Legendario'
    else:
        randomChest = np.random.uniform(1,4)
        if round(randomChest) == 1:
            typeChest = 'Plata'

        elif round(randomChest) == 2:
            typeChest = 'Oro'

        elif round(randomChest) == 3:
            typeChest = 'Gigante'

        elif round(randomChest) == 4:
            typeChest = 'Magico'

    return typeChest

def generateCarts(typeChest):
    typeCard = ""
    quantityCarts = ""
    randomCard = np.random.uniform(1,100)

    if (typeChest == 'Plata'):
        if round(randomCard) >= 1 and round(randomCard) <= 69:

            typeCard = 'Comun'
            quantityCarts = 16
        elif round(randomCard) >= 70 and round(randomCard) <= 88:

            typeCard = 'Especial'
            quantityCarts = 2
        elif round(randomCard) >= 89 and round(randomCard) <= 98:

            typeCard = 'Epica'
            quantityCarts = 1
        elif round(randomCard) >= 99 and round(randomCard) <= 100:

            typeCard = 'Legendaria'
            quantityCarts = 1
    elif (typeChest == 'Oro'):
        if round(randomCard) >= 1 and round(randomCard) <= 69:

            typeCard = 'Comun'
            quantityCarts = 29
        elif round(randomCard) >= 70 and round(randomCard) <= 85:

            typeCard = 'Especial'
            quantityCarts = 10
        elif round(randomCard) >= 86 and round(randomCard) <= 96:

            typeCard = 'Epica'
            quantityCarts = 3
        elif round(randomCard) >= 97 and round(randomCard) <= 100:

            typeCard = 'Legendaria'
            quantityCarts = 1
    elif (typeChest == 'Gigante'):
        if round(randomCard) >= 1 and round(randomCard) <= 58:

            typeCard = 'Comun'
            quantityCarts = 300
        elif round(randomCard) >= 59 and round(randomCard) <= 78:

            typeCard = 'Especial'
            quantityCarts = 74
        elif round(randomCard) >= 79 and round(randomCard) <= 92:

            typeCard = 'Epicas'
            quantityCarts = 6
        elif round(randomCard) >= 93 and round(randomCard) <= 100:

            typeCard = 'Legendaria'
            quantityCarts = 1
    elif (typeChest == 'Magico'):
        if round(randomCard) >= 1 and round(randomCard) <= 58:

            typeCard = 'Comun'
            quantityCarts = 72
        elif round(randomCard) >= 59 and round(randomCard) <= 78:

            typeCard = 'Especial'
            quantityCarts = 21
        elif round(randomCard) >= 79 and round(randomCard) <= 89:

            typeCard = 'Epica'
            quantityCarts = 10
        elif round(randomCard) >= 90 and round(randomCard) <= 100:

            typeCard = 'Legendaria'
            quantityCarts = 1
    elif (typeChest == 'SuperMagico'):
        if round(randomCard) >= 1 and round(randomCard) <= 88:

            typeCard = 'Epica'
            quantityCarts = 35
        elif round(randomCard) >= 89 and round(randomCard) <= 100:

            typeCard = 'Legendaria'
            quantityCarts = 1
    elif (typeChest == 'SuperEspecial'):
        if round(randomCard) >= 1 and round(randomCard) <= 40:

            typeCard = 'Comun'
            quantityCarts = 400
        elif round(randomCard) >= 41 and round(randomCard) <= 100:

            typeCard = 'Especial'
            quantityCarts = 120
    elif (typeChest == 'Legendario'):
        if round(randomCard) >= 1 and round(randomCard) <= 100:

            typeCard = 'Legendaria'
            quantityCarts = 1      

    return typeCard, quantityCarts


def calculateSamples(quantity):
    plays = []
    chest = []
    carts = []
    quantityList = []
    especialCase = 241
    wins = 0
    for i in range (quantity):
        gameResult = generateWins()
        plays.append(gameResult)
        if (gameResult =="win"):
            wins = wins + 1
            chestResult = generateChest(wins,especialCase)
            chest.append(chestResult)
            cartResult, quantityResult = generateCarts(chestResult)
            carts.append(cartResult)
            quantityList.append(quantityResult)
            
        else: 
            chest.append("---")
            carts.append("---")
            quantityList.append("---")

    print("Jugadas\n" , len(plays))
    print("Cofres\n" , len(chest) )
    print("Cartas\n" , len(carts) )    
    return plays, chest, carts, quantityList

valoresCSV(rutaArchivo)
generateWins()
