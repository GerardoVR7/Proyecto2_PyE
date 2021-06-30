import pandas as pd
import numpy as np
import math

def valoresCSV(ruta):

    archivoCSV = pd.read_csv(ruta, header=0)
    print(archivoCSV)


def generateWins():
    thePlay = ""
    randomWin = np.random.uniform(1,2)
    print('Numpy: ' , round(randomWin) )
    print('Numpy: ' , randomWin )
    if ( round(randomWin) == 1):
        thePlay = "win"
    else:
        thePlay = "lose"
    
    print(thePlay)
    return thePlay

def generateChest():
    typeChest = ""
    randomChest = np.random.uniform(1,4)

    print('Cofre: ' , round(randomChest) )

    if round(randomChest) == 1:
        typeChest = 'Plata'
        print('Plata')
    elif round(randomChest) == 2:
        typeChest = 'Oro'
        print('Oro')
    elif round(randomChest) == 3:
        typeChest = 'Gigante'
        print('Gigante')
    elif round(randomChest) == 4:
        typeChest = 'Magico'
        print('Magico')
    return typeChest

def generateCarts(typeChest):
    typeCard = ""
    quantityCarts = ""
    randomCard = np.random.uniform(1,100)

    print('Carta: ' , round(randomCard) )

    if (typeChest == 'Plata'):
        if round(randomCard) >= 1 and round(randomCard) <= 69:
            print('Comun')
        elif round(randomCard) >= 70 and round(randomCard) <= 88:
            print('Especiales')
        elif round(randomCard) >= 89 and round(randomCard) <= 98:
            print('Epicas')
        elif round(randomCard) >= 99 and round(randomCard) <= 100:
            print('Legendaria')
    elif (typeChest == 'Oro'):
        if round(randomCard) >= 1 and round(randomCard) <= 69:
            print('Comun')
        elif round(randomCard) >= 70 and round(randomCard) <= 85:
            print('Especiales')
        elif round(randomCard) >= 86 and round(randomCard) <= 96:
            print('Epicas')
        elif round(randomCard) >= 97 and round(randomCard) <= 100:
            print('Legendaria')
    elif (typeChest == 'Gigante'):
        if round(randomCard) >= 1 and round(randomCard) <= 58:
            print('Comun')
        elif round(randomCard) >= 59 and round(randomCard) <= 78:
            print('Especiales')
        elif round(randomCard) >= 79 and round(randomCard) <= 92:
            print('Epicas')
        elif round(randomCard) >= 93 and round(randomCard) <= 100:
            print('Legendaria')
    elif (typeChest == 'Magico'):
        if round(randomCard) >= 1 and round(randomCard) <= 58:
            print('Comun')
        elif round(randomCard) >= 59 and round(randomCard) <= 78:
            print('Especiales')
        elif round(randomCard) >= 79 and round(randomCard) <= 89:
            print('Epicas')
        elif round(randomCard) >= 90 and round(randomCard) <= 100:
            print('Legendaria')

    return typeCard, quantityCarts


def calculateSamples(quantity):
    plays = []
    chest = []
    carts = []
    for i in range (quantity):
        valor1 = generateWins()
        print(valor1)
        plays.append(valor1)
        if (valor1 =="win"):
            pass

valoresCSV("Proyecto/Archivos/simulacion_1k.csv")
generateWins()
generateChest()