# herencia ejemplo práctico

class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresar_dato(self):
        self.datos = [int(input("ingresar datos" + str(i + 1) + "= ")) for i in range(self.n)]


class OperacionesBasicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

    def suma(self):
        a, b, = self.datos
        s = a + b
        print("El resultado es: ", s)

    def resta(self):
        a, b, = self.datos
        r = a - b
        print("El resultado es: ", r)

    def multiplicacion(self):
        a, b, = self.datos
        m = a * b
        print("El resultado es: ", m)

    def division(self):
        a, b, = self.datos
        d = a / b
        print("El resultado es: ", d)


class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)

    def cuadrada(self):
        import math
        a,  = self.datos
        print("El resultado es: ", math.sqrt(a))


ejemplo = Raiz()
print(ejemplo.ingresar_dato())
print(ejemplo.cuadrada())





