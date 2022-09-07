# ciclo for

"""word = input("Ingrese una palabra: ")

for i in range(10):
    print(word)"""

"""print("Comienzo")

contador = 1

for i in [3, 4, 5, 7, 8]:
    print(f'Vuelta número: {contador}')
    print(f'Hola, ahora i vale {i} y su cuadrado vale {i**2}')
    contador += 1

print("Fin")"""

numero = int(input("Ingresa un número para una tabla de multiplicar: "))
print("")

print(f'Tabla de multiplicar del número {numero}')

for i in range(1, 11):
    print(f'{i} x {numero} = {i*numero}')








