"""
Aprovechando la red neuronal, creamos algoritmos predictivos.
Estos algoritmos predictivos son los que nos permitirán predecir el resultado de una tarea concreta.
Además estarán conectados con los algoritmos de aprendizaje para que puedan aprender de los resultados obtenidos.

"""
import numpy as np
import red_neuronal as rn
import algoritmos_predictivos as ap

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
salidas = np.array([0,1,1,0])

RedNeuronal = np.array([entradas, salidas])

red_neuronal = rn.RedNeuronal(entradas, salidas)  # type: ignore
red_neuronal.entrenamiento()
print(red_neuronal)

algoritmo_predictivo = ap.AlgoritmoPredictivo(entradas, salidas)  # type: ignore
algoritmo_predictivo.prediccion()
print(algoritmo_predictivo)

# Path: proyecto_Bella\algoritmos_predictivos.py

