# funciones con parámetros

"""def es_par(numero): # funcion con parámetro
    if numero % 2 == 0:
        print(f'El número {numero} es par')
    else:
        print(f'El número {numero} es impar')


es_par(5) # llamada de función con argumento"""

"""def saludar(nombre):
    print("Hola " + nombre + ",  estás aprendiendo a programar con Django")


saludar("Erick")"""

"""def resta(a=None, b=None):  # implica introducir los dos parámetros, o saldrá None
    if a is None or b is None:
        print("Error, debes enviar dos números a la función")  # si son introducidos los dos parámetros, no sale el
        # mensaje de error

        return
    return a - b


resultado = resta(5, 4)

print(resultado)"""


def multiplicacion(numero=None):
    if numero is None:
        print("Por favor, introduce un número")
    else:
        print(f'Tabla de Multiplicar del {numero}: ')
        for i in range(1, 11):
            print(f'{i} X {numero} = {i * numero}')


multiplicacion(5)


