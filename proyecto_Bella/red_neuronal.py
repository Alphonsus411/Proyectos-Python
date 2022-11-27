"""
Usando la unidad neuronal anterior, creamos una red neuronal para el procesamiento de entradas o inputs.
    
"""

import numpy as np
import unidad_neuronal as un

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
salidas = np.array([0,1,1,0])

red_neuronal = un.UnidadNeuronal(entradas, salidas)
red_neuronal.entrenamiento()
print(red_neuronal)
print(red_neuronal.prediccion([0,0]))
print(red_neuronal.prediccion([0,1]))
print(red_neuronal.prediccion([1,0]))
print(red_neuronal.prediccion([1,1]))

# Path: proyecto_Bella\red_neuronal.py