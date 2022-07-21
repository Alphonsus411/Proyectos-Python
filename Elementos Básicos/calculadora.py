# crea una calculadora

import math
import os

calculadora = {'suma': lambda x, y: x + y, 'resta': lambda x, y: x - y, 'multiplicacion': lambda x, y: x * y,
               'division': lambda x, y: x / y}  # crea un diccionario con las operaciones


# agrega una funcion a un diccionario
def agregar_funcion(diccionario, nombre_funcion, funcion):
    diccionario[nombre_funcion] = funcion
    return diccionario


# agrega operaciones algebraicas a un diccionario
def agregar_operaciones(diccionario):
    diccionario = agregar_funcion(diccionario, 'suma', lambda x, y: x + y)
    diccionario = agregar_funcion(diccionario, 'resta', lambda x, y: x - y)
    diccionario = agregar_funcion(diccionario, 'multiplicacion', lambda x, y: x * y)
    diccionario = agregar_funcion(diccionario, 'division', lambda x, y: x / y)
    return diccionario


# agrega operaciones trigonometricas a un diccionario
def agregar_operaciones_trigonometricas(diccionario):
    diccionario = agregar_funcion(diccionario, 'seno', lambda x: math.sin(x))
    diccionario = agregar_funcion(diccionario, 'coseno', lambda x: math.cos(x))
    diccionario = agregar_funcion(diccionario, 'tangente', lambda x: math.tan(x))
    return diccionario


# agrega operaciones logaritmicas a un diccionario
def agregar_operaciones_logaritmicas(diccionario):
    diccionario = agregar_funcion(diccionario, 'logaritmo', lambda x: math.log(x))
    diccionario = agregar_funcion(diccionario, 'logaritmo base 10', lambda x: math.log10(x))
    return diccionario


# agrega operaciones de raiz a un diccionario
def agregar_operaciones_raiz(diccionario):
    diccionario = agregar_funcion(diccionario, 'raiz cuadrada', lambda x: math.sqrt(x))
    diccionario = agregar_funcion(diccionario, 'raiz cubica', lambda x: math.cbrt(x))  # type: ignore
    return diccionario


# agrega operaciones de potencia a un diccionario
def agregar_operaciones_potencia(diccionario):
    diccionario = agregar_funcion(diccionario, 'potencia', lambda x, y: math.pow(x, y))
    return diccionario


# agrega operaciones de raiz cuadrada a un diccionario
def agregar_operaciones_raiz_cuadrada(diccionario):
    diccionario = agregar_funcion(diccionario, 'raiz cuadrada', lambda x: math.sqrt(x))
    return diccionario


# agrega operaciones de raiz cubica a un diccionario
def agregar_operaciones_raiz_cubica(diccionario):
    diccionario = agregar_funcion(diccionario, 'raiz cubica', lambda x: math.cbrt(x))  # type: ignore
    return diccionario


# agrega operaciones de matrices a un diccionario
def agregar_operaciones_matrices(diccionario):
    diccionario = agregar_funcion(diccionario, 'matriz', lambda x, y: x * y)
    return diccionario


# agrega operaciones de integracion a un diccionario
def agregar_operaciones_integracion(diccionario):
    diccionario = agregar_funcion(diccionario, 'integracion', lambda x, y: x + y)
    return diccionario


# genera una interfaz para la calculadora
def generar_interfaz():
    print('Bienvenido a la calculadora')
    print('Por favor ingrese una operacion')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    print('5. Seno')
    print('6. Coseno')
    print('7. Tangente')
    print('8. Logaritmo')
    print('9. Logaritmo base 10')
    print('10. Raiz cuadrada')
    print('11. Raiz cubica')
    print('12. Potencia')
    print('13. Matriz')
    print('14. Integracion')
    print('15. Salir')
    print('16. Ayuda')
    print('17. Limpiar pantalla')
    print('18. Limpiar pantalla y salir')


