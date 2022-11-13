# polimorfismo

class Gato():
    def sonido(self):  # métodos iguales para animales diferentes
        print("Miau")


class Perro():
    def sonido(self):
        print("Guau")


class Cerdo():
    def sonido(self):
        print("Oink , Oink")


def EscucharSonido(animal):
    animal.sonido()  # llamamos al método de las clases Gato, Perro y Cerdo


Gato1 = Gato()  # creamos los objetos llamando a las clases relacionadas
Perro1 = Perro()
Cerdo1 = Cerdo()

EscucharSonido(Gato1)  # llamamos a la función que activa el método de las dos clases anteriores,
# basada en los objetos creados anteriormente
EscucharSonido(Perro1)
EscucharSonido(Cerdo1)
