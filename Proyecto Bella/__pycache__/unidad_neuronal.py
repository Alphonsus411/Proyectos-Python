"""
Definimos una red neuronal de aprendizaje 

"""

import numpy as np

class UnidadNeuronal:
    def __init__(self, entradas, pesos, umbral):
        self.entradas = entradas
        self.pesos = pesos
        self.umbral = umbral

    def activacion(self):
        # Suma ponderada de las entradas
        suma = np.dot(self.entradas, self.pesos)
        # Aplicamos la función de activación
        if suma > self.umbral:
            return 1
        else:
            return 0

    def ajuste(self, error, tasa_aprendizaje):
        # Ajustamos los pesos
        self.pesos = self.pesos + tasa_aprendizaje * error * self.entradas
        # Ajustamos el umbral
        self.umbral = self.umbral + tasa_aprendizaje * error

    def __str__(self):
        return "Entradas: " + str(self.entradas) + " Pesos: " + str(self.pesos) + " Umbral: " + str(self.umbral)

if __name__ == "__main__":
    # Creamos la neurona
    neurona = UnidadNeuronal([1, 0], [0.5, 0.5], 0.5)
    print(neurona)
    # Calculamos la activación
    print(neurona.activacion())
    # Ajustamos los pesos
    neurona.ajuste(1, 0.1)
    print(neurona)
    
