# genera una tabla de excel
def generar_tabla(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i * j, end="\t")
        print()


# genera una tabla de excel con formato
def generar_tabla_formato(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("{:4}".format(i * j), end="\t")
        print()


# genera una tabla de excel con formato y color
def generar_tabla_formato_color(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j % 2 == 0:
                print("{:4}".format(i * j), end="\t")
            else:
                print("{:4}".format(i * j), end="\t")
        print()


# genera una tabla de excel para usos de contabilidad
def generar_tabla_contabilidad(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("{:4}".format(i * j), end="\t")
        print()


# representa esos datos en una grafica de barras
def generar_grafica(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("{:4}".format(i * j), end="\t")
        print()


if __name__ == "__main__":
    n = int(input("Ingrese el valor de n: "))
    generar_tabla(n)
    generar_tabla_formato(n)
    generar_tabla_formato_color(n)
    generar_tabla_contabilidad(n)
    generar_grafica(n)
    print("Fin del programa")
    input("Presione enter para salir")
    exit()