# inicia la calculadora
def iniciar_calculadora():
    calculadora = {}
    calculadora = agregar_operaciones(calculadora)
    calculadora = agregar_operaciones_trigonometricas(calculadora)
    calculadora = agregar_operaciones_logaritmicas(calculadora)
    calculadora = agregar_operaciones_raiz(calculadora)
    calculadora = agregar_operaciones_potencia(calculadora)
    calculadora = agregar_operaciones_raiz_cuadrada(calculadora)
    calculadora = agregar_operaciones_raiz_cubica(calculadora)
    calculadora = agregar_operaciones_matrices(calculadora)
    calculadora = agregar_operaciones_integracion(calculadora)
    generar_interfaz()
    while True:
        try:
            operacion = input('Ingrese una operacion: ')
            if operacion == '1':
                print('Ingrese el primer numero: ')
                numero1 = float(input())
                print('Ingrese el segundo numero: ')
                numero2 = float(input())
                print('El resultado de la suma es: ' + str(calculadora['suma'](numero1, numero2)))
            elif operacion == '2':
                print('Ingrese el primer numero: ')
                numero1 = float(input())
                print('Ingrese el segundo numero: ')
                numero2 = float(input())
                print('El resultado de la resta es: ' + str(calculadora['resta'](numero1, numero2)))
            elif operacion == '3':
                print('Ingrese el primer numero: ')
                numero1 = float(input())
                print('Ingrese el segundo numero: ')
                numero2 = float(input())
                print('El resultado de la multiplicacion es: ' + str(calculadora['multiplicacion'](numero1, numero2)))
            elif operacion == '4':
                print('Ingrese el primer numero: ')
                numero1 = float(input())
                print('Ingrese el segundo numero: ')
                numero2 = float(input())
                print('El resultado de la division es: ' + str(calculadora['division'](numero1, numero2)))
            elif operacion == '5':
                print('Ingrese el numero: ')
                numero = float(input())
                print('El resultado del seno es: ' + str(calculadora['seno'](numero)))
            elif operacion == '6':
                print('Ingrese el numero: ')
                numero = float(input())
                print('El resultado del coseno es: ' + str(calculadora['coseno'](numero)))
            elif operacion == '7':
                print('Ingrese el numero: ')
                numero = float(input())
                print('El resultado de la tangente es: ' + str(calculadora['tangente'](numero)))
            elif operacion == '8':
                print('Ingrese el numero: ')
                numero = float(input())
                print('El resultado del logaritmo es: ' + str(calculadora['logaritmo'](numero)))
            elif operacion == '9':
                print('Ingrese el numero: ')
                numero = float(input())
                print('El resultado del logaritmo base 10 es: ' + str(calculadora['logaritmo base 10'](numero)))
            elif operacion == '10':
                print('Ingrese el numero: ')
                numero = float(input())
                print('El resultado de la raiz cuadrada es: ' + str(calculadora['raiz cuadrada'](numero)))
            elif operacion == '11':
                print('Ingrese el numero: ')
                numero = float(input())
                print('El resultado de la raiz cubica es: ' + str(calculadora['raiz cubica'](numero)))
            elif operacion == '12':
                print('Ingrese el numero: ')
                numero = float(input())
                print('Ingrese el exponente: ')
                exponente = float(input())
                print('El resultado de la potencia es: ' + str(calculadora['potencia'](numero, exponente)))
            elif operacion == '13':
                print('Ingrese el numero: ')
                numero = float(input())
                print('Ingrese el exponente: ')
                exponente = float(input())
                print('El resultado de la matriz es: ' + str(calculadora['matriz'](numero, exponente)))
            elif operacion == '14':
                print('Ingrese el numero: ')
                numero = float(input())
                print('Ingrese el exponente: ')
                exponente = float(input())
                print('El resultado de la integracion es: ' + str(calculadora['integracion'](numero, exponente)))
            elif operacion == '15':
                print('Gracias por usar la calculadora')
                break
            elif operacion == '16':
                print('Ingrese el numero: ')
                numero = float(input())
                print('Ingrese el exponente: ')
                exponente = float(input())
                print('El resultado de la matriz es: ' + str(calculadora['matriz'](numero, exponente)))
            elif operacion == '17':
                os.system('clear')
            elif operacion == '18':
                os.system('clear')
                break
            else:
                print('Operacion no valida')
        except ValueError:
            print('Ingrese un numero')


# cierra la calculadora
def cerrar_calculadora():
    print('Gracias por utilizar la calculadora')
    exit()
