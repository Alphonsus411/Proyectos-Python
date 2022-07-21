# calculadora

print("Bienvenidos a la calculadora de Python")

numero1 = float(input("Escriba un número: "))
numero2 = float(input("Escriba un número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

opcion = str(input("Por favor, elija una opción: "))

if opcion == "suma":
    print('El resultado de la operacion es: {}'.format(str(suma)))
if opcion == "resta":
    print('El resultado de la operacion es: {}'.format(str(resta)))
if opcion == "multiplicacion":
    print('El resultado de la operacion es: {}'.format(str(multiplicacion)))
if opcion == "division":
    print('El resultado de la operación es: {}'.format(str(division)))
else:
    print('Gracias por usar este programa')
