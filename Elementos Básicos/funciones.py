# funciones en Python

def mi_funcion(name, edad):
    print("Hola  " + name + " tu edad es " + str(edad) + "!")


def suma_numeros(a, b):
    return a + b


# mi_funcion("Juan", "35")

suma = suma_numeros(5, 6)

print(suma)


def recursion(k):
    if k > 0:
        result = k + recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


recursion(7)
