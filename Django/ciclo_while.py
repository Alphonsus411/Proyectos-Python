# ciclo while
# Calculadora de Índice de Masa Corporal

print("Calculadora de Índice de Masa Corporal (IMC) \n")

contador = 0  # inicio del bucle while

while contador != 2:
    contador = int(input("Quieres seguir calculando el IMC? 1. Si y 2.No \n"))

    if contador == 1:
        estatura = float(input("Ingrese su estatura en metros: "))
        peso = float(input("Ingrese su peso en kilogramos: "))
        resultado = round(peso / (estatura ** 2), 2)  # fórmula del índice de masa corporal, con redondeo de dos
        # decimales al final

        if resultado < 18.5:
            print(f' IMC {resultado} = Por Debajo de tu Peso')
        elif 18.5 < resultado < 24.99:
            print(f' IMC {resultado} = Peso Normal')
        elif 19 < resultado < 30:
            print(f' IMC {resultado}= Sobrepeso, debe comenzar a cuidarse')
        elif resultado > 30:
            print(f' IMC {resultado}= Obesidad, debería ponerse a dieta')

        elif contador == 2:
            print("Hasta pronto")

print("Gracias por usar nuestra calculadora de IMC")

