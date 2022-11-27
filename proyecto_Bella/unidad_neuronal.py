"""
Creamos una unidad neuronal con una sola neurona, 
pero con la capacidad de aprender de los datos de entrada, 
y mediante la lógica inferencial tomaR una decisión.

"""

import numpy as np

class UnidadNeuronal:
    def __init__(self, entradas, salidas):
        self.entradas = entradas
        self.salidas = salidas
        self.pesos = np.random.rand(entradas.shape[1])
        self.tasa_aprendizaje = 0.1

    def activacion(self, x):
        if x >= 0:
            return 1
        else:
            return 0

    def entrenamiento(self):
        for i in range(1000):
            resultado = self.activacion(np.dot(self.entradas, self.pesos))
            error = self.salidas[i] - resultado
            self.pesos += self.tasa_aprendizaje * error * self.entradas[i]

    def prediccion(self, entrada):
        return self.activacion(np.dot(entrada, self.pesos))
    
    def __str__(self):
        return f"pesos: {self.pesos}"
    
    def __repr__(self):
        return f"pesos: {self.pesos}"
    
    def __call__(self, entrada):
        return self.prediccion(entrada)

# Path: proyecto_Bella\main.py
