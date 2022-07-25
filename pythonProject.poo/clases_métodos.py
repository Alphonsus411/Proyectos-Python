# clase y estático

class Pastel:
    def __init__(self, ingredientes):
        self.ingredientes = ingredientes

    def __repr__(self, ):  # retorna los valores generales del constructor
        return f'Pastel({self.ingredientes})'

    @classmethod
    def Pastel_chocolate(cls):  # trabaja con el término cls, en vez de self
        return cls(['harina', 'chocolate', 'huevos', 'leche', 'azucar'])

    @classmethod
    def Pastel_vainila(cls):
        return cls(['harina', 'vainilla', 'huevos', 'leche', 'azucar'])


print(Pastel.Pastel_chocolate())
