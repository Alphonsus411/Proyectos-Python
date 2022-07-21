# Funciones_2

from random import *


def GeneraNumeroAleatorio(minimo, maximo):
    try:
        if minimo > maximo:
            aux = minimo
            minimo = maximo
            maximo = aux
            return randint(minimo, maximo)
    except TypeError:
        print("Debes escribir números")
        return -1


i = 0
while i < 5:
    print(GeneraNumeroAleatorio("Adolfo", 10))

    i = i + 1
