import re

"""
result = re.search(r"^(\w*), (\w*)$",
                   "Lovelace, Ada")  # el patrón de búsqueda \w sirve para letras, números y barras o guiones bajos
print(result)
print(result.groups())  # esta llamada a impresión pide el patrón por grupos
print(result[0])  # imprimimos todo el grupo
print(result[1])  # imprimimos uno de sus elementos
print(result[2])

print("{} {} ".format(result[2], result[1]))  # otra forma de imprimir todo el grupo

"""


def rearrange_name(name):  # creamos una función que realice estos procedimientos de manera automática
    result = re.search(r"^(\w*) (\w)*$", name)
    if result is None:
            return name

    return "{} {}".format(result[2], result[1])


rearrange_name("Lovelace, Ada")
rearrange_name("Zanussem, Erick")
rearrange_name("Hopper, Grace M.")
rearrange_name("Voltaire")

print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Zanussem, Erick"))
print(rearrange_name("Hopper, Grace M."))
print(rearrange_name("Voltaire"))

# Path: Interacción con PC\regular_expressions_capturing_groups.py




