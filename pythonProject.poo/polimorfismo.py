# polimorfismo

class Automovil:
    rueda = 4

    def desplazamiento(self):
        print("El automovil se desplaza sobre cuatro ruedas")


class Moto:
    rueda = 2

    def desplazamiento(self): # puedo tener el mismo objeto con valores diferentes en dos clases completamente
        # independientes
        print("La moto se está moviendo sobre dos ruedas")
        


