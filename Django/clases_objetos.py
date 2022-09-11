# clases y objetos

class Bicicleta:
    def __init__(self, color, cambios, rin):  # método iniciador de los atributos de la clase
        self.color = color  # atributos de la clase, con self por delante
        self.cambios = cambios
        self.rin = rin

    def frenar(self):  # creamos los métodos de la clase bicicleta
        return " La bicicleta está frenando"

    def avanzar(self):
        return "La bicicleta está avanzando"

    def girar(self):
        return "La bicicleta está girando"


urbana = Bicicleta("Rojo", 8, 27.5)
hibrida = Bicicleta("Azul", 1, 29)

print("Urbana: " + str(urbana.color))  # el atributo no tiene paréntesis, el método sí
print("Comportamiento de la bicicleta Urbana: " + str(urbana.girar()))
print("\n")
print("Hibrida: " + "cambios " + str(hibrida.cambios))  # el atributo no tiene paréntesis, el método sí
print("Comportamiento de la bicicleta Hibrida: " + str(hibrida.frenar()))



