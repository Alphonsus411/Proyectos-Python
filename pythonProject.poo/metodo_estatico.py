# metodo estático

import math


class Pastel:
    def __init__(self, ingredientes, tamano):
        self.ingredientes = ingredientes
        self.tamano = tamano

    def __repr__(self):  # al haber dos parámetros, tenemos que precisar cual de  los dos devolvemos con el return,
        # o quizás ambos, como en este ejemplo
        return f'Pastel({self.ingredientes}, 'f'{self.tamano})'

    def area(self):
        return self.tamano_area(self.tamano)

    @staticmethod  # valor independiente, no usa ni self ni cls
    def tamano_area(Area):
        return Area ** 2 * math.pi


NuevoPastel = Pastel(['harina', 'huevos', 'leche', 'crema', 'chocolate'], 4) # creamos un nuevo objeto porque en
# metodo estático es necesario
print(NuevoPastel.tamano_area(5))






