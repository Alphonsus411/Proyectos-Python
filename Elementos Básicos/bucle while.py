# Bucle While

import math

numero = int(input("Escriba un número:"))

while numero < 0:
    print('Error -> Debería ser un número positivo')
    numero = int(input("Escriba un número:"))

print(f"\nSu raíz cuadrada es: {(math.sqrt(numero)): .2f}")
