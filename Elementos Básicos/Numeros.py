def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]


# La función odd_numbers devuelve una lista de números impares entre 1 y n, inclusive. Rellene los espacios en blanco de la función, utilizando la comprensión de listas. Sugerencia: recuerde que los contadores de lista y rango comienzan en 0 y terminan en el límite menos 1.

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10))  # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11))  # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1))  # Should print []
