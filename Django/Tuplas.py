# tuplas

"""
Crear una tupla con números,
luego pedir un número por teclado
e indicar cuántas veces se repite
"""

numeros = (5, 6, 7, 8, 5, 5, 6, 90, 12, 14, 12)

numero = int(input("Dame un número de la lista: "))  # creamos una variable para almacenar uno de los números de la
# lista

# print("El número se repite:  " + str(numeros.count(numero)) + " veces.")  # imprimimos el número contando el número
# de veces que se repite
print("El número " + str(numero) + " se encuentra en la posición: " + str(numeros.index(numero))) # imprimimos la
# posición de un número en la lista o tupla








