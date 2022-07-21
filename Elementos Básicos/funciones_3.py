# funciones_3
# crea una función que calcule el factorial de un número pasado por parámetro
# crea una función que, dados dos números, mostrará todos los números que hay entre ellos.

# def factorial(num):
# resultado = num

# for i in range(num - 1, 1, -1):
# resultado = resultado * i
# return resultado


# print(factorial(5))

def NumeroEntre(num1, num2):
    if num1 > num2:
        aux = num1
        num1 = num2
        num2 = aux
    for i in range(num1 + 1, num2):
        print(i)


NumeroEntre(10, 1)


