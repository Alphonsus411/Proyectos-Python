import re

print(re.search(r"Py.*n", "Pygmalion"))

print(re.search(r"Py.*n", "Python Programming"))

print(re.search(r"Py[a-z]*n", "Python Programming"))
# modificamos el patrón de búsqueda para que se extienda más allá de la n

print(re.search(r"Py[a-z]*n", "Pyn"))

print(re.search(r"o+l+", "goldfish"))
# aquí hay otro modo de buscar patrones por coincidencias más cortas posibles

print(re.search(r"o+l+", "woolly"))

print(re.search(r"o+l+", "boil"))

print(re.search(r"p?each", "To each their own"))

print(re.search(r"p?each", "I like peaches"))




























