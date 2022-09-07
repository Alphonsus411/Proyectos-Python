# funciones posicionales

"""def suma(*args):  # con este parámetro, puedo traer cualquier número de argumentos a la función
    suma = 0
    for arg in args:  # con esta iteración recorremos todos los argumentos existentes
        suma += arg
    return suma


resultado = suma(3, 4, 5)

print(resultado)"""

"""def lenguaje(nombre, *lenguajes): # cambiamos *arg por un nombre que define el grupo de parámetros
    print(f'Hola {nombre}')
    print(f'Tus lenguajes favoritos son: {lenguajes}')


lenguaje("Erick Zanussem", "Python", "Javascript", "R", "SQL")"""


def lenguaje(nombre, **lenguajes):  # uso de los **kwargs
    print(f'Hola {nombre}')
    print("Buscando información acerca de tus lenguajes favoritos...")
    print("Cargando información... \n")

    print("Información: ")
    contador = 0
    for clave in lenguajes:  # recorremos los lenguajes favoritos, usando el parámetro clave de uno en uno
        contador += 1
        print(f'Tu {contador} lenguaje favorito es {lenguajes[clave]}')


lenguaje("Erick Zanussem", lenguaje1 ="Python", lenguaje2 ="Javascript", lenguaje3 ="R", lenguaje4 ="SQL" )
# pasamos las claves en forma de diccionario

