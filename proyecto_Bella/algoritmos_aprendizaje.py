"""
Aprovechando los anteriores parámetros, importamos la red neuronal y creamos algoritmos de aprendizaje.
Estos algoritmos de aprendizaje son los que nos permitirán entrenar a la red neuronal para que pueda realizar tareas concretas.  
    
"""
import numpy as np
import red_neuronal as rn

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
salidas = np.array([0,1,1,0])

RedNeuronal = np.array([entradas, salidas])

red_neuronal = rn.RedNeuronal(entradas, salidas)  # type: ignore
red_neuronal.entrenamiento()
print(red_neuronal)

# Path: proyecto_Bella\unidad_neuronal.py




