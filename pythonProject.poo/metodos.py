# metodos

# class Matematica:
# def suma(self):
# self.n1 = 2
# self.n2 = 3


# s = Matematica()
# s.suma()
# print(s.n1 + s.n2)

# class Ropa:
# def __init__(self):
# self.marca = "Emilio Tucci"
# self.talla = "XXL"
# self.color = "negro"


# traje = Ropa()
# print(traje.talla)
# print(traje.color)
# print(traje.marca)

class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1 * n2
        self.division = n1 / n2


operacion = Calculadora(5, 4)
print(operacion.resta)



