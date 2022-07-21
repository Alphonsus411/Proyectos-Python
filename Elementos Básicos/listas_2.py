# Escriba un programa que permita crear una lista con 5 palabras ingresadas por el usuario.


def ingresar_lista():
    lista = []
    for i in range(5):
        lista.append(input("Ingrese una palabra: "))
    return lista


def mostrar_lista(lista):
    print("Lista: ", lista)


# Dependiendo de la opción que este elija, el programa debe pedir el nombre del elemento que quiere añadir
# o caso contrario el que quiere eliminar, así mismo, si dijo que “no” quiere eliminar el elemento de la lista.

def agregar_elemento(lista):
    elemento = input("Ingrese un elemento a agregar: ")
    lista.append(elemento)
    return lista


if __name__ == "__main__":
    lista = ingresar_lista()
    mostrar_lista(lista)
    opcion = input("Desea agregar un elemento? (s/n): ")
    if opcion == "s":
        lista = agregar_elemento(lista)
        mostrar_lista(lista)
    else:
        print("No se agregará ningún elemento")

    opcion = input("Desea eliminar un elemento? (s/n): ")
    if opcion == "s":
        elemento = input("Ingrese un elemento a eliminar: ")
        lista.remove(elemento)
        mostrar_lista(lista)
    else:
        print("No se eliminará ningún elemento")
    mostrar_lista(lista)
    print("Lista final: ", lista)
    print("Fin del programa")
