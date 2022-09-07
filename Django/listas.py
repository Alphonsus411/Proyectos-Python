# listas

"""
Escribir un programa que almacene las asignaturas de un curso
"""
"""asignaturas = ["Matemáticas", "Física", "Castellano", "Inglés"]

print(asignaturas[3]) # llamamos al índice desde el parámetro de la lista
print(type(asignaturas))"""

"""""# Lotería

numeros = []

for i in range(6):
    numeros.append(int(input("Introduce un número: ")))  # le damos a la lista vacía la propiedad de poder añadir
    # elementos nuevos escribiéndolos desde la consola , usando el método append

numeros.sort()
print(f'Los números ganadores son: {numeros}')"""

lista = [1, 4, 5, 6, 7, 8, 6, "Hola"]

"""
lista.remove(6)  # método para eliminar elementos de la lista
lista.pop(2)  # método para eliminar por posición del elemento
del lista[0]   # método para eliminar también basado en posición
lista.clear()  # vacía una lista completa, también puede eliminar efectos de todos los métodos anteriores...
lista.count(6) # método para contar un elemento de la lista y cuántas veces se repite
lista.index("Hola")  # método para saber la posición de un elemento de la lista
"""

lista.reverse()  # método para posicionar la lista al revés

print(lista)











