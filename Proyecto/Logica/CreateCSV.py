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
        print('Plata')
    elif round(randomChest) == 2:
        print('Oro')
    elif round(randomChest) == 3:
        print('Gigante')
    elif round(randomChest) == 4:
        print('Magico')

def generateCarts():
    typeCard = ""
    randomCard = np.random.uniform(1,100)

    print('Carta: ' , round(randomCard) )
    
    if round(randomCard) >= 1 and round(randomCard) <= 58:
        print('Comun')
    elif round(randomCard) >= 59 and round(randomCard) <= 78:
        print('Especiales')
    elif round(randomCard) >= 79 and round(randomCard) <= 89:
        print('Epicas')
    elif round(randomCard) >= 90 and round(randomCard) <= 100:
        print('Legendaria')


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