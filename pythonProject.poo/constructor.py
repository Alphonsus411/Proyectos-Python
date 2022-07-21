# constructor

class Persona:
    pass

    def __init__(self, nombre, ano):
        self.nombre = nombre
        self.ano = ano

    def descripcion(self):
        return " {} tiene {} años".format(self.nombre, self.ano)

    def comentario(self, frase):
        return "{} dice: {}".format(self.nombre, frase)


cientifico = Persona("Erick", 46)
print(cientifico.descripcion())
print(cientifico.comentario("Estamos programando en Python"))

