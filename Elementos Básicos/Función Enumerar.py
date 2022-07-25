def skip_elements(elements):
    # devuelve los elementos pares de la lista
    return elements[::2]


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ["Orange", "Pineapple", "Strawberry"  "Kiwi", "Peach"]))  # Should be ["Orange", "Strawberry", "Peach"]
