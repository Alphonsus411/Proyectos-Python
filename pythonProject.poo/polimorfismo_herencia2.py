# polimorfismo con herencia

class Aves:
    def volar(self):
        print("La mayoría de las aves puede volar, pero algunas no")


class Aguila(Aves):
    def volar(self):
        print("Las aguilas pueden volar")


class Gallina(Aves):
    def volar(self):
        print("La gallina no puede volar")


object_ave = Aves()
object_aguila = Aguila()
object_gallina = Gallina()
object_ave.volar()
object_aguila.volar()
object_gallina.volar()




