#inicia saludo
print("Hola, bienvenido a mi creador de lógica")
#inicia ciclo
while True:
    razonamiento = input("¿Qué quieres que haga? ")
    if razonamiento == "salir":
        print("Hasta pronto")
        break
    elif razonamiento == "sumar":
        print("Ingresa los números que quieres sumar")
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        print("El resultado es: ", num1 + num2)
    elif razonamiento == "restar":
        print("Resta dos números") #inicia ciclo
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        print("El resultado es: ", num1 - num2)
    elif razonamiento == "multiplicar":
        print("Multiplica dos números")
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        print("El resultado es: ", num1 * num2)
    elif razonamiento == "dividir":
        print("Divide dos números")
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        print("El resultado es: ", num1 / num2)
    elif razonamiento == "potencia":    #inicia ciclo
        print("Calcula la potencia de un número")
        num1 = int(input("Ingresa el número: "))
        num2 = int(input("Ingresa el exponente: "))
        print("El resultado es: ", num1 ** num2)
    elif razonamiento == "raiz":
        print("Calcula la raíz de un número")
        num1 = int(input("Ingresa el número: "))
        print("El resultado es: ", num1 ** 0.5)
    elif razonamiento == "factorial":   
        print("Calcula el factorial de un número")
        num1 = int(input("Ingresa el número: "))
        print("El resultado es: ", num1 * (num1 - 1) * (num1 - 2) * (num1 - 3) * (num1 - 4) * (num1 - 5) * (num1 - 6) * (num1 - 7) * (num1 - 8) * (num1 - 9) * (num1 - 10))
    elif razonamiento == "salir":
        print("Hasta pronto")
        break
    else:
        print("No entiendo")
        continue
    print("")
    
#fin del programa
print("Fin del programa")
print("Gracias por usarme")

