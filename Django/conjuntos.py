# conjuntos

"""
add // Añade un elemento al final del conjunto
clear // Elimina toda la información de un conjunto
pop // Devuelve y elimina un error arbitrario o devuelve un error si está vacío
remove // Intenta eliminar un elemento del conjunto, si no existe eleva un error
union // Devuelve un conjunto con todos los elementos de los conjuntos mezclados

"""

# primera forma para crear conjuntos

alumnos = {"Andrea", "Ruby", "Marcos", "Maldonado", "Jose"}

# print(alumnos)

# segunda forma para crear conjuntos

lenguajes = set(["PHP", "Java", "C#", "Python"])

# lenguajes.add("Ruby")
# lenguajes.clear()
# lenguajes.pop()
# lenguajes.remove("Java")

conjunto_total = alumnos.union(lenguajes)

print(conjunto_total)











