import pandas as pd
import numpy as np
import math

global rutaArchivo
rutaArchivo = None
rutaArchivo = "Proyecto\Archivos\simulacion_1k.csv"

def valoresCSV(ruta):
    archivoCSV = pd.read_csv(ruta, header=0)
    totalPlays, totalChest1, totalChest2, totalQuantity = calculateSamples(1000)
    archivoCSV ["Plays"] = totalPlays
    archivoCSV ["Chest1"] = totalChest1
    archivoCSV ["Chest2"] = totalChest2
    archivoCSV ["Quantity"] = totalQuantity
    archivoCSV.to_csv(ruta, index=False)

def generateWins():
    thePlay = ""
    randomWin = np.random.randint(2, size=1)
    if ( randomWin == 1):
        thePlay = "win"
    else:
        thePlay = "lose"    
    return thePlay

def roulette(valor):
    typeChest = ""
    typeChest2 = ""
    firsValue = 0
    secondValue = 0
    if (valor == 'win'):
        randomRoulette = np.random.randint(10, size=1)
        if(randomRoulette >= 0 and randomRoulette <= 6):
            randomChest = np.random.randint(4,size=1)
            if (randomChest == 0):
                typeChest = 'Plata'
                firsValue = 1
            if (randomChest == 1):
                typeChest = 'Oro'
                firsValue = 3
            if (randomChest == 2):
                typeChest = 'Gigante'
                firsValue =5
            if (randomChest == 3):
                typeChest = 'Magico'
                firsValue = 7
        else:
            randomChest = np.random.randint(3,size=1)
            if(randomChest == 0):
                typeChest = 'SuperEspecial'
                firsValue = 7
            if(randomChest == 1):
                typeChest = 'SuperMagico'
                firsValue = 9
            if (randomChest == 2):
                typeChest = 'Legendario'
                firsValue = 10
        
        if(randomRoulette >= 0 and randomRoulette <= 6):
            randomChest2 = np.random.randint(4,size=1)
            if (randomChest2 == 0):
                typeChest2 = 'Plata'
                secondValue = 1
            if (randomChest2 == 1):
                typeChest2 = 'Oro'
                secondValue = 3
            if (randomChest2 == 2):
                typeChest2 = 'Gigante'
                secondValue = 5
            if (randomChest2 == 3):
                typeChest2 = 'Magico'
                secondValue = 7
        else:
            randomChest2 = np.random.randint(3,size=1)
            if(randomChest2 == 0):
                typeChest2 = 'SuperEspecial'
                secondValue = 7
            if(randomChest2 == 1):
                typeChest2 = 'SuperMagico'
                secondValue = 9
            if (randomChest2 == 2):
                typeChest2 = 'Legendario'
                secondValue = 10
    quantity = firsValue + secondValue
    print(typeChest , typeChest2, quantity)
    return typeChest, typeChest2, quantity

def calculateSamples(quantity):
    plays = []
    chest = []
    chest2 = []
    quantityList = []
    wins = 0
    for i in range (quantity):
        gameResult = generateWins()
        plays.append(gameResult)
        if (gameResult =="win"):
            wins = wins + 1
            typeChest, typeChest2, quantityCarts = roulette(gameResult)
            chest.append(typeChest)
            chest2.append(typeChest2)
            quantityList.append(quantityCarts)
        else: 
            chest.append('vacio')
            chest2.append('vacio')
            quantityList.append('vacio')


    print("Jugadas\n" , len(plays))
    print("Cofres\n" , len(chest) )
    print("Cofres2\n" , len(chest2))
    print("Cartas\n" , len(quantityList))
    return plays, chest, chest2, quantityList

valoresCSV(rutaArchivo)

