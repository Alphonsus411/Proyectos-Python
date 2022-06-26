#crea un programa de contador de geometría
def contador():
    print("""
    1. Cuadrado
    2. Triángulo
    3. Rectángulo
    4. Rombo
    5. Trapecio
    6. Salir
    """)
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        lado = int(input("Ingrese el lado: "))
        area = lado * lado
        print("El área del cuadrado es: ", area)
        contador()
    elif opcion == 2:
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))
        area = base * altura / 2
        print("El área del triángulo es: ", area)
        contador()
    elif opcion == 3:
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))
        area = base * altura
        print("El área del rectángulo es: ", area)
        contador()
    elif opcion == 4:
        diagonal = int(input("Ingrese la diagonal: "))
        area = diagonal * diagonal / 2
        print("El área del rombo es: ", area)
        contador()
    elif opcion == 5:
        base = int(input("Ingrese la base: "))
        altura = int(input("Ingrese la altura: "))
        area = base * altura / 2
        print("El área del trapecio es: ", area)
        contador()
    elif opcion == 6:
        print("Gracias por usar el programa")
        print("Erick Zanusemm")
        